USE BANCO

CREATE TABLE CONTA_CORRENTE(

NOME_CLIENTE VARCHAR(200),
CPF INT,
DATA_NASCIMENTO VARCHAR(10),
SENHA VARCHAR(200),
SALDO float
)




CREATE TABLE CONTA_POUPANCA(

NOME_CLIENTE VARCHAR(200),
CPF INT,
DATA_NASCIMENTO DATE,
SENHA VARCHAR(200),
SALDO float
)

SELECT @@SERVERNAME


INSERT INTO CONTA_CORRENTE (NOME_CLIENTE, CPF, DATA_NASCIMENTO, SENHA, SALDO) VALUES ('MATHEUS', 504, '17/07/1998', '123', 555)

SELECT * FROM CONTA_CORRENTE



