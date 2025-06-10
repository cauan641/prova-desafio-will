numeros = [int(input(f"Número {i+1}: ")) for i in range(10)]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
print("Pares:", pares)
print("Ímpares:", impares)
