# Dados
nomes = [ "Ana", "Claudia", "Diego", "Diogo", "Elizia", "Fabricio", "Gabriella", "Marcelo", "Marcelly", "Tássia" ]
medias = [ 8.5, 6.0, 4.5, 6.5, 9.5, 5.5, 8.0, 4.0, 9.0, 2.5]

def Exibir_Alunos():
    for nome in nomes:
        i = nomes.index(nome)
        print("\nID:", i, "\nAluno:\n", nome,"\nMédia:",medias[i],)

def Retorno_Menu():
    print("Escolhas as opções abaixo")
    print("[A] Alterar\n[E] Excluir\n[M] Mostrar Nomes\n[S] Sair")
    entrada = input().upper()
    # Condicional enorme
    if (entrada != None and not entrada.isdigit() and entrada != "A" or entrada != "E" or entrada != "S"):
        return entrada
    else:
        print("Insira um valor válido")
        Retorno_Menu

def Varificar_Item_Indice(indice):
    if (indice > -1 and indice <= nomes.__len__()):
        return True
    else:
        return False

def Retorno_Option():
    entrada = input().upper()
    if (entrada == "S"):
        return True
    else:
        return False

while True:
    match Retorno_Menu():
        case "A":
            print("Insira o ID:")
            indice = int(input())
            if (Varificar_Item_Indice(indice)):
                print(nomes[indice], medias[indice])
                print("\nDeseja alterar o registro?\nS\\N")
                # Entrada de entrada do índice, confirmação
                if (Retorno_Option()):
                    print("Insira a nova nota")
                    valor = float(input())
                    if (valor > 0 and valor <= 10):
                        print("Confirme?\nS\\N")
                        # Entrada de nota, confirmação
                        if (Retorno_Option()):
                            medias[indice] = valor
                        else:
                            Retorno_Menu()
                    else:
                        print("Insira uma nota corretamente")
                        Retorno_Menu()
                else:
                    Retorno_Menu()
            else:
                print("Insira um índice válido")
                Retorno_Menu()

        case "E":
            print("E")

        case "M":
            Exibir_Alunos()

        case "S":
            print("Saindo")
            break
        case _:
            Retorno_Menu()