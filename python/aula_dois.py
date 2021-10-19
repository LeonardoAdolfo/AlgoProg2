num= int(input('De o numero desejado: '))

if (num%2)==0:
    print('Numero Par')
else:
    print('Numero Impar')



n1 = int(input('De o lado do triângulo'))
n2 = int(input('De o lado do triângulo'))
n3 = int(input('De o lado do triângulo'))


if(n1 + n2 > n3) or (n1 + n3 > n2) or (n3 + n2 > n1):
    if(n1 == n2) and (n1 == n3):
        print('Equilátero')
    elif (n1 == n2) or (n2 == n3) or (n3 == n1):
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Não é triângulo')












