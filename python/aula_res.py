# soma = 0
# for n in range(500):
#     if n % 3 == 0 and n % 2 != 0:
#         soma += n
# else:
#     print(soma)

#n1 = int(input('De o 1° n°: '))
#n2 = int(input('De o 2° n°: '))
#n3 = int(input('De o 3° n°: '))


# if n1 > n2 > n3:
#     print( n1,"-", n2,"-", n3)
# elif n2 > n1 > n3:
#     print( n2,"-", n1,"-", n3)
# elif n3 > n2 > n1:
#     print(n3,"-", n2,"-", n1)


sum = 0

for i in range(10):
    n4 = int(input('De o {}° n°: '.format(i)))
    if n4%2==0:
        sum += n4
    else: 
        print('Numero Impar')
else:
    print('A media dos números pares foi {}'.format((sum/10)))
