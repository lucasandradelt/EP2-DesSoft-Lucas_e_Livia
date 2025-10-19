def define_posicoes(linha, coluna, orientacao, tamanho):
    pos_inicial = [linha, coluna]
    opcoes = []
    for i in range(tamanho):
        if orientacao == "vertical": #para pegar a vertical: mesma coluna e linha diferente:
            opcoes.append([linha+i,coluna])
        elif orientacao == "horizontal": # II II II horizontal: coluna diferente e mesma linha:
            opcoes.append([linha,coluna+i])
    return opcoes

def preenche_frota(dic_frota, nome, lin, col, orient, tam):
    
    posicoes_novo_navio = define_posicoes(lin, col, orient, tam)
    if nome in dic_frota:
        dic_frota[nome].append(posicoes_novo_navio)
    else:
        dic_frota[nome] = [posicoes_novo_navio]
    
    return dic_frota

def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
    
    
