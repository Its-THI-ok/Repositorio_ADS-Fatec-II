# Biblioteca
import os, time, decimal

# Variáveis
preco = 0.00

# Verifica se o preço está certo
while(preco < 1):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Insira um preço:")
    preco = float(input("R$ "))
    time.sleep(1.5)
    if (preco <= 0):
        print("Insira o preço corretamente")
        time.sleep(3)

# Calcula o Desconto
def desconto(preco, porcentual):
    return preco - preco*(porcentual/100)

# Exibe o resultado
os.system('cls' if os.name == 'nt' else 'clear')
porcentagem = int(input("Insira a porcentagem:\n"))
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
precoNovo = desconto(preco, porcentagem)
print("O valor era de R$ " + "{:.2f}".format(preco),"\nAgora estar por R$ " + "{:.2f}".format(precoNovo))