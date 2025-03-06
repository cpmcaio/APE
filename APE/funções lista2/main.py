
# Escreva um programa para ler a quantidade de estudantes de uma turma. 
# Gere uma lista contendo notas aleatórias para esses estudantes, com valores entre 0 e 100.

# Calcular e exibir:
# a) As notas dos estudantes.
# b) A média das notas da turma.
# c) A quantidade de estudantes com nota acima da média da turma.
# d) A quantidade de estudantes com nota abaixo da média da turma.
# e) A quantidade de estudantes aprovados (nota maior ou igual a 70).
# f) A quantidade de estudantes reprovados (nota menor que 70).
# g) A quantidade de estudantes que não possuem nota entre 70 e 80 (inclusive).
# h) Notas que foram encontradas na avaliação.
# i) Nota(s) mais frequente(s).

# Utilize as funções da biblioteca manipula_lista.py.

import manipula_lista as ml

quantidade=int(input("digite a quantidade de alunos"))

# Gera a lista de notas aleatórias para os alunos
notas = ml.gerar_lista(quantidade, 0, 100)

# a) Exibe as notas dos estudantes
print("\nNotas dos estudantes:")
ml.exibir_lista(notas)

# b) Calcula e exibe a média das notas da turma
media = ml.calcular_media(notas)
print("\nMédia das notas da turma:", media)

# c) Exibe a quantidade de estudantes com nota acima da média
qtd_acima_media = ml.quantidade_elementos_acima_da_media(notas)
print("\nQuantidade de estudantes com nota acima da média:", qtd_acima_media)

# d) Exibe a quantidade de estudantes com nota abaixo da média
qtd_abaixo_media = ml.quantidade_elementos_abaixo_da_media(notas)
print("\nQuantidade de estudantes com nota abaixo da média:", qtd_abaixo_media)

# e) Exibe a quantidade de estudantes aprovados (nota >= 70)
aprovados = ml.quantidade_elementos_entre_dois_valores(notas, 70, 100)
print("\nQuantidade de estudantes aprovados:", aprovados)

# f) Exibe a quantidade de estudantes reprovados (nota < 70)
reprovados = ml.quantidade_elementos_fora_de_um_intervalo(notas, 70, 100)
print("\nQuantidade de estudantes reprovados:", reprovados)

# g) Exibe a quantidade de estudantes que não possuem nota entre 70 e 80 (inclusive)
fora_entre_70_80 = ml.quantidade_elementos_fora_de_um_intervalo(notas, 70, 80)
print("\nQuantidade de estudantes com nota fora do intervalo [70, 80]:", fora_entre_70_80)

# h) Exibe as notas que foram encontradas na avaliação (elementos distintos)
notas_distintas = ml.elementos_distintos(notas)
print("\nNotas encontradas na avaliação (distintas):", notas_distintas)

# i) Exibe a(s) nota(s) mais frequente(s)
nota_mais_frequente = ml.elemento_mais_frequente(notas)
print("\nNota(s) mais frequente(s):", nota_mais_frequente)

