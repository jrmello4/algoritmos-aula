salario = float(input('digite seu salario: '))

if salario > 5000:
    desconto = salario * 0.10
    print(f'o desconto do imposto é de: {desconto:.2f}')
else:
    desconto = salario * 0.05
    print(f'O desconto do imposto é de: {desconto:.2f}')