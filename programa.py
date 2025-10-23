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
# for nome, (tamanho, quantidade) in tipos_de_navios.items():
#     for i in range(quantidade):
        
#         posicao_certa = False #antes de começar o loop, fala que é False 
#         while not posicao_certa:
#             print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
#             linha = int(input("Linha: "))
#             coluna = int(input("Coluna: "))
#             if nome != "submarino":
#                 orienta = int(input("[1] Vertical [2] Horizontal >"))
#                 orientacao = "vertical" if orienta == 1 else "horizontal"
#             else: 
#                 orientacao = "horizontal"
#             if posicao_valida(frota, linha, coluna, orientacao,tamanho):
#                 frota = preenche_frota(frota, nome, linha, coluna, orientacao,tamanho)
#                 posicao_certa = True # condição de ser True
#             else:
#                 print("Esta posição não está válida!")
# print(frota)

# Para o programa usar as funções de funcoes:
from funcoes import *

# criar o dic da frota 
frota = {}
tipos_de_navios = {
    "porta-aviões": (4, 1),
    "navio-tanque": (3, 2),
    "contratorpedeiro": (2, 3),
    "submarino": (1, 4)
}

def le_int_valido(prompt):
    """Lê uma entrada do usuário e só retorna um int se a entrada for válida (sem usar try/except)."""
    while True:
        s = input(prompt).strip()
        # aceita apenas números inteiros não-negativos como coordenadas
        if s.isdigit():
            return int(s)
        print("Entrada inválida. Digite um número inteiro entre 0 e 9.")

for nome, (tamanho, quantidade) in tipos_de_navios.items():
    for i in range(quantidade):
        posicao_certa = False
        while not posicao_certa:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = le_int_valido("Linha: ")
            coluna = le_int_valido("Coluna: ")

            # validar intervalo 0-9 aqui (para evitar valores fora do tabuleiro)
            if not (0 <= linha <= 9 and 0 <= coluna <= 9):
                print("Linha ou coluna fora do intervalo válido (0-9). Tente novamente.")
                continue

            # obter orientação
            if nome != "submarino":
                # pede até user escolher 1 ou 2
                while True:
                    orienta_s = input("[1] Vertical [2] Horizontal >").strip()
                    if orienta_s in ("1", "2"):
                        orienta = int(orienta_s)
                        break
                    print("Opção inválida. Digite 1 para Vertical ou 2 para Horizontal.")
                orientacao = "vertical" if orienta == 1 else "horizontal"
            else:
                orientacao = "horizontal"  # submarino tem tamanho 1; orientação não importa, manter 'horizontal'

            # chama posicao_valida — esta função deve retornar True/False
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                # chame preenche_frota; algumas implementações retornam o dicionário atualizado,
                # outras apenas modificam em place. Então tratamos os dois casos:
                resultado = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                # se a função retornou algo não-None (um dicionário), atualize frota
                if resultado is not None:
                    frota = resultado
                posicao_certa = True
            else:
                print("Esta posição não está válida!")

# Se quiser ver a frota no final:
print(frota)