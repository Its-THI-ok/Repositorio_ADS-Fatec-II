# Dados
nomes = [ "Ana", "Claudia", "Diego", "Diogo", "Elizia", "Fabricio", "Gabriella", "Marcelo", "Marcelly", "Tássia" ]
medias = [ 8.5, 6.0, 4.5, 6.5, 9.5, 5.5, 8.0, 4.0, 9.0, 2.5]

def Show_Names():
    for i, nome in enumerate(nomes):
        print("\nID:", i, "\nAluno:\n", nome,"\nMédia:",medias[i],)

def Menu():
    print("Escolhas as opções abaixo\n[A] Alterar\n[E] Excluir\n[M] Mostrar Nomes\n[S] Sair")
    entrada = input().upper()
    # Condicional enorme
    if (entrada != None and not entrada.isdigit() and entrada in ["A", "E", "M", "S"]):
        return entrada
    else:
        print("Insira um valor válido")

def Check_Index(indice):
    if (indice > -1 and indice < len(nomes)):
        return indice
    else:
        return None

def Option_Execute(condition=None, textoNeg=None):
    """
    Pesquisei o que é callable, achei interessante colocar, pq ele verifica se tal parâmetro é chamável
    Por exemplo, objetos, classes, métodos e propriamente ditas, funções. O que vai ser importante para
    minha abstração.
    """

    input_msg = input().upper()
    if ((input_msg == "S" or input_msg == "SIM") and callable(condition)):
        condition()
        return True
    elif (input_msg == "S" or input_msg == "SIM"):
        return True
    else:
        print(textoNeg)
        return False

def Insert_Nota(target=-1):
    if (target == None or not target not in range(0, len(nomes))): return print("Valor fora de índice")
    # Carregando Dado
    print(nomes[target], medias[target])
    print(f"\nDeseja alterar registro de {nomes[target]}?\nS\\N")

    status = Option_Execute(None, "Saindo")
    if not status: return

    valor = float(input("Insira a nova nota:\n"))

    if (valor >= 0 and valor <= 10):
        print("Confirme?\nS\\N")
        Option_Execute(lambda: medias.__setitem__(target, valor), "Cancelado")
    else:
        print("Insira uma nota corretamente")

def Remove_Data(target=-1):
    if (target == None or target not in range(0, len(nomes))): return print("Valor fora de índice")
    # Carregando Dado
    print(nomes[target], medias[target])
    print(f"\nDeseja remover {nomes[target]} do registro?\nS\\N")

    status = Option_Execute(None, "Cancelando")
    if not status: return
    nomes.pop(target)
    medias.pop(target)

while True:
    match Menu():
        case "A":
            target = int(input("Insira o ID:\n"))
            Insert_Nota(Check_Index(target))

        case "E":
            target = int(input("Insira o ID:\n"))
            Remove_Data(Check_Index(target))

        case "M":
            Show_Names()

        case "S":
            print("Saindo")
            break
        case _:
            None