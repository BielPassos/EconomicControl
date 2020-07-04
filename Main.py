from MenusMatriz import *
from  Logica import *

def main():
    cont = 0
    armazena = open("Banco.txt", 'r')
    ler = armazena.readlines()

    matriz = []
    verifica = True
    if str(ler) == '[]' or str(ler) == '':
        criaMatriz(matriz)
    else:
        matriz = eval(ler[0])
    armazena = open("Banco.txt", "r")

    months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
              "Novembro", "Dezembro"]
    weeks = [1, 2, 3, 4]
    Menu()
    printaMatriz(str(ler))

    while verifica:

        comando = int(input("\nInsira o comando desejado >> "))

        if comando == 0:
            resposta = True
            while resposta:
                mes = int(input("Qual mês desejado?(0 = Janeiro, 1 = Fevereiro, 2 = Março,...) >>"))
                semana = int(input(
                    "Qual semana desejada?(Primeira Semana = 0, Segunda Semana = 1, Terceira Semana = 2 e Quarta Semana = 3) >>"))
                valor = float(input("Qual valor desejado? >>"))
                print("\nMês escolhido >>", months[mes])
                print(weeks[semana], "ª semana")
                adicionaValorMes(matriz, mes, semana, valor)

                ler = str(matriz)
                print(ler)

                armazena = open("Banco.txt", "w")
                armazena.write(str(ler))

                saida = input("Deseja adicionar mais algum valor a algum mês? S/N >>")
                if saida == 'n':
                    adiciona('Banco.txt', ler, saida)

                if saida == "N" or saida == "n":
                    resposta = False
                    print("*************************************")

        elif comando == 1:
            print(str(matriz))
            print("*************************************")


        elif comando == 2:
            resposta = True
            while resposta:
                mes = int(
                    input("Qual mês desejado para fazer a visualização?(0 = Janeiro, 1 = Fevereiro, 2 = Março,...) >>"))
                print("Mês >>", months[mes])
                print(matriz[mes])
                saida = input("Deseja visualizar mais algum mês? S/N >>")
                if saida == "N" or saida == "n":
                    resposta = False
                    print("*************************************")


        elif comando == 3:
            resposta = True
            while resposta:
                mes = int(input("Qual mês desejado para fazer a soma?(0 = Janeiro, 1 = Fevereiro, 2 = Março,...) >>"))
                print("Soma", months[mes], ">> R$", somaMes(matriz, mes))
                saida = input("Deseja visualizar mais alguma soma de algum mês? S/N >>")
                if saida == "N" or saida == "n":
                    resposta = False
                    print("*************************************")

        elif comando == 4:
            print(matriz)
            print("Soma Total >> R$", somaGeral(matriz))
            print("*************************************")

        else:
            print("Comando inválido.")

        Menu2()

        var = input("Deseja Continuar com algo?S/N >>")
        if var == "N" or var == "n":
            verifica = False
            print("Até mais, tenha um bom dia!")


main()
