from random import randint
#valor do for
N=int(input())

#vetor padrão
vetorA=[]

#vetor do cálculo
vetorB=[]

#adiciona um numero ao vetor seguinte o loop n
for i in range(N):
    vetorA.append(randint(1,100))
#vai verificar se o vetor A é par
for k in range(len(vetorA)):
     if vetorA[k] % 2 == 0:
        vetorB.append(0)
#caso seja, 0, caso não, 1.
     else: 
        vetorB.append(1)
print(vetorA)
print(vetorB)

