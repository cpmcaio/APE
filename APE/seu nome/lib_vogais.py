'''
    Nome: lib_vogais
    Descrição: Biblioteca para manipulação de vogais em textos.
    Autores: Valéria Cavalcanti, <seu_nome>
    Data: 27/02/2025
    Versão: 1.0
'''

# Verifica se um determinado símbolo é vogal.
def eh_vogal(simbolo: str) -> bool:
    vogais=["a","e","i","o","u","A","E","I","O","U"]
    if simbolo in vogais:
        return True
    else:
        return False

# Verifica se um texto é formado apenas por vogais.
def eh_texto_vogal(texto: str) -> bool:
    vogais=["a","e","i","o","u","A","E","I","O","U"]
    sovogais=True
    for simbolo in texto:
        if simbolo  not in vogais:
            sovogais=False
    return sovogais


# Retorna a quantidade de vogais em um texto.
def quantidade_vogais(texto: str) -> int:
    vogais=["a","e","i","o","u","A","E","I","O","U"]
    count_vogais=0
    for simbolo in texto:
        if simbolo in vogais:
            count_vogais+=1
    return(count_vogais)        
# Remove as vogais de um texto.
def remove_vogais(texto:str) -> str:
    vogais=["a","e","i","o","u","A","E","I","O","U"]
    texto_modificado=""
    for simbolo in texto:
        if simbolo not in vogais:
            texto_modificado+=simbolo
        
        
    return (texto_modificado)

# Identifica as vogais que estão presentes em um texto.
def identifica_vogais(texto: str) -> list:
    vogais=["a","e","i","o","u","A","E","I","O","U"]
    lista_vogais_texto=[]
    for simbolo in texto:
        if simbolo in vogais:
            lista_vogais_texto.append(simbolo)
    return(lista_vogais_texto)

# Frequêcia de vogais em um texto.
def frequencia_vogais(texto: str) -> list:
    vogais=["a","e","i","o","u"]
    lista_frequencia=[0,0,0,0,0]
    for simbolo in texto:
        if simbolo.lower() in vogais:
            index=vogais.index(simbolo.lower())
            lista_frequencia[index]+=1
    return lista_frequencia

# Substitui as vogais de um texto por * (asterísco).
def substitui_vogais(texto: str) -> str:
    vogais=["a","e","i","o","u","A","E","I","O","U"]
    texto_modificado=""
    for simbolo in texto:
        if simbolo in vogais:
            texto_modificado+="*"
        else:
            texto_modificado+=simbolo
        
    return (texto_modificado)
# Identifica a vogal que mais aparece em um texto. Pode haver mais de uma vogal com a mesma frequência.
def vogal_mais_frequente(texto: str) -> list:
    vogais=["a","e","i","o","u"]
    lista_frequencia=[0,0,0,0,0]

    for simbolo in texto:
        if simbolo.lower() in vogais:
            index=vogais.index(simbolo.lower())
            lista_frequencia[index]+=1

    maior_frequencia=max(lista_frequencia)
    maiores_frequencias=[]

    for  i in range(len(lista_frequencia)):
        if lista_frequencia[i]==maior_frequencia:
            maiores_frequencias.append(vogais[i])
    

    return maiores_frequencias

# Sortear uma vogal.
def sortear_vogal() -> str:
    from random import randint
    vogais=["a","e","i","o","u"]
    numero=randint(0,4)
    return vogais[numero]