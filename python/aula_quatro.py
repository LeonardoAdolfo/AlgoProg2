
# i = 0
# sum = 0
# opcao = 9999999999
# while(opcao != 0):
#     opcao = int(input('De o numero desejado: '))
#     if(opcao % 2 == 0 ):
#         sum += opcao
#         i += 1
        
# print('A media de {}'.format((sum/i)))

# opcao = 999999999999999999

# while(opcao != -1):
#     opcao = int(input('De a tabuada desejada: '))
#     for n in range(1,11):
#         print('{} x {} = {}'.format(opcao, n, (opcao*n)))

n1 = int(input('De o primeiro numero '))
n2 = int(input('De o segundo numero '))

op = str(input('Qual operação desejada: + Adição; - Subtração; * Multiplicação; / Divisão: '))

if(op == '+'):
    print('A soma deu {}'.format(n1+n2))
elif(op == '-'):
    print('A subtração deu {}'.format(n1-n2))
elif(op=='*'):
    print('A multiplicação deu {}'.format(n1*n2))
elif(op == '/'):
    print('A divisão deu {}'.format(n1/n2))
