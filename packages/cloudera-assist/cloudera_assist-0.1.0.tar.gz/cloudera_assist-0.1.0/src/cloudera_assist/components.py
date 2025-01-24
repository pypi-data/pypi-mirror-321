# Copyright 2025 Cloudera, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import contextlib
import os
import sys
import termios
import threading


@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


class KeyboardThread(threading.Thread):
    def __init__(self, callback, name="keyboard-input-thread"):
        self.callback = callback
        super(KeyboardThread, self).__init__(name=name, daemon=True)
        self.start()

    def run(self):
        with raw_mode(sys.stdin):
            try:
                # See https://github.com/pallets/click/blob/main/src/click/_termui_impl.py#L733
                encoding = (
                    getattr(sys.stdin, "encoding", None) or sys.getdefaultencoding()
                )
                while True:
                    if self.callback(os.read(sys.stdin.fileno(), 32).decode(encoding)):
                        break
            except (KeyboardInterrupt, EOFError):
                pass
