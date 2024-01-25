import unittest

from eval import Eval
from environment import Environment


class TestVariables(unittest.TestCase):
    def setUp(self):
        self.environment = Environment(global_record={'VERSION': '0.0.1', 'true': True, 'false': False})
        self.eva = Eval(env=self.environment)

    def test_global_definition(self):
        self.assertEqual(self.eva.eval('VERSION'), '0.0.1')
        self.assertEqual(self.eva.eval(['var', 'isTrue', 'true']), True)

    def test_variable_assignments(self):
        self.assertEqual(self.eva.eval(['var', 'x', 3]), 3)
        self.assertEqual(self.eva.eval('x'), 3)


if __name__ == '__main__':
    unittest.main()
