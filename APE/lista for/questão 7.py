count=0
for i in range (8):
    nota=int(input('Digite a nota: '))
    if nota>0 and nota<100:
        count+=1
        
print(f'foram informadas {count} notas para o suap')
        
