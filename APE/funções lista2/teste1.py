# test_ml.py

import manipula_lista as ml

# Teste 1 - Gerar lista
lista_gerada = ml.gerar_lista(5, 1, 10)
print("Teste 1 - Lista gerada:", lista_gerada)
# Esperado: Uma lista com 5 números aleatórios entre 1 e 10 (exemplo: [3, 5, 7, 1, 10])

# Teste 2 - Exibir lista
print("\nTeste 2 - Exibindo lista:")
ml.exibir_lista([10, 20, 30, 40])
# Esperado: Exibição dos números 10, 20, 30 e 40 em linhas separadas

# Teste 3 - Calcular média
media = ml.calcular_media([10, 20, 30, 40])
print("\nTeste 3 - Média:", media)
# Esperado: Média de [10, 20, 30, 40] = (10 + 20 + 30 + 40) / 4 = 25.0

# Teste 4 - Elementos acima da média
acima_media = ml.elementos_acima_da_media([10, 20, 30, 40])
print("\nTeste 4 - Elementos acima da média:", acima_media)
# Esperado: Elementos acima da média (25) = [30, 40]
# **Depende da média calculada no Teste 3.**

# Teste 5 - Elementos abaixo da média
abaixo_media = ml.elementos_abaixo_da_media([10, 20, 30, 40])
print("\nTeste 5 - Elementos abaixo da média:", abaixo_media)
# Esperado: Elementos abaixo da média (25) = [10, 20]
# **Depende da média calculada no Teste 3.**

# Teste 6 - Elementos entre dois valores
entre_valores = ml.elementos_entre_dois_valores([10, 20, 30, 40, 50], 20, 40)
print("\nTeste 6 - Elementos entre 20 e 40:", entre_valores)
# Esperado: Elementos entre 20 e 40 (inclusive) = [20, 30, 40]

# Teste 7 - Elementos fora de um intervalo
fora_valores = ml.elementos_fora_de_um_intervalo([10, 20, 30, 40, 50], 20, 40)
print("\nTeste 7 - Elementos fora do intervalo [20, 40]:", fora_valores)
# Esperado: Elementos fora do intervalo [20, 40] = [10, 50]

# Teste 8 - Elementos distintos
distintos = ml.elementos_distintos([10, 20, 30, 10, 40, 20])
print("\nTeste 8 - Elementos distintos:", distintos)
# Esperado: Elementos distintos = [10, 20, 30, 40]

# Teste 9 - Elemento(s) mais frequente(s)
mais_frequente = ml.elemento_mais_frequente([10, 20, 30, 10, 40, 20])
print("\nTeste 9 - Elemento(s) mais frequente(s):", mais_frequente)
# Esperado: Elementos mais frequentes = [10, 20] (ambos aparecem 2 vezes)
# **Não depende de cálculo anterior, mas deve ser revisado se o código atual estiver correto.**

# Teste 10 - Quantidade de elementos acima da média
qtd_acima = ml.quantidade_elementos_acima_da_media([10, 20, 30, 40])
print("\nTeste 10 - Quantidade de elementos acima da média:", qtd_acima)
# Esperado: Quantidade de elementos acima da média (25) = 2 (30 e 40)
# **Depende da média calculada no Teste 3.**

# Teste 11 - Quantidade de elementos abaixo da média
qtd_abaixo = ml.quantidade_elementos_abaixo_da_media([10, 20, 30, 40])
print("\nTeste 11 - Quantidade de elementos abaixo da média:", qtd_abaixo)
# Esperado: Quantidade de elementos abaixo da média (25) = 2 (10 e 20)
# **Depende da média calculada no Teste 3.**

# Teste 12 - Quantidade de elementos entre dois valores
qtd_entre = ml.quantidade_elementos_entre_dois_valores([10, 20, 30, 40, 50], 20, 40)
print("\nTeste 12 - Quantidade de elementos entre 20 e 40:", qtd_entre)
# Esperado: Quantidade de elementos entre 20 e 40 (inclusive) = 3 (20, 30, 40)

# Teste 13 - Quantidade de elementos fora de um intervalo
qtd_fora = ml.quantidade_elementos_fora_de_um_intervalo([10, 20, 30, 40, 50], 20, 40)
print("\nTeste 13 - Quantidade de elementos fora do intervalo [20, 40]:", qtd_fora)
# Esperado: Quantidade de elementos fora do intervalo [20, 40] = 2 (10 e 50)

# Teste 14 - Quantidade de elementos distintos
qtd_distintos = ml.quantidade_elementos_distintos([10, 20, 30, 10, 40, 20])
print("\nTeste 14 - Quantidade de elementos distintos:", qtd_distintos)
# Esperado: Quantidade de elementos distintos = 4 (10, 20, 30, 40)
