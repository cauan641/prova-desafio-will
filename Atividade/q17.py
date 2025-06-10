def par_ou_impar(n):
    return "Par" if n % 2 == 0 else "Ímpar"
n = int(input("Digite um número: "))
print(par_ou_impar(n))
