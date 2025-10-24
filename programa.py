# from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida, monta_tabuleiros

# frota = {
#     "porta-aviões": [],
#     "navio-tanque": [],
#     "contratorpedeiro": [],
#     "submarino": []}

# navios = {
#     "porta-aviões": {"quantidade": 1, "tamanho": 4},
#     "navio-tanque": {"quantidade": 2, "tamanho": 3},
#     "contratorpedeiro": {"quantidade": 3, "tamanho": 2},
#     "submarino": {"quantidade": 4, "tamanho": 1}}

# for nome_navio, info in navios.items():
#     for i in range(info["quantidade"]):
#         linha, coluna = -1, -1
#         orientacao = "horizontal"
#         while not posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
#             print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {info['tamanho']}")
#             linha = int(input("Linha: "))
#             coluna = int(input("Coluna: "))
#             if nome_navio != "submarino":
#                 orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
#                 orientacao = "vertical" if orientacao_input == 1 else "horizontal"
#             else:
#                 orientacao = "horizontal"
#             if not posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
#                 print("Esta posição não está válida!")
#         frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, info["tamanho"])

# frota_oponente = {
#     'porta-aviões': [
#         [[9, 1], [9, 2], [9, 3], [9, 4]]
#     ],
#     'navio-tanque': [
#         [[6, 0], [6, 1], [6, 2]],
#         [[4, 3], [5, 3], [6, 3]]
#     ],
#     'contratorpedeiro': [
#         [[1, 6], [1, 7]],
#         [[0, 5], [1, 5]],
#         [[3, 6], [3, 7]]
#     ],
#     'submarino': [
#         [[2, 7]],
#         [[0, 6]],
#         [[9, 7]],
#         [[7, 6]]
#     ]
# }

# tabuleiro_oponente = posiciona_frota(frota_oponente)
# tabuleiro_jogador = posiciona_frota(frota)

# total_navios_oponente = 0
# for lista in frota_oponente.values():
#     total_navios_oponente += len(lista)

# jogando = True
# while jogando:
#     print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

#     while True:
#         entrada = input("Jogador, qual linha deseja atacar? ")
#         try:
#             linha_input = int(entrada)
#         except:
#             print("Linha inválida!")
#             continue
#         if 0 <= linha_input <= 9:
#             break
#         print("Linha inválida!")

#     while True:
#         entrada = input("Jogador, qual coluna deseja atacar? ")
#         try:
#             coluna_input = int(entrada)
#         except:
#             print("Coluna inválida!")
#             continue
#         if 0 <= coluna_input <= 9:
#             break
#         print("Coluna inválida!")

#     if str(tabuleiro_oponente[linha_input][coluna_input]) in "X-":
#         print(f"A posição linha {linha_input} e coluna {coluna_input} já foi informada anteriormente!")
#         # volta para o passo de perguntar a linha novamente
#     else:
#         tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_input, coluna_input)

#     if afundados(frota_oponente, tabuleiro_oponente) == total_navios_oponente:
#         print("Parabéns! Você derrubou todos os navios do seu oponente!")
#         jogando = False

from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida, monta_tabuleiros

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []}

navios = {
    "porta-aviões": {"quantidade": 1, "tamanho": 4},
    "navio-tanque": {"quantidade": 2, "tamanho": 3},
    "contratorpedeiro": {"quantidade": 3, "tamanho": 2},
    "submarino": {"quantidade": 4, "tamanho": 1}}

for nome_navio, info in navios.items():
    for i in range(info["quantidade"]):
        linha, coluna = -1, -1
        orientacao = "horizontal"
        while not posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
            print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {info['tamanho']}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if nome_navio != "submarino":
                orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "vertical" if orientacao_input == 1 else "horizontal"
            else:
                orientacao = "horizontal"
            if not posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
                print("Esta posição não está válida!")
        frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, info["tamanho"])

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

total_navios_oponente = 0
for lista in frota_oponente.values():
    total_navios_oponente += len(lista)

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    while True:
        entrada = input("Jogador, qual linha deseja atacar? ")
        try:
            linha_input = int(entrada)
        except:
            print("Linha inválida!")
            continue
        if 0 <= linha_input <= 9:
            break
        print("Linha inválida!")

    while True:
        entrada = input("Jogador, qual coluna deseja atacar? ")
        try:
            coluna_input = int(entrada)
        except:
            print("Coluna inválida!")
            continue
        if 0 <= coluna_input <= 9:
            break
        print("Coluna inválida!")

    if str(tabuleiro_oponente[linha_input][coluna_input]) in "X-":
        print(f"A posição linha {linha_input} e coluna {coluna_input} já foi informada anteriormente!")
        continue  # <--- aqui reiniciamos o loop para pedir outra jogada
    else:
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_input, coluna_input)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios_oponente:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
