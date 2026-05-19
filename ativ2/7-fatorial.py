fatorial = 0

num = int(input('Digite um numero: '))

for i in range(1, num + 1):
    if i == 1:
        fatorial = i
    else:
        fatorial *= i
print(f'O fatorial de {num} é: {fatorial}')