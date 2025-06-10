frase = input("Digite uma frase: ").lower()
vogais = sum(1 for letra in frase if letra in "aeiou")
print("Quantidade de vogais:", vogais)
