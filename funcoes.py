# def define_posicoes(linha, coluna, orientacao, tamanho):
#     linha = int(linha)
#     coluna = int(coluna)
#     pos_inicial = [linha, coluna]
#     opcoes = []
#     for i in range(tamanho):
#         if orientacao == "vertical": #para pegar a vertical: mesma coluna e linha diferente:
#             opcoes.append([linha+i,coluna])
#         elif orientacao == "horizontal": # II II II horizontal: coluna diferente e mesma linha:
#             opcoes.append([linha,coluna+i])
#     return opcoes

# def preenche_frota(dic_frota, nome, lin, col, orient, tam):
#     lin = int(lin)
#     col = int(col)
#     posicoes_novo_navio = define_posicoes(lin, col, orient, tam)
#     if nome in dic_frota:
#         dic_frota[nome].append(posicoes_novo_navio)
#     else:
#         dic_frota[nome] = [posicoes_novo_navio]
    
#     return dic_frota

# def faz_jogada (tabuleiro, linha, coluna):
#     if tabuleiro[linha][coluna] == 1:
#         tabuleiro[linha][coluna] = 'X'
#     elif tabuleiro[linha][coluna] == 0:
#         tabuleiro[linha][coluna] = '-'
#     return tabuleiro

# def posiciona_frota(dic_frota):
#     tab2 = [[0 for _ in range(10)] for _ in range(10)]
#     for nav, configuracoes in dic_frota.items():
#         for config in configuracoes:
#             for pos in config:
#                 linha, coluna = pos
#                 tab2[linha][coluna] = 1
    
#     return tab2

# def afundados(dicionario, tabuleiro):  # dic. recebe info das embarcações, com linha e coluna dos navios
#     i = 0  # contagem de navios afundados

#     for embarcacoes in dicionario.values():  # percorre as listas dentro do dicionário
#         for embarcacao in embarcacoes:       # percorre cada navio individualmente
#             afundados = 0                    # conta as partes do navio que foram atingidas

#             for linha, coluna in embarcacao:  # verifica as posições no tabuleiro
#                 if tabuleiro[linha][coluna] == 'X':
#                     afundados += 1

#             # se o número de partes atingidas for igual ao tamanho do navio, ele afundou
#             if afundados == len(embarcacao):
#                 i += 1
#     return i

# # def posicao_valida(dic_frota, linha, coluna, orientacao, tamanho):
# #     linha = int(linha)
# #     coluna = int(coluna)
# #     posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

# #     for j, k in posicoes:
# #         if not (0 <= j <= 9 and 0 <= k <= 9):
# #             return False

# #     for embarcacoes in dic_frota.values():
# #         for embarcacao in embarcacoes:
# #             for pos in embarcacao:
# #                 if pos in posicoes:
# #                     return False

# #     return True

# def posicao_valida(dic_frota, linha, coluna, orientacao, tamanho):
#     linha = int(linha)
#     coluna = int(coluna)
#     if orientacao not in ("vertical", "horizontal"):
#         return False
#     posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
#     for j, k in posicoes:
#         if not (0 <= j <= 9 and 0 <= k <= 9):
#             return False
#     for embarcacoes in dic_frota.values():
#         for embarcacao in embarcacoes:
#             for pos in embarcacao:
#                 if pos in posicoes:
#                     return False
#     return True

# def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
#     texto = ''
#     texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
#     texto += '_______________________________      _______________________________\n'

#     for linha in range(len(tabuleiro_jogador)):
#         jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
#         oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
#         texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
#     return texto






# def define_posicoes(linha, coluna, orientacao, tamanho):
#     posicoes = []
#     if orientacao == "vertical":
#         for i in range(tamanho):
#             posicoes.append([linha + i, coluna])
#     elif orientacao == "horizontal":
#         for i in range(tamanho):
#             posicoes.append([linha, coluna + i])
#     return posicoes

# def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
#     posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
#     if nome_navio not in frota:
#         frota[nome_navio] = []
#     frota[nome_navio].append(posicoes)
#     return frota

# def faz_jogada(tabuleiro, linha, coluna):
#     if tabuleiro[linha][coluna] == 1:
#         tabuleiro[linha][coluna] = "X"
#     else:
#         tabuleiro[linha][coluna] = "-"
#     return tabuleiro

# def posiciona_frota(frota):
#     tabuleiro = []
#     for i in range(10):
#         linha = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#         tabuleiro.append(linha)

#     for nome_navio in frota:
#         for navio in frota[nome_navio]:
#             for posicao in navio:
#                 linha = posicao[0]
#                 coluna = posicao[1]
#                 tabuleiro[linha][coluna] = 1

#     return tabuleiro

# def afundados(frota, tabuleiro):
#     contador = 0
#     for nome_navio in frota:
#         for navio in frota[nome_navio]:
#             afundou = True
#             for posicao in navio:
#                 linha = posicao[0]
#                 coluna = posicao[1]
#                 if tabuleiro[linha][coluna] != "X":
#                     afundou = False
#             if afundou == True:
#                 contador = contador + 1
#     return contador

# def posicao_valida(frota,linha, coluna, orientacao, tam):
#     posicoes= define_posicoes(linha, coluna, orientacao, tam)
#     for line, column in posicoes:
#         if line <0 or line>9 or column<0 or column>9:
#             return False
    
#     for nome in frota:
#         for navio in frota[nome]:
#             for posicao in navio:
#                 if posicao in posicoes:
#                     return False
#     return True

# def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
#     texto = ''
#     texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
#     texto += '_______________________________      _______________________________\n'
#     for linha in range(len(tabuleiro_jogador)):
#         jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
#         oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
#         texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
#     return texto


def define_posicoes (lin,col,ori,siz):
    ret = []
    for i in range(siz):
        ret.append([lin+i,col]) if ori == "vertical" else ret.append([lin,col+i])
    return ret

def preenche_frota (fr,na,lin,col,ori,siz):
    if na not in fr:
        fr[na] = []
    fr[na].append(define_posicoes(lin,col,ori,siz))
    return fr

def faz_jogada (grid,lin,col):
    if grid[lin][col] == 1:
        grid[lin][col] = 'X'
    else:
        grid[lin][col] = '-'
    return grid

def posiciona_frota (fr):
    grid = [
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10,
        [0]*10
    ]
    for val in fr.values():
        for bar in val:
            for pos in bar:
                grid[pos[0]][pos[1]] = 1
    return grid
def afundados(fr, tab):
    afundado = 0
    pos = []
    i = 0
    while i < 10:
        j = 0
        while j < 10:
            if tab[i][j] == 'X':
                pos.append([i, j])
            j += 1
        i += 1
    for val in fr.values():
        for bar in val:
            cont = 0
            for p in bar:
                if p in pos:
                    cont += 1
            if cont == len(bar):
                afundado += 1
    return afundado
def posicao_valida (fr,lin,col,ori,siz):
    posicoes = define_posicoes(lin,col,ori,siz)
    for p in posicoes:
        if p[0] < 0 or p[0] > 9 or p[1] < 0 or p[1] > 9:
            return False
    for val in fr.values():
        for bar in val:
            for p in posicoes:
                if p in bar:
                    return False
    return True
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto