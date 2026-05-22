while True:
    print('=== MENU ===')
    print('1. Jogar')
    print('2. Configurações')
    print('3. Ajuda')
    print('4. Sair')
    
    opcao = input('\nEscolha uma opção: ')
    
    if opcao == '1':
        print('Você escolheu a opção 1 para Jogar\n')
    elif opcao == '2':
        print('Você escolheu a opção 2 para Configurações\n')
    elif opcao == '3':
        print('Você escolheu a opção 3 para Ajuda\n')
    elif opcao == '4':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida! Tente novamente.\n')
