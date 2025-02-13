import random
vetor=[]
while(len(vetor)<6):
    x=random.randint(1,6)
    if x not in vetor:
        vetor.append(x)
    else:
        continue

print(vetor)