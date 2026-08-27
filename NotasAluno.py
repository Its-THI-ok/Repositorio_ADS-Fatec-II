notas = [None, None]
counter = 0

for i in notas:
    # O i está como 
    i = float(input("Insira a nota:\n"))
    while(i < 0 or i > 10):
        print("Nota inválida, coloque uma nota correta")
        i = float(input("Insira a nota:\n"))
    notas[counter] = round(i, 1)
    counter += 1

# Cálculo
media = round((notas[0] + notas[1])/2, 1)
# Condicional
if (media >= 6):
    print("Parabéns, você foi aprovado!")
elif (media < 6 and media > 4):
    print("Irá precisar realizar a prova substituta. Boa sorte!")
    print("Irá precisar de:", (12 - max(notas[0], notas[1])))
else:
    print("Infelizmente você foi reprovado, esperamos que consiga na próxima")
