# Tru, except, else e finally
# instância é um objeto de uma classe
string = 'Luigui'
print(isinstance(string, str))

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
except (TypeError, IndexError) as error:
    print('TypeError ou IndexError')
    print('MSG', error)
    print('Nome:', error.__class__.__name__)
# a maior classe de erro é Exception
except Exception:
    print('ERRO DESCONHECIDO.')

print("CONTINUAR")
