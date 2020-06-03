class Opreation:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def cal(self):
        rst = None
        return rst


class OpreationAdd(Opreation):
    def __init__(self):
        Opreation.__init__(self)

    def cal(self):
        return self.a + self.b


class OpreationSub(Opreation):
    def __init__(self):
        Opreation.__init__(self)

    def cal(self):
        return self.a - self.b


class SimpleFactory:
    def __init__(self, op):
        self.op = op

    def getOperation(self):
        if self.op == '+':
            return OpreationAdd()
        elif self.op == '-':
            return OpreationSub()


sim = SimpleFactory('-').getOperation()
sim.a = 3
sim.b = 1
print(sim.cal())
