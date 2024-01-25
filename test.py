import unittest

from eval import Eval


class TestScanner(unittest.TestCase):
    def setUp(self):
        self.eval = Eval()

    def test_number(self):
        self.assertEqual(self.eval.eval(1), 1)

    def test_string(self):
        self.assertEqual(self.eval.eval('"hello world"'), 'hello world')

    def test_addition(self):
        self.assertEqual(self.eval.eval(['+', 1, 5]), 6)
        self.assertEqual(self.eval.eval(['+', ['+', 2, 3], 5]), 10)

    def test_multiplication(self):
        self.assertEqual(self.eval.eval(['*', 1, 5]), 5)
        self.assertEqual(self.eval.eval(['*', ['*', 2, 3], 5]), 30)
        self.assertEqual(self.eval.eval(['+', ['*', 2, 3], 5]), 11)

    def test_division(self):
        self.assertEqual(self.eval.eval(['/', 6, 3]), 2)

    def test_subtraction(self):
        self.assertEqual(self.eval.eval(['-', 6, 3]), 3)


if __name__ == '__main__':
    unittest.main()
