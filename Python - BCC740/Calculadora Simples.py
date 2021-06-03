class Calculadora:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subt(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def divi(self):
        return self.a / self.b

c = Calculadora(6,5)
print("a + b = : ", c.soma())
print("a - b = : ", c.subt())  
print("a x b = : ", c.mult())  
print("a / b = : ", c.divi())        