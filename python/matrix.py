# calculadora automatica de matrix (sem numpy pq sim)
# caiu, nao mexe no meu codego. se quiser fazer em python, faça outro arquivo

# Primeiro: entrada de operacao (soma, subtracao e multiplicacao)
# depois add determinante, trasnposto, cofator, adjunto e inverso

# depois da entrada; funcao para ler ordem e valores das matrizes
# soma/subtracao: matrizes de mesma ordem. forma nova matriz que valor de c(ij) = a(ij) +- b(ij)

# multiplicacao: coluna da primeira matriz igual linha da segunda matriz. 
# forma nova matriz de qtd de linha da primeira matriz e qtd coluna da segunda matriz

from os import system

def lerMatriz() -> list:
    matriz = []
    linha = int(input("Escreva a quantidade de linhas da matriz: "))
    coluna = int(input("Escreva a quantidade de colunas da matriz: "))

    system("cls")

    for i in range(linha):
        matriz.append([])
        for j in range(coluna):
            matriz[i].append(float(input(f"Valor da matriz({i+1}{j+1}): ")))
        system("cls")
    
    return matriz

while True:
    operacao = input('''Escolha sua operação:
1. Soma (+)
2. Subtracao (-)
3. Multiplicacao (*)
0. Sair (s)
''').lower()
    
    if operacao in ["1", "2", "3", "+", "-", "*", "soma", "subtracao", "multiplicacao"]:
        matrizA = lerMatriz()
        matrizB = lerMatriz()
        matrizC = []

        if operacao in ["soma", "+", "1"]:
            if len(matrizA) == len(matrizB):
                for i in range(len(matrizA)):
                    matrizC.append([])
                    for j in range(len(matrizA[i])):
                        matrizC[i].append(matrizA[i][j] + matrizB[i][j])

                print(matrizC)
                quit()
            else:
                print("A ordem das matrizes tem que ser igual. Tente novamente")

        elif operacao in ["subtração", "subtracao", "sub", "-", "2"]:
            if len(matrizA) == len(matrizB):
                for i in range(len(matrizA)):
                    matrizC.append([])
                    for j in range(len(matrizA[i])):
                        matrizC[i].append(matrizA[i][j] - matrizB[i][j])

                print(matrizC)
                quit()
            else:
                print("A ordem das matrizes tem que ser igual. Tente novamente")

        elif operacao in ["multiplicação", "multiplicacao", "multi", "3", "*"]:
            pass

    elif operacao in ["s", "0"]:
        print("Saindo...")
        quit()

    else:
        print("Entrada invalida, tente novamente.")

