USE ansfinanceiro;

CREATE table operadoras(
Registro_ANS varchar(20) UNIQUE primary key,
CNPJ varchar(20),
Razao_Social varchar(255),
Nome_Fantasia varchar(255),
Modalidade varchar(100),
Logradouro varchar(255),
Numero varchar(50),
Complemento varchar(100),
Bairro varchar(100),
Cidade varchar(100),
UF char(2),
CEP varchar(10),
DDD varchar(3),
Telefone varchar(20),
Fax varchar(20),
Endereco_eletronico varchar(255),
Representante varchar(255),
Cargo_Representante varchar(100),
Regiao_de_Comercializacao text,
Data_Registro_ANS date
);

create table demonstracoes_contabeis (
	id int auto_increment primary key,
	Data_demonstracao date not null,
    Registro_ANS varchar(20) not null,
    CD_CONTA_CONTABIL varchar(10) not null,
    Descricao text,
    VL_SALDO_INICIAL decimal(15, 2) default 0.00,
    VL_SALDO_FINAL decimal(15, 2) default 0.00,
    foreign key (Registro_ANS) references operadoras(Registro_ANS)

);

LOAD DATA  INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS);

SET foreign_key_checks = 0;


LOAD DATA  INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/1T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'  
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Data_demonstracao,Registro_ANS, CD_CONTA_CONTABIL, Descricao, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA  INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/2t2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'  
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Data_demonstracao,Registro_ANS, CD_CONTA_CONTABIL, Descricao, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA  INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/3T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'  
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Data_demonstracao,Registro_ANS, CD_CONTA_CONTABIL, Descricao, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA  INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2023.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'  
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Data_demonstracao,Registro_ANS, CD_CONTA_CONTABIL, Descricao, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA  INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/1T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'  
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Data_demonstracao,Registro_ANS, CD_CONTA_CONTABIL, Descricao, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA  INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/2T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'  
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Data_demonstracao,Registro_ANS, CD_CONTA_CONTABIL, Descricao, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA  INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/3T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'  
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Data_demonstracao,Registro_ANS, CD_CONTA_CONTABIL, Descricao, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA  INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2024.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'  
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Data_demonstracao,Registro_ANS, CD_CONTA_CONTABIL, Descricao, VL_SALDO_INICIAL, VL_SALDO_FINAL);


SELECT 
    o.Razao_Social AS Operadora,
    SUM(d.VL_SALDO_FINAL) AS Total_Despesas
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras o ON d.Registro_ANS = o.Registro_ANS
WHERE 
    d.Descricao = 'Despesas com Eventos/Sinistros não cobertos'
    AND d.Data_demonstracao >= DATE_SUB(CURDATE(), INTERVAL 9 MONTH)
GROUP BY 
    o.Razao_Social
ORDER BY 
    Total_Despesas DESC
LIMIT 10;


SELECT 
    o.Razao_Social AS Operadora,
    SUM(d.VL_SALDO_FINAL) AS Total_Despesas
FROM 
    demonstracoes_contabeis d
JOIN 
    operadoras o ON d.Registro_ANS = o.Registro_ANS
WHERE 
    d.Descricao = 'Despesas com Eventos/Sinistros não cobertos'
    AND d.Data_demonstracao >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY 
    o.Razao_Social
ORDER BY 
    Total_Despesas DESC
LIMIT 10;

SET foreign_key_checks = 1;


