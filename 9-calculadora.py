valor = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))
operacao = int(input('digite a operação desejada: \n 1 - soma \n 2 - subtracao \n 3 - multiplicacao \n 4 - divisao \n'))
if operacao == 1:
    print(f'{valor} + {valor2} = {valor + valor2}')
elif operacao == 2:
    print(f'{valor} - {valor2} = {valor - valor2}')
elif operacao == 3:
    print(f'{valor} * {valor2} = {valor * valor2}')
elif operacao == 4:
    print(f'{valor} / {valor2} = {valor / valor2}') 
else:
    print('Operação invalida')