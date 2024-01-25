class Eval:
    def eval(self, exp):
        if self.is_number(exp):
            return exp
        elif self.is_string(exp):
            return exp[1:-1]
        elif exp[0] == '/':
            return self.eval(exp[1]) / self.eval(exp[2])
        elif exp[0] == '*':
            return self.eval(exp[1]) * self.eval(exp[2])
        elif exp[0] == '+':
            return self.eval(exp[1]) + self.eval(exp[2])
        elif exp[0] == '-':
            return self.eval(exp[1]) - self.eval(exp[2])

    @staticmethod
    def is_number(exp):
        return isinstance(exp, int) or isinstance(exp, float)

    @staticmethod
    def is_string(exp):
        if not isinstance(exp, str):
            return False

        return exp[0] == exp[-1] == '"'
