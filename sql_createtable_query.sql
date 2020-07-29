CREATE TABLE agendamento(id_agendamento INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    id_pedido INT, 
    horario_agendado DATETIME, 
    tempo_estimado TIME);

CREATE TABLE pedido(id_pedido INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    id_produto INT, 
    quantidade INT,
    id_comanda INT, 
    id_restaurante INT);

CREATE TABLE produto(id_produto INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(40), preco FLOAT);

CREATE TABLE restaurante(id_restaurante INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    endereco VARCHAR(100));

CREATE TABLE cliente(id_cliente INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    usuario VARCHAR(10) NOT NULL UNIQUE,
    nome VARCHAR(30),
    endereco VARCHAR(100), 
    hash VARCHAR(110),
    ip_pacote INT);

CREATE TABLE desafio(id_desafio INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    id_cliente INT, dia_completo DATETIME);

CREATE TABLE pontos(id_pontos INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    id_cliente INT, 
    pontos_acumulados INT);

CREATE TABLE pacote_promocional(id_pacote INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    id_cliente INT, 
    valor INT);

CREATE TABLE comanda(id_comanda INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
    id_cliente INT, 
    valor FLOAT,
    completo BOOL);



INSERT INTO produto(name, preco) VALUES('Frango Fusilli Queijo de Cabra', 32.90)
INSERT INTO produto(name, preco) VALUES('Burrata Presunto Cru', 39.90)
INSERT INTO produto(name, preco) VALUES('Couscous Cogu Gordo', 27.90)
INSERT INTO produto(name, preco) VALUES('Salmao Edamame', 37.90)
INSERT INTO produto(name, preco) VALUES('Tofu e Quinos', 39.90)
INSERT INTO produto(name, preco) VALUES('Frango e Parmesao', 24.90)
INSERT INTO produto(name, preco) VALUES('Frango Avocado', 31.90)

INSERT INTO cliente(name, endereco, hash, id_pacote) VALUES('Cesar Wen', 'Rua Verbo Divino 1061', '')