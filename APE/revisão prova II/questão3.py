from random import randint
matriz=[]
vetor_diagonal_principal=[]
vetor_diagonal_secundaria=[]

for i in range(5):
    matriz.append([0]*5)

for i in range(5):
    for k in range(5):
        matriz[i][k]=randint(1,20)

for i in range(5):
    vetor_diagonal_principal.append(matriz[i][i])
    vetor_diagonal_secundaria.append(matriz[i][5-i-1])

print ("diagonal secundária: ", vetor_diagonal_secundaria)
print("diagonal principal: ",vetor_diagonal_principal)

print("matriz: ",*matriz,sep="\n")

