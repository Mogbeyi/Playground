class State:

    def __init__(self, value):
        self.value = value

    def increase(self):
        return self.value + 1

    def decrease(self):
        return self.value - 1

a = State(4)
print(a.value)
print(a.increase())
