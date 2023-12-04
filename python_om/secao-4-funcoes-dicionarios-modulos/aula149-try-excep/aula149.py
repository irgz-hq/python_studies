# Tru, except, else e finally

try:
    a = 18
    b = 0
    print(b[0])
    print("linha antes do possível erro")
    c = a / b
    print("linha depois do possível erro")
except ZeroDivisionError:
    print("não é possivel dividir por zero")
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError):
    print('TypeError ou IndexError')
# a maior classe de erro é Exception
except Exception:
    print('ERRO DESCONHECIDO.')

print("CONTINUAR")