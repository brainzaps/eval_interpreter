class Environment:
    def __init__(self, global_record=None):
        self.record = global_record or {}

    def define(self, name, value):
        self.record[name] = value
        return value

    def lookup(self, name):
        if name not in self.record:
            raise ReferenceError(f'Variable {name} is not defined')

        return self.record[name]
