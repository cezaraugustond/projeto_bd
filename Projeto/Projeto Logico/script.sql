-- -----------------------------------------------------
-- Table Federacao
-- -----------------------------------------------------
DROP TABLE IF EXISTS Federacao CASCADE;

CREATE TABLE Federacao (
  id_federecao INT NOT NULL,
  nome VARCHAR(100) NOT NULL,
  sigla VARCHAR(10) NOT NULL,
  estado CHAR(2) NOT NULL,
  cnpj VARCHAR(18) NOT NULL,
  site VARCHAR(100),
  PRIMARY KEY (id_federecao),
  CONSTRAINT cnpj_unique UNIQUE (cnpj)
);

-- -----------------------------------------------------
-- Table Estadio
-- -----------------------------------------------------
DROP TABLE IF EXISTS Estadio CASCADE;

CREATE TABLE Estadio (
  id_estadio INT NOT NULL,
  nome VARCHAR(100) NOT NULL,
  capacidade INT NOT NULL CHECK (capacidade > 0),
  cidade VARCHAR(45) NOT NULL,
  estado CHAR(2) NOT NULL,
  PRIMARY KEY (id_estadio)
);

-- -----------------------------------------------------
-- Table Clube
-- -----------------------------------------------------
DROP TABLE IF EXISTS Clube CASCADE;

