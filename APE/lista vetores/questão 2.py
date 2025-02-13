import random

vetor =[]
vetores_unicos=[]
for i in range(5):
    vetor.append(random.randint(1,60))
 
for i in range(len(vetor)):
    if vetor[i] not in vetores_unicos:
        vetores_unicos.append(vetor[i])
    
print(vetor)
print(vetores_unicos)