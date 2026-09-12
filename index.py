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
        Retorno_Menu()

def Varificar_Item_Indice(indice):
    if (indice > -1 and indice <= nomes.__len__()):
        return True
    else:
        return False

def Retorno_Option_Execute(condition):
    """
    Pesquisei o que é callable, achei interessante colocar, pq ele verifica se tal parâmetro é chamável
    Por exemplo, objetos, classes, métodos e propriamente ditas, funções. O que vai ser importante para
    minha abstração.
    """
    if (not callable(condition) or condition == False): return

    entrada = input().upper()
    if (entrada == "S" or entrada == "SIM"):
        condition()
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
                if (Retorno_Option_Execute(False)):
                    print("Insira a nova nota")
                    valor = float(input())
                    if (valor > 0 and valor <= 10):
                        print("Confirme?\nS\\N")
                        # Entrada de nota, confirmação
                        """
                        Antes de dizer que só copiei e colei, pesqusei porquê não pode fazer desta forma:
                            Retorno_Option_Execute(lambda: medias[indice] = valor)
                        Por algum motivo, Python não deixa, recorri a IA para entender o porquê, a mesma disse
                        que a palavra chave lambda não aceita atribuições dentro do corpo, fazendo assim eu
                        falhar tentando atribuir algo, ao invés de criar uma função normalmente (Quebraria
                        o que eu quero fazer), pesquisei qual era o método mais eficiente, e ela me indicou
                        o parâmetro __setitem__, indaguei, ela disse que é a mesma coisa que a atribuição que
                        fiz normalmente, mas ao invés de fazer como uma atribuição, ela faz como um método.
                        A explicação da IA Abaixo:
                            # ====================================================================
                            # NOTA DE DOCUMENTAÇÃO: Por que não usamos 'lambda' comum aqui?
                            # 
                            # Erro original: Retorno_Option_Execute(lambda: medias[indice] = valor)
                            # Motivo: Em Python, lambdas aceitam apenas expressões que retornam valor.
                            # Atribuições com o sinal '=' são 'statements' (instruções) e proibidas em lambdas.
                            #
                            # Solução 1 (Usada): medias.__setitem__(indice, valor)
                            # Explicação: É o método interno do Python para atribuição. Por ser um método, 
                            # funciona dentro da lambda.
                            #
                            # Solução 2 (Alternativa Padrão):
                            # def atualizar(): medias[indice] = valor
                            # Retorno_Option_Execute(atualizar)
                            # ====================================================================

                        """
                        Retorno_Option_Execute(lambda: medias.__setitem__(indice, valor))
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