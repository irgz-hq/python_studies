from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina_de_escrever = MaquinaDeEscrever()

print(escritor.nome)
print(caneta.marca)
print(maquina_de_escrever)

escritor.ferramenta = MaquinaDeEscrever()
escritor.ferramenta.escrever()

escritor.ferramenta = Caneta('Bic')
escritor.ferramenta.escrever()
