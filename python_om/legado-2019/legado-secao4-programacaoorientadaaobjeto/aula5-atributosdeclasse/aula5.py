"""
quando vc chamar a variavel a partir da instancia, ele vai procurar primeiro
na instancia e depois na classe
"""
class A:
    vc = 123

a1 = A()
a2 = A()

a1.vc = 321

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

print(a1.vc)
print(a2.vc)
print(A.vc)
