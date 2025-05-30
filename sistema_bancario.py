from idlelib.mainmenu import menudefs
import datetime
saldo = float(0.00)
extrato = ""
saques_do_dia = 0
limite_de_saque = 10
menu = """
(1)Depositar
(2)Sacar
(3)Extrato
(4)Sair
"""

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        data = datetime.datetime.now()
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f} data: {data} \n"
        print("Valor depositado com sucesso")
    else:
        print("Valor para deposito invalido")

def sacar(valor):
    global saldo, extrato, saques_do_dia, limite_de_saque, data
    if valor <= 0:
        print("Valor invalido para o saque")
        return

    if saques_do_dia < limite_de_saque:
        if valor <= saldo and valor <=500.00:
            data2 = datetime.datetime.now()
            saldo -= valor
            extrato += f"Saque R${valor:.2f} data: {data2} \n"
            saques_do_dia += 1
            print("Saque realizado com sucesso")
        else:
            print("Valor de saque maior do que o saldo atual")
    else:
        print("Limite de saque atingido")

while True:
    opcao = input(menu)
    if opcao == "1":
        depositar_user =(input("Digite o valor para depositar: "))
        depositar(float(depositar_user))
    elif opcao == "2":
        sacar_user =(input("Digite o valor para sacar :  "))
        sacar(float(sacar_user))
    elif opcao == "3":
        print(extrato)
    elif opcao == "4":
        break
    else:
        print("Valor invalido")
