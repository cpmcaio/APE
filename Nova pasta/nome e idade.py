def ler_dados():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    return nome, idade

nome1, idade1 = ler_dados()
nome2, idade2 = ler_dados()


if idade1 > idade2:
    print(f"A pessoa mais velha é: {nome1}")
else:
    print(f"A pessoa mais velha é: {nome2}")
