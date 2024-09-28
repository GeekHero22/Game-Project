import random
#LISTAS PARA DEFINIR A VIDA, ATAQUE MINIMO E ATAQUE MÁXIMO DO GUERREIRO E DO MAGO
guerreiro = [60, 7, 14, 6, 12]
mago = [40, 9, 18, 7, 15]
ladino = [30, 8, 20, 7, 15]


#ONDE O JOGO COMEÇA
def jogo():
    print(
        "Seja bem vindo ao PvP magos e guerreiros!")  #MENSAGEM DE BOAS-VINDAS
    print()

    #USUARIO DEFINE A CLASSE DO JOGADOR 1
    print("Escolha sua classe jogador 1!")
    escolha_classe_jogador1 = int(
        input(
            "Digite 1 para ser um Guerreiro, 2 para ser um Mago ou 3 para ser um Ladino:"
        ))
    print()

    #CONDIÇÃO PARA SABER SE JOGADOR1 É GUERREIRO OU MAGO:
    if escolha_classe_jogador1 == 1:
        print("O jogador 1 é um Guerreiro")
        print()
        vida_jogador1 = guerreiro[0]  # acessar indice 0 da lista guerreiro
        ataque_minimo_jogador1 = guerreiro[
            1]  # acessar indice 1 da lista guerreiro
        ataque_maximo_jogador1 = guerreiro[
            2]  # acessar indice 0 da lista guerreiro
        acerto_minimo_jogador1 = guerreiro[
            3]  # acessar indice 0 da lista guerreiro
        acerto_maximo_jogador1 = guerreiro[
            4]  # acessar indice 0 da lista guerreiro

    elif escolha_classe_jogador1 == 2:
        print("O jogador 1 é um Mago")
        print()
        vida_jogador1 = mago[0]  #acessar indice 0 da lista mago
        ataque_minimo_jogador1 = mago[1]  #acessar indice 1 da lista mago
        ataque_maximo_jogador1 = mago[2]  #acessar indice 2 da lista
        acerto_minimo_jogador1 = mago[3]
        acerto_maximo_jogador1 = mago[4]

    elif escolha_classe_jogador1 == 3:
        print("O jogador 1 é um Ladino")
        print()
        vida_jogador1 = ladino[0]  #acessar indice 0 da lista mago
        ataque_minimo_jogador1 = ladino[1]  #acessar indice 1 da lista mago
        ataque_maximo_jogador1 = ladino[2]  #acessar indice 2 da lista
        acerto_minimo_jogador1 = ladino[3]
        acerto_maximo_jogador1 = ladino[4]

#USUARIO DEFINE A CLASSE DO JOGADOR 2
    print("Escolha sua classe jogador 2!")
    escolha_classe_jogador2 = int(
        input(
            "Digite 1 para ser um Guerreiro, 2 para ser um Mago ou 3 para ser um Ladino:"
        ))
    print()

    #CONDIÇÃO PARA SABER SE JOGADOR2 É GUERREIRO OU MAGO:
    if escolha_classe_jogador2 == 1:
        print("O jogador 2 é um Guerreiro")
        print()
        vida_jogador2 = guerreiro[0]
        ataque_minimo_jogador2 = guerreiro[1]
        ataque_maximo_jogador2 = guerreiro[2]
        acerto_minimo_jogador2 = guerreiro[3]
        acerto_maximo_jogador2 = guerreiro[4]

    elif escolha_classe_jogador2 == 2:
        print("O jogador 2 é um Mago")
        print()
        vida_jogador2 = mago[0]
        ataque_minimo_jogador2 = mago[1]
        ataque_maximo_jogador2 = mago[2]
        acerto_minimo_jogador2 = mago[3]
        acerto_maximo_jogador2 = mago[4]

    elif escolha_classe_jogador1 == 3:
        print("O jogador 2 é um ladino")
        print()
        vida_jogador2 = ladino[0]  #acessar indice 0 da lista mago
        ataque_minimo_jogador2 = ladino[1]  #acessar indice 1 da lista mago
        ataque_maximo_jogador2 = ladino[2]  #acessar indice 2 da lista
        acerto_minimo_jogador2 = ladino[3]
        acerto_maximo_jogador2 = ladino[4]

