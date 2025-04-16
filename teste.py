
from os import system

def lerMatriz() -> list:
    matriz = []
    linha = int(input("Escreva a quantidade de linhas da matriz: "))
    coluna = int(input("Escreva a quantidade de colunas da matriz: "))

    for i in range(linha):
        matriz.append([])
        for j in range(coluna):
            matriz[i].append(float(input(f"Valor da matriz({i+1}{j+1}): ")))
        system("cls")
    
    return matriz

matrizA = lerMatriz()