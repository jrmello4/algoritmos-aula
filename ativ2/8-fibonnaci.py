fibonacci = 0
proximo = 1
num = int(input('Digite um numero: '))

for i in range(1, num):
    fibonacci, proximo = proximo, fibonacci + proximo
print(f'O {num}° termo é: {fibonacci}')