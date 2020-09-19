
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
    senha = input("Digite uma senha a sua escolha:\n")
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


def atualizarDados(cpf):

    att = int(input("O que deseja atualizar?\n1 - CPF\n2 - Data de Nascimento\n3 - Senha\n"))

    operacoes = {
                1: "CPF",
                2: "Data",
                3: "Senha"
                
        }
    tipo_op = operacoes.get(att, "Inválido")

    print(tipo_op)
    if(tipo_op == "CPF"):
        novo_cpf = int(input("Digite seu novo CPF:\n"))
        

        cursor.execute("UPDATE CONTA_CORRENTE SET CPF = " + str(novo_cpf) + "WHERE CPF = " + str(cpf)  )
        
        conn.commit()
        print("CPF ATUALIZADO!")

    if(tipo_op == "Data"):
        novo_data = int(input("Digite sua nova data de nascimento:\n"))
        

        cursor.execute("UPDATE CONTA_CORRENTE SET DATA_NASCIMENTO = " + str(novo_data) + "WHERE CPF = " + str(cpf)  )
        
        conn.commit()
        print("DATA DE NASCIMENTO ATUALIZADA!")
    
    if(tipo_op == "Senha"):
        novo_senha = int(input("Digite sua nova senha:\n"))
        

        cursor.execute("UPDATE CONTA_CORRENTE SET SENHA = " + str(novo_senha) + "WHERE CPF = " + str(cpf)  )
        
        conn.commit()
        print("SENHA ATUALIZADA!")
#flag_login = False
def login():
    try:
        login = int(input("Insira seu cpf cadastrado: \n"))
        senha = input("Insira sua senha: \n")
        flag_login = False
        
        #cursor.execute("SELECT * FROM CONTA_CORRENTE WHERE CPF = " + str(login) + " AND SENHA = " + senha)
        
        cursor.execute("SELECT CASE WHEN COUNT(1) > 0 THEN 1 ELSE 0 END AS 'CPF' FROM CONTA_CORRENTE WHERE CPF = " + str(login) + "AND SENHA = " + senha)
        
        for row in cursor.fetchall():
            a = row
            if 1 in a:
                a = 1
                conn.commit()
                print("Login bem sucedido")
                flag_login = True
                return login
            else:
                b = 1
                print("Login falhou")
                login = False
                return login    
            return a
       
        
        
       
    except:
        print("login falhou")


sair = 0

while (sair != 3):
    inicio = input("Bem vindo ao banco do Teths!\nPressione 1 para logar\nPressione 2 para criar conta\nPressione 3 para encerrar a aplicação\n")


    if(inicio == "1"):
        login = login()

        #print(login)


        operacoes = {
                1: "Depositar",
                2: "Transferir",
                3: "Atualizar Dados",
                4: "Sair"
        }
        op = 0

        if (login != False):
            while (op != 4):
                op = int(input("1 - Depositar\n2 - Transferir\n3 - Atualizar Dados\n4 - Sair")) 
            

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
                if(tipo_op == "Atualizar Dados"):
                    atualizarDados(login)        
                if(tipo_op == 'Sair'):
                    input('Saindo')
                    op = 4
                
    if(inicio == "2"):
        criar_conta()
    if(inicio == "3"):
        sair = 3    
