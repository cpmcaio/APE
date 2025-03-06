# Gerar uma lista de tamanho n com valores aleatórios.
import random
from typing import Counter


def gerar_lista(quantidade: int, menor_valor: int, maior_valor: int) -> list:
    lista = []
    for i in range(quantidade):
        lista.append(random.randint(menor_valor, maior_valor))
    return lista


# Exibir os elementos da lista, um por linha.
def exibir_lista(lista: list):
    for i in range(len(lista)):
        print(i)
    pass

# Calcular a média dos valores da lista.
def calcular_media(lista: list) -> float:
    soma = sum(lista)
    media = soma / len(lista)
    return media

# Elementos com valores acima da média
def elementos_acima_da_media(lista: list) -> list:
    media = calcular_media(lista) 
    elementos_acima = []  
    for i in lista:
        if i > media:
            elementos_acima.append(i)
    
    return elementos_acima

# Elementos com valores abaixo da média.
def elementos_abaixo_da_media(lista: list) -> list:
    media = calcular_media(lista) 
    elementos_abaixo = []  
    for i in lista:
        if i < media:
            elementos_abaixo.append(i)
    return elementos_abaixo
    
    pass

# Elementos com valores entre (inclusive) dois valores informados.
def elementos_entre_dois_valores(lista: list, valor1: int, valor2: int) -> list:
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1
    
    elementos_entre = []  # Lista para armazenar os elementos que estão no intervalo
    
    # Itera sobre os elementos da lista
    for i in lista:
        if valor1 <= i <= valor2:  # Verifica se o elemento está entre valor1 e valor2 (inclusive)
            elementos_entre.append(i)
    
    return elementos_entre

    pass

# Elementos com valores fora de um intervalo informado.
def elementos_fora_de_um_intervalo(lista: list, valor1: int, valor2: int) -> list:
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1
    elementos_fora = []
    for i in lista:
        if i < valor1 or i > valor2: 
            elementos_fora.append(i)
    
    return elementos_fora

# Elementos distintos da lista.
def elementos_distintos(lista: list) -> list:
    elementos_distintos=[]
    for i in range(len(lista)):
        if  lista[i] not in elementos_distintos:
            elementos_distintos.append(lista[i])

    return elementos_distintos
    pass

# Elemento mais frequente. Pode haver repetição.
def elemento_mais_frequente(lista: list) -> list:
    elementos_mais_frequentes=[]
    frequencia=0
    for i in range (len(lista)):
        if lista.count(lista[i])>frequencia:
            frequencia = lista.count(lista[i])
    for i in range (len(lista)):
        if lista.count(lista[i]) == frequencia:
            elementos_mais_frequentes.append(lista[i])
    return elementos_mais_frequentes
    pass

# Calcular a quantidade de elementos com valores acima da média.
def quantidade_elementos_acima_da_media(lista: list) -> int:
    media = calcular_media(lista) 
    elementos_acima = []  
    for i in lista:
        if i > media:
            elementos_acima.append(i)
    
    return len(elementos_acima)
    pass

# Calcular a quantidade de elementos com valores abaixo da média.
def quantidade_elementos_abaixo_da_media(lista: list) -> int:
    media = calcular_media(lista) 
    elementos_abaixo = []  
    for i in lista:
        if i < media:
            elementos_abaixo.append(i)
        return len(elementos_abaixo)
    pass

# Calcular a quantidade de elementos com valores entre (inclusive) dois valores informados.
def quantidade_elementos_entre_dois_valores(lista: list, valor1: int, valor2: int) -> int:
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1
    
    elementos_entre = []  # Lista para armazenar os elementos que estão no intervalo
    
    # Itera sobre os elementos da lista
    for i in lista:
        if valor1 <= i <= valor2:  # Verifica se o elemento está entre valor1 e valor2 (inclusive)
            elementos_entre.append(i)
    
    return len(elementos_entre)

    pass

# Calcular a quantidade de elementos com valores fora de um intervalo informado.
def quantidade_elementos_fora_de_um_intervalo(lista: list, valor1: int, valor2: int) -> int:
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1
    elementos_fora = []
    for i in lista:
        if i < valor1 or i > valor2: 
            elementos_fora.append(i)
    
    return len(elementos_fora)
    pass

# Calcular a quantidade de elementos distintos da lista
def quantidade_elementos_distintos(lista: list) -> int:
    elementos_distintos=[]
    for i in range(len(lista)):
        if  lista[i] not in elementos_distintos:
            elementos_distintos.append(lista[i])

    return len(elementos_distintos)
    pass