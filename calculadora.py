def calculate():
    operation = input('''
Escolha a operação que você gostaria:
+  para adição
-  para subtração
*  para multiplicação
/  para divisão
m  para média
%  para porcentagem
r  para raiz quadrada
^  para potência (elevado)
!  para fatorial
''')
    if operation in ['+', '-', '*', '/', 'm', '%', '^']:
        numero_1 = float(input('Coloque o primeiro número: '))
        numero_2 = float(input('Coloque o segundo número: '))

        if operation == '+':
            print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')


        elif operation == '-':
            print(f'{numero_1} - {numero_2} = {numero_1 - numero_2}')

        elif operation == '*':
            print(f'{numero_1} * {numero_2} = {numero_1 * numero_2}')

        elif operation == '/':
            if numero_2 != 0:
                print(f'{numero_1} / {numero_2} = {numero_1 / numero_2}')
            else:
                print('Erro: divisão por zero!')

        elif operation == 'm':
            print(f'Média entre {numero_1} e {numero_2} = {(numero_1 + numero_2) / 2}')

        elif operation == '%':
            print(f'{numero_1}% de {numero_2} = {(numero_1 / 100) * numero_2}')

        elif operation == '^':
            print(f'{numero_1} ^ {numero_2} = {numero_1 ** numero_2}')

    elif operation == 'r':
        numero = float(input('Coloque o número: '))
        if numero >= 0:
            raiz = numero ** 0.5   
            print(f'Raiz quadrada de {numero} = {raiz}')
        else:
                        print('Erro: não existe raiz real de número negativo!')

    elif operation == '!':
        numero = int(input('Coloque o número inteiro: '))
        if numero >= 0:
            fatorial = 1
            for i in range(1, numero + 1): 
                fatorial *= i
            print(f'{numero}! = {fatorial}')
        else:
            print('Erro: fatorial não existe para números negativos!')

    else:
        print('Você não escreveu uma operação válida, tente novamente.')

    again()

def again():
    calc_again = input(''' 
Você quer calcular novamente? 
Aperte S para SIM e N para NÃO: ''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('tchau bb, ate a proxima.')
    else:
        again()

calculate()

