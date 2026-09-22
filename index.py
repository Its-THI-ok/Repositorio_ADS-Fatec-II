# Dados
nomes = [ "Ana", "Claudia", "Diego", "Diogo", "Elizia", "Fabricio", "Gabriella", "Marcelo", "Marcelly", "Tássia" ]
medias = [ 8.5, 6.0, 4.5, 6.5, 9.5, 5.5, 8.0, 4.0, 9.0, 2.5]

def Menu():
    entrada = input("Escolhas as opções abaixo\n[A] Alterar\n[E] Excluir\n[M] Mostrar Nomes\n[S] Sair\n").upper()
    if (entrada not in ["A", "E", "M", "S"]):
        print("Insira um valor válido")
    else:
        return entrada

def Check_Index(indice):
    if (indice in range(0, len(nomes))):
        return indice
    else:
        return -1

def Option_Execute(condition=None, textoNeg=None):
    """
    Pesquisei o que é callable, achei interessante colocar, pq ele verifica se tal parâmetro é chamável
    Por exemplo, objetos, classes, métodos e propriamente ditas, funções. O que vai ser importante para
    minha abstração.
    """
    input_msg = input().upper()
    if ((input_msg == "S" or input_msg == "SIM") and callable(condition)): condition(); return True
    elif (input_msg == "S" or input_msg == "SIM"): return True
    else: print(textoNeg); return False

def Insert_Nota(target=-1):
    if (not Check_Index(target) >= 0): return print("Valor fora de índice")
    # Carregando Dado
    if not Option_Execute(print(f"{nomes[target]}, {medias[target]}\nDeseja alterar registro de {nomes[target]}?\nS\\N"), "Saindo"): return
    valor = float(input("Insira a nova nota:\n"))
    if (valor > 0 or valor < 10):
        print("Confirme?\nS\\N")
        Option_Execute(lambda: medias.__setitem__(target, valor), "Cancelado")
    else:
        print("Insira uma nota corretamente")

def Remove_Data(target=-1):
    if (not Check_Index(target) >= 0): return print("Valor fora de índice")
    # Carregando Dado
    if not Option_Execute(print(f"{nomes[target]}, {medias[target]}\nDeseja remover {nomes[target]} do registro?\nS\\N"), "Cancelando"): return
    nomes.pop(target)
    medias.pop(target)

while True:
    match Menu():
        case "A":
            Insert_Nota(Check_Index(int(input("Insira o ID:\n"))))
        case "E":
            Remove_Data(Check_Index(int(input("Insira o ID:\n"))))
        case "M":
            for i, nome in enumerate(nomes):
                print("\nID:", i, "\nAluno:\n", nome,"\nMédia:",medias[i],)
        case "S":
            print("Saindo")
            break
        case _:
            None
