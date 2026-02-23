import psycopg

dados_conexao = ""

try:
    with psycopg.connect(dados_conexao) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            versao = cur.fetchone()
            print(f"Conectado com sucesso ao {versao[0]}")

            cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'aplicacao_crud';")
            esquema = cur.fetchone()

            if esquema:
                print("Esquema 'aplicacao_crud' encontrado!")
            else:
                print("AVISO: DB conectado, mas não foi encontrado o esquema 'aplicacao_crud'.")
except Exception as e:
    print(f"ERRO DE CONEXÃO: {e}")

def salvar_jogador(dados):
    try:
        with psycopg.connect(dados_conexao) as conn:
            with conn.cursor() as cur:
                cur.execute("SET search_path TO aplicacao_crud;")
            
                sql = """
                INSERT INTO Jogador (primeiro_nome, sobrenome, data_nascimento, cpf, licenca, posicao, altura, peso, telefones)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_jogador;
                """
                cur.execute(sql, dados)
                id_gerado = cur.fetchone()[0]
                return id_gerado
    except Exception as e:
        print(f"ERRO AO SALVAR JOGADOR: {e}")
        return None

def salvar_clube(dados):
    try:
        with psycopg.connect(dados_conexao) as conn:
            with conn.cursor() as cur:
                cur.execute("SET search_path TO aplicacao_crud;")
                sql = "INSERT INTO Clube (nome, cnpj, cidade, estado) VALUES (%s, %s, %s, %s) RETURNING id_clube;"
                cur.execute(sql, dados)
                return cur.fetchone()[0]
    except Exception as e:
        print(f"ERRO AO SALVAR CLUBE: {e}")
        return None

def salvar_contrato(dados):
    try:
        with psycopg.connect(dados_conexao) as conn:
            with conn.cursor() as cur:
                cur.execute("SET search_path TO aplicacao_crud;")
                sql = """
                INSERT INTO Contrato (id_clube, id_jogador, data_fim, salario, multa)
                VALUES (%s, %s, %s, %s, %s) RETURNING id_contrato;
                """
                cur.execute(sql, dados)
                return cur.fetchone()[0]
    except Exception as e:
        print(f"ERRO AO SALVAR CONTRATO: {e}")
        return None

def buscar_jogadores_db(nome=None, id_jogador=None):
    try:
        with psycopg.connect(dados_conexao) as conn:
            with conn.cursor() as cur:
                cur.execute("SET search_path TO aplicacao_crud;")
                
                if id_jogador:
                    cur.execute("SELECT * FROM Jogador WHERE id_jogador = %s;", (id_jogador,))
                elif nome:
                    cur.execute("SELECT * FROM Jogador WHERE primeiro_nome ILIKE %s OR sobrenome ILIKE %s;", (f"%{nome}%", f"%{nome}%"))
                else:
                    cur.execute("SELECT * FROM Jogador ORDER BY id_jogador;")
                
                return cur.fetchall()
    except Exception as e:
        print(f"ERRO NA BUSCA DE JOGADOR: {e}")
        return []

def buscar_clubes_db(nome=None, id_clube=None):
    try:
        with psycopg.connect(dados_conexao) as conn:
            with conn.cursor() as cur:
                cur.execute("SET search_path TO aplicacao_crud;")
                
                if id_clube:
                    cur.execute("SELECT * FROM Clube WHERE id_clube = %s;", (id_clube,))
                elif nome:
                    cur.execute("SELECT * FROM Clube WHERE nome ILIKE %s;", (f"%{nome}%",))
                else:
                    cur.execute("SELECT * FROM Clube ORDER BY id_clube;")
                
                return cur.fetchall()
    except Exception as e:
        print(f"ERRO NA BUSCA DE CLUBE: {e}")
        return []