#AQUI COMEÇA A BATALHA
    while vida_jogador1 > 0 and vida_jogador2 > 0:  #Enquanto ninguém tiver a vida zerada, o jogo rola normalmente
        print()
        print(f"Jogador 1 está com {vida_jogador1} de vida")
        print(f"Jogador 2 está com {vida_jogador2} de vida")
        print()

        #TURNO JOGADOR 1
        print()
        print("Vez do jogador 1 atacar!")
        escolha_ataque_jogador1 = int(
            input(
                "Digite 1 para atacar usando ataque minimo ou 2 para atacar usando ataque maximo:"
            ))
        print()

        #SE A ESCOLHA DO JOGADOR1 FOR 1, ELE ATACARÁ USANDO ATAQUE MINIMO

        if escolha_ataque_jogador1 == 1:
            dado = random.randint(1, 20)  #DADO DE 20 LADOS
            print(dado)
            if dado >= acerto_minimo_jogador1:
                ataque_jogador1 = ataque_minimo_jogador1
                vida_jogador2 -= ataque_jogador1
                print(
                    f"O jogador 2 recebeu {ataque_jogador1} de dano e está com {vida_jogador2} de vida"
                )
                print()
            else:
                print("jogador 1 errou o ataque")

    #SE A ESCOLHA DO JOGADOR1 FOR 2, ELE ATACARÁ USANDO ATAQUE MAXIMO
        elif escolha_ataque_jogador1 == 2:
            dado = random.randint(1, 20)  #DADO DE 20 LADOS
            print(dado)
            if dado >= acerto_maximo_jogador1:
                ataque_jogador1 = ataque_maximo_jogador1
                vida_jogador2 -= ataque_jogador1
                print(
                    f"O jogador 2 recebeu {ataque_jogador1} de dano e está com {vida_jogador2} de vida"
                )
                print()
            else:
                print("jogador 1 errou o ataque")

        if vida_jogador2 <= 0:
            print("O jogador 2 foi derrotado!")
            print("Fim de jogo")
            break

    #TURNO JOGADOR 2
        print("Vez do jogador 2 atacar!")
        escolha_ataque_jogador2 = int(
            input(
                "Digite 1 para atacar usando ataque minimo ou 2 para atacar usando ataque maximo: "
            ))

        #SE A ESCOLHA DO JOGADOR2 FOR 1, ELE ATACARÁ USANDO ATAQUE MINIMO
        if escolha_ataque_jogador2 == 1:
            dado = random.randint(1, 20)  #DADO DE 20 LADOS
            print(dado)
            if dado >= acerto_minimo_jogador2:
                ataque_jogador2 = ataque_minimo_jogador2
                vida_jogador1 -= ataque_jogador2
                print(
                    f"O jogador 1 recebeu {ataque_jogador2} de dano e está com {vida_jogador1} de vida"
                )
            else:
                print("jogador 2 errou o ataque")

    #SE A ESCOLHA DO JOGADOR2 FOR 1, ELE ATACARÁ USANDO ATAQUE MINIMO
        elif escolha_ataque_jogador2 == 2:
            dado = random.ranint(1, 20)  #DADO DE 20 LADOS
            print(dado)
            if dado >= acerto_maximo_jogador2:
                ataque_jogador2 = ataque_maximo_jogador2
                vida_jogador1 -= ataque_jogador2
                print(
                    f"O jogador 1 recebeu {ataque_jogador2} de dano e está com {vida_jogador1} de vida"
                )
            else:
                print("jogador 2 errou o ataque")

        if vida_jogador1 <= 0:
            print("O jogador 1 foi derrotado!")
            print("Fim de jogo")
            break


#Para rodar a função jogo()
jogo()
