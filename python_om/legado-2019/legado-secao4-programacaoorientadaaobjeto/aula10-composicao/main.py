from classes import Clientes, Endereco

cliente1 = Clientes("Luigui", 26)
cliente1.insere_endereco("Maceió", "AL")
cliente1.lista_enderecos()

#aqui esse del serve para deletar a instancia e nesse programa mostrar que a classe
#Enderecos tbem eh apagada por causa da agregacao, lembrando que nao precisa chamar
#Endereco la em cima, pq ela ja foi instanciada dentro da classe Clinetes.
del cliente1
print()


cliente2 = Clientes("Maria", 55)
cliente2.insere_endereco("Rio de Janeiro", "RJ")
cliente2.insere_endereco("Salvador", "Bahia")
cliente2.lista_enderecos()
del cliente2
print()

print('##########################################################')
print("A partir daqui eh o garbet colector do Python: ")
