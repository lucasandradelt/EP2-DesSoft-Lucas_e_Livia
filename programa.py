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
for nome, (tamanho, quantidade) in tipos_de_navios.items():
    for i in range(quantidade):
        
        posicao_certa = False #antes de começar o loop, fala que é False 
        while not posicao_certa:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if nome != "submarino":
                orienta = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "vertical" if orienta == 1 else "horizontal"
            else: 
                orientacao = "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao,tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao,tamanho)
                posicao_certa = True # condição de ser True
            else:
                print("Esta posição não está válida!")


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

jogando = True
while jogando:
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        
            return texto

    while True:
            linha = input("Linha: ")
            
            if 0 <= linha <= 9:
                break
            else:
                print("Linha inválida!")

    while True:
            coluna = input("Coluna: ")

            if 0 <= coluna <= 9:
                break
            else:
                print("Coluna inválida!")

    atual = tabuleiro_oponente[linha][coluna]
    if str(atual) in ("X", "0"):
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        continue
    
    faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(tabuleiro_oponente):
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
        jogando = False
        break

    