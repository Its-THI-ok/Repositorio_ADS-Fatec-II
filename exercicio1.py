numero = None
while (True):
    numero = int(input("Digite um número positivo:\n"))
    if (numero >= 0):
        if (numero % 2 == 0):
            print("É par")
            break
        else:
            print("É Ímpar")
            break
