class Calculadora:

    def soma(self, a, b):
        return a + b
    
    def subt(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def divi(self, a, b):
        return a / b

c = Calculadora()
print("a + b = : ", c.soma(5,7))
print("a - b = : ", c.subt(10,4))  
print("a x b = : ", c.mult(2,3))  
print("a / b = : ", c.divi(9,3))