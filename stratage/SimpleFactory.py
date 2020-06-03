class Program:
    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op

    def cal(self):
        if self.op == '-':
            return self.a - self.b
        elif self.op == '+':
            return self.a + self.b
        elif self.op == '*':
            return self.a * self.b
        elif self.op == '/':
            return self.a / self.b
        else:
            print("Error op!")
            return None

p = Program(2,3,'-')
print(p.cal())