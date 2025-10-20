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

def posiciona_frota(dic_frota):
    tab2 = [[0 for _ in range(10)] for _ in range(10)]
    for nav, configuracoes in dic_frota.items():
        for config in configuracoes:
            for pos in config:
                linha, coluna = pos
                tab2[linha][coluna] = 1
    
    return tab2

def afundados(dicionario, tabuleiro):  # dic. recebe info das embarcações, com linha e coluna dos navios
    i = 0  # contagem de navios afundados

    for embarcacoes in dicionario.values():  # percorre as listas dentro do dicionário
        for embarcacao in embarcacoes:       # percorre cada navio individualmente
            afundados = 0                    # conta as partes do navio que foram atingidas

            for linha, coluna in embarcacao:  # verifica as posições no tabuleiro
                if tabuleiro[linha][coluna] == 'X':
                    afundados += 1

            # se o número de partes atingidas for igual ao tamanho do navio, ele afundou
            if afundados == len(embarcacao):
                i += 1
    return i

def posicao_valida (dic_frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    i = 0
    for j,k in posicoes:
        if k<0 or k>9 or j<0 or j>9:
            i+=1
    for embarcacoes in dic_frota.values():
        for embarcacao in embarcacoes:
            for pos in embarcacao:
                if pos in posicoes:
                    i+=1
    if i ==0:
        return True 




            
            