def buscar_contratos_db(id_contrato=None, id_jogador=None):
    try:
        with psycopg.connect(dados_conexao) as conn:
            with conn.cursor() as cur:
                cur.execute("SET search_path TO aplicacao_crud;")
                
                sql = """
                SELECT co.id_contrato, cl.nome, jo.primeiro_nome, co.data_fim, co.salario
                FROM Contrato co
                JOIN Clube cl ON co.id_clube = cl.id_clube
                JOIN Jogador jo ON co.id_jogador = jo.id_jogador
                """
                
                if id_contrato:
                    cur.execute(sql + " WHERE co.id_contrato = %s;", (id_contrato,))
                elif id_jogador:
                    cur.execute(sql + " WHERE co.id_jogador = %s;", (id_jogador,))
                else:
                    cur.execute(sql + " ORDER BY co.id_contrato;")
                
                return cur.fetchall()
    except Exception as e:
        print(f"ERRO AO BUSCAR CONTRATO: {e}")
        return []

def remover_jogador_db(id_jogador):
    try:
        with psycopg.connect(dados_conexao) as conn:
            with conn.cursor() as cur:
                cur.execute("SET search_path TO aplicacao_crud;")
                cur.execute("DELETE FROM Jogador WHERE id_jogador = %s;", (id_jogador,))
                if cur.rowcount > 0:
                    return True
                return False
    except Exception as e:
        print(f"ERRO AO REMOVER JOGADOR: {e}")
        return False

def remover_clube_db(id_clube):
    try:
        with psycopg.connect(dados_conexao) as conn:
            with conn.cursor() as cur:
                cur.execute("SET search_path TO aplicacao_crud;")
                cur.execute("DELETE FROM Clube WHERE id_clube = %s;", (id_clube,))
                return cur.rowcount > 0
    except Exception as e:
        print(f"ERRO AO REMOVER CLUBE: {e}")
        return False

def remover_contrato_db(id_contrato):
    try:
        with psycopg.connect(dados_conexao) as conn:
            with conn.cursor() as cur:
                cur.execute("SET search_path TO aplicacao_crud;")
                cur.execute("DELETE FROM Contrato WHERE id_contrato = %s;", (id_contrato,))
                return cur.rowcount > 0
    except Exception as e:
        print(f"ERRO AO REMOVER CONTRATO: {e}")
        return False

def atualizar_jogador_db(id_jogador, novos_dados):
    try:
        with psycopg.connect(dados_conexao) as conn:
            with conn.cursor() as cur:
                cur.execute("SET search_path TO aplicacao_crud;")
                sql = """
                UPDATE Jogador 
                SET primeiro_nome = %s, sobrenome = %s, cpf = %s, posicao = %s, altura = %s, peso = %s
                WHERE id_jogador = %s;
                """
                cur.execute(sql, novos_dados + (id_jogador,))
                return cur.rowcount > 0
    except Exception as e:
        print(f"ERRO AO ATUALIZAR JOGADOR: {e}")
        return False

def atualizar_clube_db(id_clube, novos_dados):
    try:
        with psycopg.connect(dados_conexao) as conn:
            with conn.cursor() as cur:
                cur.execute("SET search_path TO aplicacao_crud;")
                sql = """
                UPDATE Clube SET nome = %s, cnpj = %s, cidade = %s, estado = %s
                WHERE id_clube = %s;
                """
                cur.execute(sql, novos_dados + (id_clube,))
                return cur.rowcount > 0
    except Exception as e:
        print(f"ERRO AO ATUALIZAR CLUBE: {e}")
        return False

def atualizar_contrato_db(id_contrato, novos_dados):
    try:
        with psycopg.connect(dados_conexao) as conn:
            with conn.cursor() as cur:
                cur.execute("SET search_path TO aplicacao_crud;")
                sql = """
                UPDATE Contrato SET data_fim = %s, salario = %s, multa = %s
                WHERE id_contrato = %s;
                """
                cur.execute(sql, novos_dados + (id_contrato,))
                return cur.rowcount > 0
    except Exception as e:
        print(f"ERRO AO ATUALIZAR CONTRATO: {e}")
        return False

