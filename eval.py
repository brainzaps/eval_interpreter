import re

from environment import Environment


class Eval:
    global_env = Environment()

    def __init__(self, env=None):
        self.global_env = env or self.global_env

    def eval(self, exp, env=None):
        env = env or self.global_env

        if self.is_number(exp):
            return exp
        if self.is_string(exp):
            return exp[1:-1]

        # Math operations
        if exp[0] == '/':
            return self.eval(exp[1]) / self.eval(exp[2])
        if exp[0] == '*':
            return self.eval(exp[1]) * self.eval(exp[2])
        if exp[0] == '+':
            return self.eval(exp[1]) + self.eval(exp[2])
        if exp[0] == '-':
            return self.eval(exp[1]) - self.eval(exp[2])

        # Variable assignment
        if exp[0] == 'var':
            name, value = exp[1:]
            return env.define(name, self.eval(value))

        if self.is_variable_name(exp):
            return env.lookup(exp)

        raise Exception('Unknown expression: {}'.format(exp))

    def is_variable_name(self, exp):
        return isinstance(exp, str) and self.is_valid_variable_name(exp)

    @staticmethod
    def is_valid_variable_name(name):
        return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name) is not None

    @staticmethod
    def is_number(exp):
        return isinstance(exp, int) or isinstance(exp, float)

    @staticmethod
    def is_string(exp):
        if not isinstance(exp, str):
            return False

        return exp[0] == exp[-1] == '"'
