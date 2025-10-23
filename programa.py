# # # Para o programa usar as funções de funcoes:
# # from funcoes import *
# # # criar o dic da frota 
# # frota = {}
# # tipos_de_navios = {
# #     "porta-aviões": (4, 1),
# #     "navio-tanque": (3, 2),
# #     "contratorpedeiro": (2, 3),
# #     "submarino": (1, 4)
# # }
# # for nome, (tamanho, quantidade) in tipos_de_navios.items():
# #     for i in range(quantidade):
        
# #         posicao_certa = False #antes de começar o loop, fala que é False 
# #         while not posicao_certa:
# #             print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
# #             linha = int(input("Linha: "))
# #             coluna = int(input("Coluna: "))
# #             if nome != "submarino":
# #                 orienta = int(input("[1] Vertical [2] Horizontal >"))
# #                 orientacao = "vertical" if orienta == 1 else "horizontal"
# #             else: 
# #                 orientacao = "horizontal"
# #             if posicao_valida(frota, linha, coluna, orientacao,tamanho):
# #                 frota = preenche_frota(frota, nome, linha, coluna, orientacao,tamanho)
# #                 posicao_certa = True # condição de ser True
# #             else:
# #                 print("Esta posição não está válida!")
# # print(frota)

# # Para o programa usar as funções de funcoes:
# from funcoes import *

# # criar o dic da frota 
# frota = {}
# tipos_de_navios = {
#     "porta-aviões": (4, 1),
#     "navio-tanque": (3, 2),
#     "contratorpedeiro": (2, 3),
#     "submarino": (1, 4)
# }

# def le_int_valido(prompt):
#     """Lê uma entrada do usuário e só retorna um int se a entrada for válida (sem usar try/except)."""
#     while True:
#         s = input(prompt).strip()
#         # aceita apenas números inteiros não-negativos como coordenadas
#         if s.isdigit():
#             return int(s)
#         print("Entrada inválida. Digite um número inteiro entre 0 e 9.")

# for nome, (tamanho, quantidade) in tipos_de_navios.items():
#     for i in range(quantidade):
#         posicao_certa = False
#         while not posicao_certa:
#             print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
#             linha = le_int_valido("Linha: ")
#             coluna = le_int_valido("Coluna: ")

#             # validar intervalo 0-9 aqui (para evitar valores fora do tabuleiro)
#             if not (0 <= linha <= 9 and 0 <= coluna <= 9):
#                 print("Linha ou coluna fora do intervalo válido (0-9). Tente novamente.")
#                 continue

#             # obter orientação
#             if nome != "submarino":
#                 # pede até user escolher 1 ou 2
#                 while True:
#                     orienta_s = input("[1] Vertical [2] Horizontal >").strip()
#                     if orienta_s in ("1", "2"):
#                         orienta = int(orienta_s)
#                         break
#                     print("Opção inválida. Digite 1 para Vertical ou 2 para Horizontal.")
#                 orientacao = "vertical" if orienta == 1 else "horizontal"
#             else:
#                 orientacao = "horizontal"  # submarino tem tamanho 1; orientação não importa, manter 'horizontal'

#             # chama posicao_valida — esta função deve retornar True/False
#             if posicao_valida(frota, linha, coluna, orientacao, tamanho):
#                 # chame preenche_frota; algumas implementações retornam o dicionário atualizado,
#                 # outras apenas modificam em place. Então tratamos os dois casos:
#                 resultado = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
#                 # se a função retornou algo não-None (um dicionário), atualize frota
#                 if resultado is not None:
#                     frota = resultado
#                 posicao_certa = True
#             else:
#                 print("Esta posição não está válida!")

# # Se quiser ver a frota no final:
# print(frota)
from funcoes import *

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
for lista in frota_oponente.values():
    total_navios_oponente += len(lista)
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