from random import randint

vetor=[]

while(len(vetor)<6):
    x=randint(1,60)
    if x not in vetor:
        vetor.append(x)
    else:
        continue

print(vetor)

for i in range (len(vetor)):
    for k in range(i+1,len(vetor)):
        if vetor[i]>vetor[k]:
            vetor[i], vetor[k] = vetor[k], vetor[i]
print(vetor)