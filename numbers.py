num = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))
num3 = int(input('digite mais um numero: '))

if num > num2 and num > num3:
    print(f'{num} é o maior numero')
elif num < num2 and num2 > num3:
    print(f'{num2} é o maior numero')
elif num3 > num and num3 > num2:
    print(f'{num3} é o maior numero')
else:
    print('os numeros são iguais')