peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e voce esta abaixo do peso')
elif imc >=18.5:
    print(f'Seu IMC é {imc:.2f} e voce esta com peso normal')
elif imc >= 25:
    print(f'Seu IMC é {imc:.2f} e voce esta com sobrepeso')
elif imc >= 30:
    print(f'Seu IMC é {imc:.2f} e voce esta com obesidade')