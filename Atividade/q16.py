soma = 0
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    if n % 5 == 0:
        soma += n
print("Soma dos múltiplos de 5:", soma)
