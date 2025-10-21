# Para o programa usar as funções de funcoes:
from funcoes import *
# criar o dic da frota 
frota = {}
tipos_de_navios = { 
    "porta-aviões": (4,1),
    "navio-tanque": (3,2),
    "contratorpedeiro": (2,3),
    "contratorpedeiro": (1,4)
}
for nome, (tamanho, quantidade) in tipos_de_navios.items():
    for i in range(quantidade):
        print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
        posicao_valida = False #antes de começar o loop, fala que é False 
        while posicao_valida == False:
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if nome != "submarino":
                orienta = int(input("[1] Vertical [2] Horizontal >"))
                orientacao = "horizontal" if orienta == 1 else "horizontal"
            else: 
                orientacao = "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao,tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao,tamanho)
                posicao_valida = True # condição de ser True
            else:
                print("Esta posição não está válida!")
print("Esta posição não está válida!")