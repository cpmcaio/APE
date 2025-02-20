xantes=input("igor, digite o codigo alfa numerico: ")
xepois=""
for i in range(len(xantes)):
    if xantes[i].isdigit()== True:
        xepois+="*"
    else:
        xepois+=xantes[i]

print("x antes das modificações: ", xantes)
print("x depois: ", xepois)
