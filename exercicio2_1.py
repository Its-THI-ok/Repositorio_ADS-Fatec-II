# Bibliotecas
import os, time

# Array de nota
notas = [None, None]
for i in range(0, len(notas)):
    if notas[i] is None:
        # Limpa antes de qualquer coisa
        os.system('cls' if os.name == 'nt' else 'clear')
        # Mensagem
        print("Insira a nota", str(i + 1) + "°")
        nota = float(input())
        # Setando a nota
        notas[i] = nota
        os.system('cls' if os.name == 'nt' else 'clear')

# Conta lógica
media = (notas[0] + notas[1])/len(notas)
# Condicional
if media >= 6:
    print("Você foi aprovado, parabéns!\nMédia: " + str(media))
else:
    print("Que pena, vc foi reprovado\nMédia: " + str(media))