# vet = []
# for n in range(5):
#     vet.append(int(input('De o elemento do vetor: ')))

# def maior_elemento(vet):
#     maior = 0
#     for i in range(5):
#         if(vet[i] > maior):
#             maior = vet[i]
#     return maior

# print('O maior numero é {}'.format(maior_elemento(vet)))

# vet = []
# for n in range(5):
#     vet.append(int(input('De o elemento do vetor: ')))

# def menor_elemento(vet):
#     menor = 0
#     for i in range(5):
#         if(vet[i] < menor):
#             menor = vet[i]
#     return menor

# print('O menor numero é {}'.format(menor_elemento(vet)))

vet = []
for n in range(5):
    vet.append(int(input('De o elemento do vetor: ')))

def soma(vet):
    soma = 0 
    for n in range(5):
        if((vet[n]%2)!=0):
            soma += vet[n]
    return soma

def media_impar(vet):
    media = 0
    s = soma(vet)
    media = s/5
    return media

print('A media é {}'.format(media_impar(vet)))