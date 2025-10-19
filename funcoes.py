def define_posicoes(linha, coluna, orientacao, tamanho):
    pos_inicial = [linha, coluna]
    opcoes = []
    for i in range(tamanho):
        if orientacao == "vertical": #para pegar a vertical: mesma coluna e linha diferente:
            opcoes.append([linha+i,coluna])
        elif orientacao == "horizontal": # II II II horizontal: coluna diferente e mesma linha:
            opcoes.append([linha,coluna+i])
    return opcoes
