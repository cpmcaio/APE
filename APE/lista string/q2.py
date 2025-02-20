x = input("Igor, digite uma palavra: ")

for i in range(len(x)):
    char = x[i]
    print("Decimal:",char, ord(char),"Binário:",char, bin(ord(char)), "Hexadecimal:",char, hex(ord(char)),"Octal:",char, oct(ord(char)),(len(x)))


