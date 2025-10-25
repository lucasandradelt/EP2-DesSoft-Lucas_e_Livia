# # from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida, monta_tabuleiros

# # frota = {
# #     "porta-aviões": [],
# #     "navio-tanque": [],
# #     "contratorpedeiro": [],
# #     "submarino": []}

# # navios = {
# #     "porta-aviões": {"quantidade": 1, "tamanho": 4},
# #     "navio-tanque": {"quantidade": 2, "tamanho": 3},
# #     "contratorpedeiro": {"quantidade": 3, "tamanho": 2},
# #     "submarino": {"quantidade": 4, "tamanho": 1}}

# # for nome_navio, info in navios.items():
# #     for i in range(info["quantidade"]):
# #         linha, coluna = -1, -1
# #         orientacao = "horizontal"
# #         while not posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
# #             print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {info['tamanho']}")
# #             linha = int(input("Linha: "))
# #             coluna = int(input("Coluna: "))
# #             if nome_navio != "submarino":
# #                 orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
# #                 orientacao = "vertical" if orientacao_input == 1 else "horizontal"
# #             else:
# #                 orientacao = "horizontal"
# #             if not posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
# #                 print("Esta posição não está válida!")
# #         frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, info["tamanho"])

# # frota_oponente = {
# #     'porta-aviões': [
# #         [[9, 1], [9, 2], [9, 3], [9, 4]]
# #     ],
# #     'navio-tanque': [
# #         [[6, 0], [6, 1], [6, 2]],
# #         [[4, 3], [5, 3], [6, 3]]
# #     ],
# #     'contratorpedeiro': [
# #         [[1, 6], [1, 7]],
# #         [[0, 5], [1, 5]],
# #         [[3, 6], [3, 7]]
# #     ],
# #     'submarino': [
# #         [[2, 7]],
# #         [[0, 6]],
# #         [[9, 7]],
# #         [[7, 6]]
# #     ]
# # }

# # tabuleiro_oponente = posiciona_frota(frota_oponente)
# # tabuleiro_jogador = posiciona_frota(frota)

# # total_navios_oponente = 0
# # for lista in frota_oponente.values():
# #     total_navios_oponente += len(lista)

# # jogando = True
# # while jogando:
# #     print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

# #     while True:
# #         entrada = input("Jogador, qual linha deseja atacar? ")
# #         try:
# #             linha_input = int(entrada)
# #         except:
# #             print("Linha inválida!")
# #             continue
# #         if 0 <= linha_input <= 9:
# #             break
# #         print("Linha inválida!")

# #     while True:
# #         entrada = input("Jogador, qual coluna deseja atacar? ")
# #         try:
# #             coluna_input = int(entrada)
# #         except:
# #             print("Coluna inválida!")
# #             continue
# #         if 0 <= coluna_input <= 9:
# #             break
# #         print("Coluna inválida!")

# #     if str(tabuleiro_oponente[linha_input][coluna_input]) in "X-":
# #         print(f"A posição linha {linha_input} e coluna {coluna_input} já foi informada anteriormente!")
# #         # volta para o passo de perguntar a linha novamente
# #     else:
# #         tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_input, coluna_input)

# #     if afundados(frota_oponente, tabuleiro_oponente) == total_navios_oponente:
# #         print("Parabéns! Você derrubou todos os navios do seu oponente!")
# #         jogando = False

# from funcoes import *

# frota = {
#     "porta-aviões": [],
#     "navio-tanque": [],
#     "contratorpedeiro": [],
#     "submarino": []
#     }

# navios = {
#     "porta-aviões": {"quantidade": 1, "tamanho": 4},
#     "navio-tanque": {"quantidade": 2, "tamanho": 3},
#     "contratorpedeiro": {"quantidade": 3, "tamanho": 2},
#     "submarino": {"quantidade": 4, "tamanho": 1}
#     }

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
# mostra_tabuleiro = True
# jogando = True
# while jogando:
#     if mostra_tabuleiro:
#         print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
#     monta_tabuleiro = True
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
#         monta_tabuleiro = False
#         continue  # <--- aqui reiniciamos o loop para pedir outra jogada
#     else:
#         tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_input, coluna_input)

#     if afundados(frota_oponente, tabuleiro_oponente) == total_navios_oponente:
#         print("Parabéns! Você derrubou todos os navios do seu oponente!")
#         jogando = False





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
#         while True:
#             print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {info['tamanho']}")
            
#             # --- Validação de Linha ---
#             while True:
#                 try:
#                     linha = int(input("Linha: "))
#                     if 0 <= linha <= 9:
#                         break
#                     print("Linha inválida!")
#                 except ValueError:
#                     print("Linha inválida!")
                    
