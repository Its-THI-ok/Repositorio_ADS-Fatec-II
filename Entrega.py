# Thiago Hespanhol Galdino da Silva

# Exercício 1
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

# Exercício 2
peso = float(input("Insira seu peso em kg:\n"))
altura = float(input("Insira a sua altura em centímetros:\n"))

def RetornoMMC(peso, altura):
    resultado = peso/pow(altura, 2)
    if (resultado < 18.5):
        return "Abaixo do Peso"
    elif (resultado >= 18.5 and resultado <= 24.9):
        return "Peso normal"
    elif (resultado > 25 and resultado <= 29,9):
        return "Sobrepeso"
    else:
        return "Obesidade"
    
MMC = RetornoMMC(peso, altura)
print("Sua marca corporal atinge o nível:", MMC)