import random
vetor = [0]*10

for i in range(10):
    vetor[i]=(random.randint(1,60))

vetor_semrep=[]

for i in range(10):
    if vetor[i] not in vetor_semrep:
        vetor_semrep.append(vetor[i])

if len(vetor)==len(vetor_semrep):
    print("não há repetição")
else: 
    print("há repetição")
print(vetor)
print(vetor_semrep)



