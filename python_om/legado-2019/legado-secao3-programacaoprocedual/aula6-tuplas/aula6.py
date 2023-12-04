t1 = 1,
t2 = (1)  # não é tupla
t3 = (1,2,3)
t4 = 1,2,3
t5 = 3*t4 + t3
n1, n2, n3, *_, n4 = t5
print(t1 )
print(t5)
print(type(t1), type(t2), type(t3), type(t4))
print(n1,n4)