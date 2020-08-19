import datetime
import pickle
import random
import pyodbc
#Classes


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-KMKBJBR;'
                      'Database=BANCO;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()                      




class Conta():
    def __init__(self, nome, nascimento, cpf, saldo, tipo_conta, senha):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.saldo = saldo 
        self.tipo_conta = tipo_conta
        self.senha = senha

class Conta_Corrente(Conta):
    def __init__(self, nome, nascimento, cpf, saldo, tipo_conta, senha):
        super().__init__(nome = nome, nascimento = nascimento, cpf = cpf, saldo = saldo, tipo_conta = tipo_conta, senha = senha)



class Conta_Poupança(Conta):
    def __init__(self, nome, nascimento, cpf, saldo, tipo_conta, senha):
        super().__init__(nome = nome, nascimento = nascimento, cpf = cpf, saldo = saldo, tipo_conta = tipo_conta, senha = senha)


#Funções


def criar_conta():
    nome = input("Digite seu nome:\n")
    nascimento = str(input("Digite sua data de nascimento: \n"))
    cpf = int(input("Digite seu CPF:\n"))
    saldo = 0
    s1 = random.randint(0,99)
    s2 = random.randint(100,300)
    senha = s1+s2
    #lista_cc = []
    #lista_p = []
    tipos_conta = {
        1: "Conta Corrente",
        2: "Conta Poupança"
    }

    conta_escolha = int(input("1 - Conta Corrente\n2 - Conta Poupança\n")) 

    tipo_conta = tipos_conta.get(conta_escolha, "Inválido")

    if(tipo_conta == "Conta Corrente"):
        cc = Conta_Corrente(nome, nascimento, cpf, saldo, tipo_conta,senha)
        
        
        #gravar_conta(cc)
        print("Nome: " + cc.nome + "\nData de Nascimento: " + cc.nascimento + "\nCPF: " + str(cc.cpf) + "\nTipo de Conta: " + cc.tipo_conta + "\nSenha: " + str(cc.senha))
        
        
        print(cc.nascimento)
        try:
            cursor.execute("INSERT INTO BANCO.dbo.CONTA_CORRENTE (NOME_CLIENTE, CPF, DATA_NASCIMENTO, SENHA, SALDO) VALUES (" + "'" + cc.nome + "'" + "," + str(cc.cpf) + "," +"'" + cc.nascimento +"'" + "," + str(cc.senha) + "," + str(cc.saldo) + ")")
            conn.commit()
            #check = True
            print("Conta Criada!")

        except:
            print("CPF já cadastrado!")

         
           


    if(tipo_conta == 2):
        pass



    
 

def depositar(conta):
    """
    get_saldo = conta.saldo
    novo_saldo = float(input("Digite o quanto deseja depositar:\n"))
    conta.saldo = conta.saldo + novo_saldo
    
    

    print("Novo saldo: " + str(conta.saldo))
    """
    login = conta
    saldo_depositar = float(input("O quanto deseja depositar?\n"))
    cursor.execute("UPDATE CONTA_CORRENTE SET SALDO = SALDO +" + str(saldo_depositar)+ " WHERE CPF = " + str(login))
    conn.commit()



def transferir(conta):
    
    login = conta
    transferir_cpf = input("Insira o CPF da pessoa que você deseja transferir:\n")
    transferir_saldo = float(input("O quanto deseja transferir?\n"))
    try:
        cursor.execute("UPDATE CONTA_CORRENTE SET SALDO = SALDO +" + str(transferir_saldo)+ " WHERE CPF = " + str(transferir_cpf) + "\nUPDATE CONTA_CORRENTE SET SALDO = SALDO -" + str(transferir_saldo)+ " WHERE CPF = " + str(login)  )
        conn.commit()
    except:
        print("Erro na transferência! Saldo insuficiente.")



def login():
    try:
        login = int(input("Insira seu cpf cadastrado: \n"))
        senha = input("Insira sua senha: \n")
        flag_login = False
    
        cursor.execute("SELECT * FROM CONTA_CORRENTE WHERE CPF = " + str(login) + " AND SENHA = " + senha)
        
        conn.commit()
        print("Login bem sucedido")
        flag_login = True
        return login
    except:
        print("login falhou")




input("Bem vindo ao banco do Teths!\nPressione Enter para continuar a tela de Login!")



login = login()

print(login)


operacoes = {
        1: "Depositar",
        2: "Transferir",
        3: "Sair"
    }
op = 0

if (login != None):
    while (op != 3):
        op = int(input("1 - Depositar\n2 - Transferir\n3 - Sair\n")) 
    

        tipo_op = operacoes.get(op, "Inválido")

        dep = 0
        tra = 0

        if(tipo_op == 'Depositar'):
            while (dep == 0):
                depositar(login)
                dep = 1
        if(tipo_op == 'Transferir'):
            while (tra == 0):
                transferir(login)
                tra = 1
        if(tipo_op == 'Sair'):
            input('Saindo')
            op = 3
        