CREATE TABLE Clube (
  id_clube INT NOT NULL,
  nome VARCHAR(45) NOT NULL,
  cnpj VARCHAR(18) NOT NULL,
  cidade VARCHAR(45) NOT NULL,
  estado CHAR(2) NOT NULL,
  data_filiacao DATE NOT NULL DEFAULT CURRENT_DATE,
  id_federecao INT NOT NULL,
  id_estadio INT NOT NULL,
  PRIMARY KEY (id_clube),
  CONSTRAINT cnpj_clube_unique UNIQUE (cnpj),
  CONSTRAINT fk_clube_federacao 
    FOREIGN KEY (id_federecao) REFERENCES Federacao (id_federecao)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_clube_estadio 
    FOREIGN KEY (id_estadio) REFERENCES Estadio (id_estadio)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table Campeonato
-- -----------------------------------------------------
DROP TABLE IF EXISTS Campeonato CASCADE;

CREATE TABLE Campeonato (
  id_campeonato INT NOT NULL,
  nome VARCHAR(45) NOT NULL,
  tipo VARCHAR(45) NOT NULL CHECK (tipo IN ('Nacional', 'Estadual', 'Copa')),
  id_federecao INT NOT NULL,
  PRIMARY KEY (id_campeonato),
  CONSTRAINT fk_campeonato_federacao 
    FOREIGN KEY (id_federecao) REFERENCES Federacao (id_federecao)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table Temporada
-- -----------------------------------------------------
DROP TABLE IF EXISTS Temporada CASCADE;

CREATE TABLE Temporada (
  id_temporada INT NOT NULL,
  ano INT NOT NULL CHECK (ano > 1900),
  formato VARCHAR(45) NOT NULL,
  id_campeonato INT NOT NULL,
  id_clube_campeao INT,
  PRIMARY KEY (id_temporada),
  CONSTRAINT fk_temporada_campeonato 
    FOREIGN KEY (id_campeonato) REFERENCES Campeonato (id_campeonato)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_temporada_clube 
    FOREIGN KEY (id_clube_campeao) REFERENCES Clube (id_clube)
    ON DELETE SET NULL ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table Jogador
-- -----------------------------------------------------
DROP TABLE IF EXISTS Jogador CASCADE;

CREATE TABLE Jogador (
  id_jogador INT NOT NULL,
  licenca INT NOT NULL,
  posicao VARCHAR(45) NOT NULL,
  altura INT NOT NULL, -- em cm
  peso INT NOT NULL,   -- em kg
  primeiro_nome VARCHAR(45) NOT NULL,
  sobrenome VARCHAR(45) NOT NULL,
  data_nascimento DATE NOT NULL,
  cpf VARCHAR(11) NOT NULL UNIQUE,
  telefones TEXT, 
  id_federecao INT NOT NULL,
  PRIMARY KEY (id_jogador),
  CONSTRAINT licenca_jogador_unique UNIQUE (licenca),
  CONSTRAINT fk_jogador_federacao 
    FOREIGN KEY (id_federecao) REFERENCES Federacao (id_federecao)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table Tecnico
-- -----------------------------------------------------
DROP TABLE IF EXISTS Tecnico CASCADE;

CREATE TABLE Tecnico (
  id_tecnico INT NOT NULL,
  licenca INT NOT NULL UNIQUE,
  especialidade VARCHAR(45),
  primeiro_nome VARCHAR(45) NOT NULL,
  sobrenome VARCHAR(45) NOT NULL,
  data_nascimento DATE NOT NULL,
  cpf VARCHAR(11) NOT NULL UNIQUE,
  id_federecao INT NOT NULL,
  PRIMARY KEY (id_tecnico),
  CONSTRAINT fk_tecnico_federacao 
    FOREIGN KEY (id_federecao) REFERENCES Federacao (id_federecao)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table Partida
-- -----------------------------------------------------
DROP TABLE IF EXISTS Partida CASCADE;

CREATE TABLE Partida (
  id_partida INT NOT NULL,
  data_hora TIMESTAMP NOT NULL,
  placar_mandante INT NOT NULL DEFAULT 0,
  placar_visitante INT NOT NULL DEFAULT 0,
  publico_total INT DEFAULT 0,
  id_clube_mandate INT NOT NULL,
  id_clube_visitante INT NOT NULL,
  id_estadio INT NOT NULL,
  id_temporada INT NOT NULL,
  PRIMARY KEY (id_partida),
  CONSTRAINT fk_partida_mandante FOREIGN KEY (id_clube_mandate) REFERENCES Clube (id_clube),
  CONSTRAINT fk_partida_visitante FOREIGN KEY (id_clube_visitante) REFERENCES Clube (id_clube),
  CONSTRAINT fk_partida_estadio FOREIGN KEY (id_estadio) REFERENCES Estadio (id_estadio),
  CONSTRAINT fk_partida_temporada FOREIGN KEY (id_temporada) REFERENCES Temporada (id_temporada)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table Sumula (Entidade Fraca)
-- -----------------------------------------------------
DROP TABLE IF EXISTS Sumula CASCADE;

CREATE TABLE Sumula (
  id_partida INT NOT NULL,
  hora_inicio TIME NOT NULL,
  hora_fim TIME NOT NULL,
  PRIMARY KEY (id_partida),
  CONSTRAINT fk_sumula_partida 
    FOREIGN KEY (id_partida) REFERENCES Partida (id_partida)
    ON DELETE CASCADE ON UPDATE CASCADE
);

-- -----------------------------------------------------
-- Table Evento
-- -----------------------------------------------------
DROP TABLE IF EXISTS Evento CASCADE;

CREATE TABLE Evento (
  id_evento INT NOT NULL,
  descricao TEXT,
  minuto_ocorrido INT NOT NULL,
  tipo_evento VARCHAR(20) CHECK (tipo_evento IN ('Gol', 'Cartao Amarelo', 'Cartao Vermelho')),
  sumula_id_partida INT NOT NULL,
  id_jogador INT NOT NULL,
  PRIMARY KEY (id_evento, sumula_id_partida),
  CONSTRAINT fk_evento_sumula 
    FOREIGN KEY (sumula_id_partida) REFERENCES Sumula (id_partida)
    ON DELETE CASCADE,
  CONSTRAINT fk_evento_jogador 
    FOREIGN KEY (id_jogador) REFERENCES Jogador (id_jogador)
    ON DELETE CASCADE
);

-- -----------------------------------------------------
-- Table Executivo
-- -----------------------------------------------------
DROP TABLE IF EXISTS Executivo CASCADE;

CREATE TABLE Executivo (
  id_executivo INT NOT NULL,
  licenca INT NOT NULL UNIQUE,
  cargo VARCHAR(45),
  primeiro_nome VARCHAR(45) NOT NULL,
  sobrenome VARCHAR(45) NOT NULL,
  cpf VARCHAR(11) NOT NULL UNIQUE,
  id_federecao INT,
  id_clube INT,
  PRIMARY KEY (id_executivo),
  -- Regra de Exclusividade: Ou clube ou federação
  CONSTRAINT check_exclusividade CHECK (
    (id_federecao IS NOT NULL AND id_clube IS NULL) OR 
    (id_federecao IS NULL AND id_clube IS NOT NULL)
  ),
  CONSTRAINT fk_executivo_fed FOREIGN KEY (id_federecao) REFERENCES Federacao (id_federecao),
  CONSTRAINT fk_executivo_clube FOREIGN KEY (id_clube) REFERENCES Clube (id_clube)
);