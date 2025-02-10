
qtd_de_aulas=int(input("quantidade de aulas na matéria "))
qtd_de_faltas=int(input("quantidade de faltas na matéria "))

qtd_assistidas=(qtd_de_aulas-qtd_de_faltas)

freq = (qtd_assistidas/qtd_de_aulas)*100

print ("Frequência: {}%".format(int(freq)))
