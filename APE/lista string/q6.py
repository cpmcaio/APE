st=input()
texto_em_minúsculo=st.lower()

contador=0
for letra in "python":
    contador+=texto_em_minúsculo.count(letra)

print(st)
print(contador)

