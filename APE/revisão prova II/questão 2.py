from random import randint

#delcarando vetor
matriz=[]
#criando a matriz 
for i in range(20):
    matriz.append([0]*50)
#preenchendo
for i in range(20):
    for j in range(50):
        matriz[i][j]=randint(1,100)
#numero que ele vai procurar 
k=int(input())
#busca
for i in range(20):
    for j in range(50):
        if matriz[i][j]==k:
            print(i, j)