nome1=input('digite o nome 1: ')
idade1=int(input('digite a idade 1: '))

nome2=input('digite o nome 2: ')
idade2=int(input('digite a idade 2: '))

if idade1>idade2:
    print(f'{nome1} é mais velho(a)')

elif idade2>idade1:
    print(f'{nome2} é o mais velho(a)')
else:
    print('as idades são iguais')
