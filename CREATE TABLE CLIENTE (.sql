CREATE TABLE CLIENTE (
        idcliente int NOT NULL,
        nome char (90) NOT NULL,
    datadenascimento DATE NOT NULL,
    cpf char (12) NOT NULL,
    email char (50) NOT NULL,
    telefone char(12) NULL,
    PRIMARY KEY (idcliente));
CREATE TABLE CURSO(
    idcurso INT NOT NULL,
    nome char (90) NOT NULL,
    cargahoraria INT NOT NULL,
    descriçao char (120) NULL,
    PRIMARY KEY(idcurso)
);
CREATE TABLE idcurso(
    idcurso int NOT NULL,
    idcliente int NOT NULL,
    datainscriçao DATE NOT NULL,
    datacancelamento DATE NULL,
    PRIMARY KEY (idcurso,idcliente ),
    FOREIGN KEY (idcliente ) REFERENCES cliente (idcliente),
    FOREIGN KEY (idcurso ) REFERENCES curso (idcurso));

