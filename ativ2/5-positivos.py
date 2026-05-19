positivos = 0
num = 0
while num >= 0:
    num = int(input('Digite um numero: '))
    if num > 0:
        positivos += 1

print(f'foram digitados {positivos} numeros positivos')