x=input("igor, digite a brincadeira: ")

qtd_upper=0
qtd_lower=0
qtd_digit=0
for i in range(len(x)):
    if  (x[i].isdigit()) == True:
        qtd_digit+=1
    if  (x[i].islower()) == True:
        qtd_lower+=1
    if  (x[i].isupper()) == True:
        qtd_upper+=1

print("qtd upper", qtd_upper)
print("qtd digit", qtd_digit)
print("qtd lower", qtd_lower)
