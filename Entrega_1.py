#Nome: Thiago Hespanhol Galdino da Silva

#Atividade 1

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
    print("Diga o seu nome, não números:")
    nome = str(input("Insira seu nome:\n"))
    testagem = testador(nome)

# Limpa o terminal de novo para imprimir a mensagem
print("Olá,",nome + "!")

#Atividade 2

nota1 = None
nota2 = None
if nota1 is None:
        print("Insira a nota 1°")
        nota1 = int(input())
if nota2 is None:
        print("Insira a nota 2°")
        nota2 = int(input())

# Conta lógica
media = (nota1 + nota2)/2
# Condicional
if media >= 6:
    print("Você foi aprovado, parabéns!\nMédia: " + str(media))
else:
    print("Que pena, vc foi reprovado\nMédia: " + str(media))

# Atividade 3

# Variáveis
preco = 0.00

# Verifica se o preço está certo
while(preco < 1):
    print("Insira um preço:")
    preco = float(input("R$ "))
    if (preco <= 0):
        print("Insira o preço corretamente")

# Calcula o Desconto
def desconto(preco, porcentual):
    return preco - preco*(porcentual/100)

# Exibe o resultado
precoNovo = desconto(preco, 10)
print("O valor era de R$ " + "{:.2f}".format(preco),"\nAgora estar por R$ " + "{:.2f}".format(precoNovo))