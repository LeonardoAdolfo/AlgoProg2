nota = []
aluno = int(input('Qual a quantidade de alunos: '))

for n in range(aluno):
    nota.append(int(input('De a nota: '))) 
calcMedia = 0
media = 0
for n in range(aluno):
    media += nota[n] 

calcMedia = media/aluno 

print('A media foi {}'.format(calcMedia))

acima = 0
for n in range(aluno):
    if aluno[n] >= media:
        acima += 1

print('A media de alunos acima da media foi {}'.format(acima))