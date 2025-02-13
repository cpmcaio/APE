Qa= int(input("Quantidade de aprovados: "))
Qr= int(input("Quantidade de reprovados: "))

Qtotal= (Qa+Qr)
Qap= (Qa*100)/Qtotal

print("Porcentagem de alunos aprovados: {}%".format(int(Qap)))
