import random
#criando vetor
vetor = []
#adicionando número aleatórios ao vetor
for i in range(10):
    vetor.append(random.randint(1,5))
#criando o booleano da repetição
repetição=False

#o primeiro loop percorre o vetor
for i in range(len(vetor)):
    #o segundo loop percorre o vetor novamente
    for k in range(i+1, len(vetor)):
        #se o valor de i for igual ao valor de k, o booleano se torna verdadeiro
        if vetor[i]==vetor[k]:
            repetição=True
            print("há repetição")
            break
if repetição == False:
    print("não há repetição")
print(vetor)