# essa funcao so funciona com str

qtd_caracters_fixo = 8
usuario = input(f"Digite o seu usuario (minimo {qtd_caracters_fixo} caracters): ")
qtd_caracters = len(usuario)

if qtd_caracters >= qtd_caracters_fixo:
    print(f"Usuario {usuario} cadastrado no sistema! ")
else:
    print(f"Usuario nao cadastrado no sistema, precisa de no minimo {qtd_caracters_fixo} caracters! ")
