palavra = list(input("Digite uma palavra: "))
tamanho = len(palavra)
contador = -1
inverso = ''

while contador >= -tamanho:
    inverso += f'{palavra[contador]}'
    contador -= 1
print(inverso)