def criaMatriz(matriz):
  for i in range(12):
    lista = []
    for i in range(4):
      lista.append(0)
    matriz.append(lista)

def Menu():
  apresenta = '''
  -----Bem vindo ao app Economic Control-----
  Comandos:
  * Insira 0 para inserir um valor em um determinado mês.
  * Insira 1 para visualização de todos mêses.
  * Insira 2 para visualização de um determinado mês.
  * Insira 3 para visualização da soma de um determinado mês.
  * Insira 4 para visualização da soma de todos os valores inseridos.
  '''
  print(apresenta)

def Menu2():
  apresenta = '''
  Comandos:
  * Insira 0 para inserir um valor em um determinado mês.
  * Insira 1 para visualização de todos mêses.
  * Insira 2 para visualização de um determinado mês.
  * Insira 3 para visualização da soma de um determinado mês.
  * Insira 4 para visualização da soma de todos os valores inseridos.
  '''
  print(apresenta)
