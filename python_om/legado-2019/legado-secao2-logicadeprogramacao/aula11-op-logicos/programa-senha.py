"""
Operadores logicos

and, or, not, in, not in
"""

#programinha de senha

login = input("Cadastre o seu login: ")
senha = input(f"Cadastre a sua senha para o login {login}: ")
senha_confirm = input(f"Confirme sua senha para o login {login}: ")

if senha != senha_confirm:
    print("senhas invalidas ")
else:
    login_confirm = input(f"Entre no sistema, para isso, digite o seu login: ")
    senha_confirm2 = input(f"Digite a sua senha: ")
    if login == login_confirm and senha == senha_confirm2:
        print(f"Usuario {login} esta logado no sistema! ")
    else:
        print("Voce nao esta logado no sistema, login ou senha incorretos. ")
