# Importando bibliotecas
import os, time

nome = str(input("Insira seu nome:\n"))

# função de testagem
def testador(nome):
    passou = False
    for i in nome:
        if i.isdigit():
            passou = True
        else:
            passou = False
    return passou

# Definindo condicional
testagem = testador(nome)
# executando condicional
while(testagem):
    # Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Diga o seu nome, não números:")
    # Define um tempo
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = str(input("Insira seu nome:\n"))
    testagem = testador(nome)

# Limpa o terminal de novo para imprimir a mensagem
os.system('cls' if os.name == 'nt' else 'clear')
print("Olá,",nome + "!")