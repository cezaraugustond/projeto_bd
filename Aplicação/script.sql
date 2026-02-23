CREATE SCHEMA IF NOT EXISTS aplicacao_crud;
SET search_path TO aplicacao_crud;

-- -----------------------------------------------------
-- Tabela Jogador
-- -----------------------------------------------------
DROP TABLE IF EXISTS Jogador CASCADE;

CREATE TABLE Jogador (
  id_jogador SERIAL PRIMARY KEY,
  primeiro_nome VARCHAR(45) NOT NULL,
  sobrenome VARCHAR(70) NOT NULL,
  data_nascimento DATE NOT NULL,
  cpf CHAR(11) NOT NULL UNIQUE,
  licenca CHAR(11) NOT NULL UNIQUE,
  posicao CHAR(3) NOT NULL,
  altura INT NOT NULL,
  peso DECIMAL(5,2) NOT NULL,
  telefones VARCHAR(11)[]
);
-- -----------------------------------------------------
-- Tabela Clube 
-- -----------------------------------------------------
DROP TABLE IF EXISTS Clube CASCADE;

CREATE TABLE Clube (
  id_clube SERIAL PRIMARY KEY,
  nome VARCHAR(70) NOT NULL,
  cnpj CHAR(14) NOT NULL UNIQUE,
  cidade VARCHAR(50) NOT NULL,
  estado CHAR(2) NOT NULL,
  data_filiacao DATE NOT NULL DEFAULT CURRENT_DATE
);

-- -----------------------------------------------------
-- Tabela Contrato
-- -----------------------------------------------------
DROP TABLE IF EXISTS Contrato CASCADE;

CREATE TABLE Contrato (
  id_contrato SERIAL PRIMARY KEY,
  data_inicio DATE NOT NULL DEFAULT CURRENT_DATE,
  data_fim DATE NOT NULL,
  salario_mensal DECIMAL(12,2),
  multa_rescisoria DECIMAL(12,2),
  id_jogador INT NOT NULL,
  id_clube INT NOT NULL,
  CONSTRAINT fk_contrato_jogador 
    FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador)
    ON DELETE CASCADE,
  CONSTRAINT fk_contrato_clube 
    FOREIGN KEY (id_clube) REFERENCES Clube (id_clube)
    ON DELETE CASCADE
);
