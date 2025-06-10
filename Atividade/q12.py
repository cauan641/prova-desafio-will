texto = input("Digite um texto: ")
letras = sum(1 for c in texto if c.isalpha())
print("Quantidade de letras:", letras)
