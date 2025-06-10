print("1-Soma 2-Subtração 3-Multiplicação 4-Divisão")
op = int(input("Escolha a operação: "))
x = float(input("Número 1: "))
y = float(input("Número 2: "))
if op == 1:
    print("Resultado:", x + y)
elif op == 2:
    print("Resultado:", x - y)
elif op == 3:
    print("Resultado:", x * y)
elif op == 4:
    print("Resultado:", x / y if y != 0 else "Erro: divisão por zero")
else:
    print("Opção inválida.")