class Scanner:
    def eval(self, exp):
        if self.is_number(exp):
            return exp
        elif self.is_string(exp):
            return exp

    @staticmethod
    def is_number(exp):
        return isinstance(exp, int) or isinstance(exp, float)

    @staticmethod
    def is_string(exp):
        return isinstance(exp, str)