#             # --- Validação de Coluna ---
#             while True:
#                 try:
#                     coluna = int(input("Coluna: "))
#                     if 0 <= coluna <= 9:
#                         break
#                     print("Coluna inválida!")
#                 except ValueError:
#                     print("Coluna inválida!")

#             # --- Definição de Orientação ---
#             if nome_navio != "submarino":
#                 while True:
#                     try:
#                         orientacao_input = int(input("[1] Vertical [2] Horizontal >"))
#                         if orientacao_input in [1, 2]:
#                             orientacao = "vertical" if orientacao_input == 1 else "horizontal"
#                             break
#                         print("Opção inválida.")
#                     except ValueError:
#                         print("Opção inválida.")
#             else:
#                 orientacao = "horizontal"

#             # --- Validação Final da Posição ---
#             if posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
#                 frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, info["tamanho"])
#                 break  # Sai do loop while True para ir para o próximo navio
#             else:
#                 print("Esta posição não está válida!")
#                 # Se for inválido, o loop while True recomeça
            

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

#     # --- Loop para garantir um ataque válido e inédito ---
#     while True:
#         # Pede e valida a Linha
#         while True:
#             entrada_linha = input("Jogador, qual linha deseja atacar? ")
#             try:
#                 linha_input = int(entrada_linha)
#                 if 0 <= linha_input <= 9:
#                     break
#                 print("Linha inválida!")
#             except ValueError:
#                 print("Linha inválida!")

#         # Pede e valida a Coluna
#         while True:
#             entrada_coluna = input("Jogador, qual coluna deseja atacar? ")
#             try:
#                 coluna_input = int(entrada_coluna)
#                 if 0 <= coluna_input <= 9:
#                     break
#                 print("Coluna inválida!")
#             except ValueError:
#                 print("Coluna inválida!")

#         # Verifica se a posição já foi atacada
#         if str(tabuleiro_oponente[linha_input][coluna_input]) in "X-":
#             print(f"A posição linha {linha_input} e coluna {coluna_input} já foi informada anteriormente!")
#             continue  # Volta ao início do loop 'while True' para pedir novas coordenadas
#         else:
#             break  # Posição válida e inédita, sai do loop de ataque
            
#     # Executa a jogada apenas após confirmar que a posição é inédita
#     tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_input, coluna_input)

#     # Verifica a condição de vitória
#     # A função afundados deve retornar o número de navios afundados
#     if afundados(frota_oponente, tabuleiro_oponente) == total_navios_oponente:
#         print("Parabéns! Você derrubou todos os navios do seu oponente!")
#         jogando = False






from funcoes import *
import random
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
        orientacao = ""
        while not posicao_valida(frota, linha, coluna, orientacao, info["tamanho"]):
            print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {info['tamanho']}")
            while True:
                linha = int(input("Linha: "))
                if 0 <= linha <= 9:
                    break
                print("Linha inválida!")
            while True:
                coluna = int(input("Coluna: "))
                if 0 <= coluna <= 9:
                    break
                print("Coluna inválida!")
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
total_navios = 0
for lista in frota_oponente.values():
    total_navios_oponente += len(lista)
for lista in frota.values():
    total_navios += len(lista)

montar = True

jogando = True
while jogando:
    if montar:
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    montar = True
    while True:
        lin = int(input("Jogador, qual linha deseja atacar? "))
        if 0 <= lin <= 9:
            break
        print("Linha inválida!")

    while True:
        col = int(input("Jogador, qual coluna deseja atacar? "))
        if 0 <= col <= 9:
            break
        print("Coluna inválida!")

    if str(tabuleiro_oponente[lin][col]) in "X-":
        print(f"A posição linha {lin} e coluna {col} já foi informada anteriormente!")
        montar = False
    else:
        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, lin, col)
    if afundados(frota_oponente, tabuleiro_oponente) == total_navios_oponente:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
        continue
    while True:
            lin_oponente = random.randint(0, 9)
            col_oponente = random.randint(0, 9)
            if str(tabuleiro_jogador[lin_oponente][col_oponente]) not in "X-":
                print(f"Seu oponente está atacando na linha {lin_oponente} e coluna {col_oponente}")
                tabuleiro_jogador = faz_jogada(tabuleiro_jogador, lin_oponente, col_oponente)
                break
    if afundados(frota, tabuleiro_jogador) == total_navios:
        print("Xi! O oponente derrubou toda a sua frota =(")
        jogando = False