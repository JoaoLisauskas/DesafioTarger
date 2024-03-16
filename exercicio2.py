numero = int(input("Verifique se o numero pertence a Fibonacci: "))
a = 0
b = 1

while numero > a:
    a, b = b, a + b

    if numero == a:
        print(f'{numero} pertence ao Fibonacci')
    
if numero != a:
    print(f'{numero} Não pertence ao Fibonacci')



             