import random
vetor = [random.randint(0, 20) for _ in range(50)]
soma= sum (vetor)
ocorrencia9=0
maior_valor= 0
for i in range(len(vetor)):
    if vetor[i]==9:
        ocorrencia9+=1
    if vetor[i] > maior_valor:
        maior_valor = vetor[i]
print (soma)
print(ocorrencia9)
print(maior_valor)
