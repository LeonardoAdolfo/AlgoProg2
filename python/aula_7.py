def media(vet):
    s=0
    m=0
    for i in range(5):
        s+=vet[i]
        m +=1
    return s/m


vet = []
for i in range(5):
    vet.append(int(input('Numero: ')))
resp = media(vet)
print(f'A media foi {resp}')



# vet = []
# for i in range(5):
#     vet.append(int(input('Numero: ')))
# resp = soma(vet)
# print(f'A soma foi {resp}')