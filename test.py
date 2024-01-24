import unittest

from scanner import Scanner


class TestScanner(unittest.TestCase):
    def setUp(self):
        self.scanner = Scanner()

    def test_number(self):
        self.assertEqual(self.scanner.eval(1), 1)

    def test_string(self):
        self.assertEqual(self.scanner.eval('1'), '1')


if __name__ == '__main__':
    unittest.main()
