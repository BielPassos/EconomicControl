def adicionaValorMes(matriz,mes,semana,valor):
  matriz[mes][semana] = valor

def somaMes(matriz,mes):
  soma = 0
  for x in matriz[mes]:
    soma += x

  return soma

def somaGeral(matriz):
  somaTudo = 0
  for i in range(len(matriz)):
   for j in range(len(matriz[i])):
    somaTudo += matriz[i][j]
  return somaTudo


def adiciona(arquivo, leitura, saida):
    valor = open(arquivo, 'w')
    valor.write(str(leitura))
    valor.close()


def printaMatriz(matriz):
    vermelho = ['\033[31m', '\033[m']
    azul = ['\033[34m', '\033[m']

    matriz2 = matriz
    cont = 0
    # print(matriz2[0], matriz2[1])

    for x in range(len(matriz2)):
        if x > 2 and matriz2[x] != matriz2[-1] and matriz2[x] != matriz2[-2]:
            if matriz[x] != ',':
                if matriz[x] == '[' and x > 2 and matriz[x + 1] != '[':
                    cont += 1
                    print(f'{vermelho[0]}Mês{vermelho[1]} {cont}: {azul[0]}', end='')
                if matriz2[x] != '[':
                    print(matriz2[x], end='')

            elif matriz2[x] == ',' and matriz[x - 1] == ']':
                print(f'\n', end='')
            else:
                print(f',', end='')
