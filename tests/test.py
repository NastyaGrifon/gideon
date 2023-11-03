import os
import sys
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(__file__), "..")))
from gideon import clear_terminal
import platform
import unittest

class TestClearTerminal(unittest.TestCase):
    def test_clear_terminal_windows(self):
        import platform
        platform.system = lambda: 'Windows'
        self.assertEqual(clear_terminal(), 'cls')

    def test_clear_terminal_linux(self):
        import platform
        platform.system = lambda: 'Linux'
        self.assertEqual(clear_terminal(), 'clear')

    def test_clear_terminal_darwin(self):
        import platform
        platform.system = lambda: 'Darwin'
        self.assertEqual(clear_terminal(), 'clear')

    def test_clear_terminal_unknown(self):
        import platform
        platform.system = lambda: 'Unknown'
        with self.assertRaises(Exception):
            clear_terminal()

if __name__ == '__main__':
    unittest.main()
