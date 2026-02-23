import banco as db

def menu_principal():
    while True:
        print('=' * 30)
        print('MENU PRINCIPAL'.center(30))
        print('=' * 30)
        print('1. Jogador')
        print('2. Clube')
        print('3. Contrato')
        print('4. Sair')
        print('=' * 30)
        opcao = 0
        while opcao <= 0 or opcao > 4:
            opcao = int(input('Opção: '))
            if opcao <= 0 or opcao > 4:
                print('ERRO: Opção inválida!')
        print('=' * 30)
        if opcao == 1:
            menu_jogador()
        elif opcao == 2:
            menu_clube()
        elif opcao == 3:
            menu_contrato()
        elif opcao == 4:
            print("CRUD FINALIZADO")
            print('=' * 30)
            break

def menu_jogador():
    while True:
        print('=' * 30)
        print('MENU DO JOGADOR'.center(30))
        print('=' * 30)
        print('1. Inserir')
        print('2. Buscar')
        print('3. Atualizar')
        print('4. Remover')
        print('5. Voltar')
        print('=' * 30)     
        opcao = 0
        while opcao <= 0 or opcao > 5:
            try:
                opcao = int(input('Opção: '))
                if opcao <= 0 or opcao > 5:
                    print('ERRO: Opção inválida!')
            except ValueError:
                print('ERRO: Digite um número inteiro!')
        if opcao == 1:
            dados = inserir_jogador()
            id_novo = db.salvar_jogador(dados)
            if id_novo:
                print(f"SUCESSO: Jogador cadastrado com ID {id_novo}")
        elif opcao == 2:
            nome, id_j = buscar_jogador()
            resultados = db.buscar_jogadores_db(nome=nome, id_jogador=id_j)
            exibir_jogadores(resultados)
        elif opcao == 3:
            id_alvo = remover_atualizar_jogador()
            if confirmar_operacao(f"ATUALIZAR o jogador de ID {id_alvo}"):
                print("Digite os novos dados do jogador:")
                novos_dados = inserir_jogador()
                sucesso = db.atualizar_jogador_db(id_alvo, novos_dados)
                if sucesso:
                    print(f"SUCESSO: Jogador {id_alvo} atualizado!")
                else:
                    print("ERRO: Não foi possível atualizar. ID inexistente?")
        elif opcao == 4:
            id_alvo = remover_atualizar_jogador()
            if confirmar_operacao(f"REMOVER o jogador de ID {id_alvo}"):
                sucesso = db.remover_jogador_db(id_alvo)
                if sucesso:
                    print(f"SUCESSO: Jogador {id_alvo} removido!")
                else:
                    print("ERRO: ID não encontrado ou falha no banco.")
        elif opcao == 5:
            break

def menu_clube():
    while True:
        print('=' * 30)
        print('MENU DO CLUBE'.center(30))
        print('=' * 30)
        print('1. Inserir')
        print('2. Buscar')
        print('3. Atualizar')
        print('4. Remover')
        print('5. Voltar')
        print('=' * 30)  
        opcao = 0
        while opcao <= 0 or opcao > 5:
            try:
                opcao = int(input('Opção: '))
                if opcao <= 0 or opcao > 5:
                    print('ERRO: Opção inválida!')
            except ValueError:
                print('ERRO: Digite um número inteiro!')
        if opcao == 1:
            dado = inserir_clube()
            id_novo = db.salvar_clube(dado)
            if id_novo:
                print(f"SUCESSO: Clube cadastrado com ID {id_novo}")
        elif opcao == 2:
            nome_busca, id_busca = buscar_clube()
            resultados = db.buscar_clubes_db(nome=nome_busca, id_clube=id_busca)
            exibir_clubes(resultados)
        elif opcao == 3:
            id_alvo = remover_atualizar_clube()
            if confirmar_operacao(f"ATUALIZAR o clube de ID {id_alvo}"):
                print("Digite os novos dados do clube:")
                novos_dados = inserir_clube() 
                sucesso = db.atualizar_clube_db(id_alvo, novos_dados)
                if sucesso:
                    print(f"SUCESSO: Clube {id_alvo} atualizado!")
                else:
                    print("ERRO: Não foi possível atualizar. Verifique o ID.")
        elif opcao == 4:
            id_alvo = remover_atualizar_clube()
            if confirmar_operacao(f"REMOVER o clube de ID {id_alvo}"):
                sucesso = db.remover_clube_db(id_alvo)
                if sucesso:
                    print(f"SUCESSO: Clube {id_alvo} removido!")
                else:
                    print("ERRO: Falha ao remover. O clube existe?")
        elif opcao == 5:
            break

def menu_contrato():
    while True:
        print('=' * 30)
        print('MENU DO CONTRATO'.center(30))
        print('=' * 30)
        print('1. Inserir')
        print('2. Buscar')
        print('3. Atualizar')
        print('4. Remover')
        print('5. Voltar')
        print('=' * 30)
        opcao = 0
        while opcao <= 0 or opcao > 5:
            try:
                opcao = int(input('Opção: '))
                if opcao <= 0 or opcao > 5:
                    print('ERRO: Opção inválida!')
            except ValueError:
                print('ERRO: Digite um número inteiro!')
        if opcao == 1:
            dados = inserir_contrato()
            id_novo = db.salvar_contrato(dados)
            if id_novo:
                print(f"SUCESSO: Contrato firmado com ID {id_novo}")
        elif opcao == 2:
            id_co, id_jo, id_cl = buscar_contrato() 
            resultados = db.buscar_contratos_db(id_contrato=id_co, id_jogador=id_jo)
            exibir_contratos(resultados)
        elif opcao == 3:
            id_alvo = remover_atualizar_contrato()
            if confirmar_operacao(f"ALTERAR os termos do contrato ID {id_alvo}"):
                print("Digite os novos dados (Data Fim, Salário, Multa):")
                data_fim = input('Nova Data Fim (AAAA-MM-DD): ')
                salario = float(input('Novo Salário: '))
                multa = float(input('Nova Multa Rescisória: '))
                sucesso = db.atualizar_contrato_db(id_alvo, (data_fim, salario, multa))
                if sucesso:
                    print(f"SUCESSO: Contrato {id_alvo} atualizado!")
                else:
                    print("ERRO: Falha na atualização.")
        elif opcao == 4:
            id_alvo = remover_atualizar_contrato()
            if confirmar_operacao(f"RESCINDIR o contrato de ID {id_alvo}"):
                sucesso = db.remover_contrato_db(id_alvo)
                if sucesso:
                    print(f"SUCESSO: Contrato {id_alvo} rescindido no sistema!")
                else:
                    print("ERRO: Não foi possível localizar o contrato.")
        elif opcao == 5:
            break

def inserir_jogador():
    while True:
        primeiro_nome = str(input('Primeiro nome: ')).strip().upper()
        tamanho = len(primeiro_nome)
        while tamanho > 45 or primeiro_nome.isalpha() == False:
            if primeiro_nome.isalpha() == False:
                print('ERRO: Primeiro nome inválido!')
            else:
                print('ERRO: Tamanho máximo ultrapassado!')
            primeiro_nome = str(input('Primeiro nome: ')).strip().upper()
            tamanho = len(primeiro_nome)
        break
    while True:
        sobrenome = str(input('Sobrenome: ')).strip().upper()
        verificao1 = str(sobrenome).split()
        verifica2 = ''.join(verificao1)
        tamanho = len(sobrenome)
        while tamanho > 70 or verifica2.isalpha() == False:
            if verifica2.isalpha() == False:
                print('ERRO: Sobrenome inválido!')
            else:
                print('ERRO: Tamanho máximo ultrapassado!')
            sobrenome = str(input('Sobrenome: ')).strip().upper()
            verificao1 = str(sobrenome).split()
            verifica2 = ''.join(verificao1)
            tamanho = len(sobrenome)
        break
    while True:
        print('Data de nascimento(dd/mm/aaaa): ')
        dia = 0
        while dia <= 0 or dia > 31:
            dia = int(input('Dia: '))
            if dia <= 0 or dia > 31:
                print('ERRO: Dia inválido!')
        mes = 0
        while mes <= 0 or mes > 12:
            mes = int(input('Mês: '))
            if mes <= 0 or mes > 12:
                print('ERRO: Mês inválido!')
        ano = 0
        while ano <= 1940 or ano > 2025:
            ano = int(input('Ano: '))
            if ano <= 1940 or ano > 2025:
                print('ERRO: Ano inválido!')
        dn = (str(ano), str(mes), str(dia))
        data_nascimento = '-'.join(dn)
        break
    while True:
        cpf = str(input('CPF: ')).strip()
        tamanho = len(cpf)
        while tamanho != 11 or cpf.isdecimal() == False:
            if cpf.isdecimal() == False:
                print('ERRO: CPF inválido!')
            else:
                print('ERRO: Tamanho máximo ultrapassado!')
            cpf = str(input('CPF: ')).strip()
            tamanho = len(cpf)
        break
    while True:
        licenca = str(input('Licença do jogador: ')).strip()
        tamanho = len(licenca)
        while tamanho != 11 or licenca.isdecimal() == False:
            if licenca.isdecimal() == False:
                print('ERRO: Licença inválida!')
            else:
                print('ERRO: Tamanho máximo ultrapassado!')
            licenca = str(input('Licença do jogador: ')).strip()
            tamanho = len(licenca)
        break
    while True:
        posicao = str(input('Posição[GOL/DEF/MEI/ATA]: ')).strip().upper()
        posicoes = ['GOL', 'DEF', 'MEI', 'ATA']
        while posicao not in posicoes:
            print('ERRO: Posição inválida!')
            posicao = str(input('Posição[GOL/DEF/MEI/ATA]: ')).strip().upper()
        break
    while True:
        altura = int(input('Altura(cm): '))
        while altura <= 140 or altura > 250:
            print('ERRO: Altura inválida!')
            altura = int(input('Altura(cm): '))
        break
    while True:
        peso = float(input('Peso(kg): '))
        while peso <= 30 or peso > 200:
            print('ERRO: peso inválida!')
            peso = float(input('Peso(kg): '))
        break
    while True:
        resp = str(input('Adicionar telefone? [S/N]: ')).strip().upper()[0]
        telefones = list()
        while resp not in 'SN':
            print('ERRO: Opção inválida!')
            resp = str(input('Adicionar telefone? [S/N]: ')).strip().upper()[0]
        while resp == 'S':
            telefone = str(input('Telefone: ')).strip()
            tamanho = len(telefone)
            while tamanho != 11 or telefone.isdecimal() == False:
                print('ERRO: Telefone inválido!')
                telefone = str(input('Telefone: ')).strip()
            telefones.append(telefone)
            resp = str(input('Adicionar outro telefone? [S/N]: ')).strip().upper()[0]
            while resp not in 'SN':
                print('ERRO: Opção inválida!')
                resp = str(input('Adicionar outro telefone? [S/N]: ')).strip().upper()[0]
            if resp == 'N':
                break
        break
    return primeiro_nome, sobrenome, data_nascimento, cpf, licenca, posicao, altura, peso, telefones

def inserir_clube():
    while True:
        nome = str(input('Nome do Clube: ')).strip().upper()
        tamanho = len(nome)
        while tamanho > 70:
            print('ERRO: Tamanho máximo ultrapassado!')
            nome = str(input('Nome do Clube: ')).strip().upper()
            tamanho = len(nome)
        break
    while True:
        cnpj = str(input('CNPJ: ')).strip()
        tamanho = len(cnpj)
        while tamanho != 14 or cnpj.isdecimal() == False:
            if cnpj.isdecimal() == False:
                print('ERRO: CNPJ inválido!')
            else:
                print('ERRO: Tamanho máximo ultrapassado!')
            cnpj = str(input('CNPJ: ')).strip()
            tamanho = len(cnpj)
        break
    while True:
        cidade = str(input('Cidade: ')).strip().upper()
        verificao1 = str(cidade).split()
        verifica2 = ''.join(verificao1)
        tamanho = len(cidade)
        while tamanho > 50 or verifica2.isalpha() == False:
            if verifica2.isalpha() == False:
                print('ERRO: Cidade inválida!')
            else:
                print('ERRO: Tamanho máximo ultrapassado!')
            cidade = str(input('Cidade: ')).strip().upper()
            verificao1 = str(cidade).split()
            verifica2 = ''.join(verificao1)
            tamanho = len(cidade)
        break
    while True:
        estado = str(input('Estado(sigla): ')).strip().upper()
        tamanho = len(estado)
        while tamanho > 2:
            print('ERRO: Tamanho máximo ultrapassado!')
            estado = str(input('Estado(sigla): ')).strip().upper()
            tamanho = len(estado)
        break
    return nome, cnpj, cidade, estado

def inserir_contrato():
    salario = None
    multa = None
    id_clube = int(input('ID do Clube: '))
    id_jogador = int(input('ID do Jogador: '))
    while True:
        print('Data do fim do contrato(dd/mm/aaaa): ')
        dia = 0
        while dia <= 0 or dia > 31:
            dia = int(input('Dia: '))
            if dia <= 0 or dia > 31:
                print('ERRO: Dia inválido!')
        mes = 0
        while mes <= 0 or mes > 12:
            mes = int(input('Mês: '))
            if mes <= 0 or mes > 12:
                print('ERRO: Mês inválido!')
        ano = 0
        while ano < 2026:
            ano = int(input('Ano: '))
            if ano < 2026:
                print('ERRO: Ano inválido!')
        df = (str(ano), str(mes), str(dia))
        data_fim = '-'.join(df)
        break
    while True:
        resp = str(input('Adicionar salário? [S/N]: ')).strip().upper()[0]
        while resp not in 'SN':
            print('ERRO: Opção inválida!')
            resp = str(input('Adicionar salário? [S/N]: ')).strip().upper()[0]
        if resp == 'S':
            salario = float(input('Salario: '))
            while salario < 0:
                print('ERRO: Salário inválido!')
                salario = float(input('Salário: '))
            break
        if resp == 'N':
            break
    while True:
        resp = str(input('Adicionar multa? [S/N]: ')).strip().upper()[0]
        while resp not in 'SN':
            print('ERRO: Opção inválida!')
            resp = str(input('Adicionar multa? [S/N]: ')).strip().upper()[0]
        if resp == 'S':
            multa = float(input('Multa: '))
            while multa < 0:
                print('ERRO: Multa inválido!')
                multa = float(input('Multa: '))
            break
        if resp == 'N':
            break
    return id_clube, id_jogador, data_fim, salario, multa

def buscar_jogador():
    nome = None
    id_jogador = None
    print('=' * 30)
    print('1. Buscar pelo nome do Jogador')
    print('2. Buscar pelo ID do Jogador')
    opcao = 0
    while opcao <= 0 or opcao > 2:
        try:
            opcao = int(input('Opção: '))
            if opcao <= 0 or opcao > 2:
                print('ERRO: Opção inválida!')
        except ValueError:
            print('ERRO: Digite um número inteiro!')
    if opcao == 1:
        while True:
            nome = str(input('Nome: ')).strip().upper()
            verificao1 = str(nome).split()
            verifica2 = ''.join(verificao1)
            tamanho = len(nome)
            while tamanho > 70 or verifica2.isalpha() == False:
                if verifica2.isalpha() == False:
                    print('ERRO: Nome inválido!')
                else:
                    print('ERRO: Tamanho máximo ultrapassado!')
                nome = str(input('Nome: ')).strip().upper()
                verificao1 = str(nome).split()
                verifica2 = ''.join(verificao1)
                tamanho = len(nome)
            break
    if opcao == 2:
        id_jogador = int(input("ID do jogador: "))
    return nome, id_jogador

def buscar_clube():
    nome = None
    id_clube = None
    print('=' * 30)
    print('1. Buscar pelo nome do Clube')
    print('2. Buscar pelo ID do Clube')
    opcao = 0
    while opcao <= 0 or opcao > 2:
        try:
            opcao = int(input('Opção: '))
            if opcao <= 0 or opcao > 2:
                print('ERRO: Opção inválida!')
        except ValueError:
            print('ERRO: Digite um número inteiro!')
    if opcao == 1:
        while True:
            nome = str(input('Nome: ')).strip().upper()
            verificao1 = str(nome).split()
            verifica2 = ''.join(verificao1)
            tamanho = len(nome)
            while tamanho > 70 or verifica2.isalpha() == False:
                if verifica2.isalpha() == False:
                    print('ERRO: Nome inválido!')
                else:
                    print('ERRO: Tamanho máximo ultrapassado!')
                nome = str(input('Nome: ')).strip().upper()
                verificao1 = str(nome).split()
                verifica2 = ''.join(verificao1)
                tamanho = len(nome)
            break
    if opcao == 2:
        id_clube = int(input('ID do Clube: '))
    return nome, id_clube

def remover_atualizar_jogador():
    print('=' * 30)
    id_jogador = int(input('ID do Jogador: '))
    return id_jogador

def remover_atualizar_clube():
    print('=' * 30)
    id_clube = int(input('ID do Clube: '))
    return id_clube

def remover_atualizar_contrato():
    print('=' * 30)
    id_contrato = int(input('ID do Contrato: '))
    return id_contrato

def buscar_contrato():
    id_contrato = None
    id_jogador = None
    id_clube = None
    print('=' * 30)
    print('1. Buscar pelo ID do Contrato')
    print('2. Buscar pelo ID do Jogador')
    print('3. Buscar pelo ID do Clube')
    opcao = 0
    while opcao <= 0 or opcao > 3:
        try:
            opcao = int(input('Opção: '))
            if opcao <= 0 or opcao > 3:
                print('ERRO: Opção inválida!')
        except ValueError:
            print('ERRO: Digite um número inteiro!')
    if opcao == 1:
        id_contrato = int(input('ID do Contrato: '))
    if opcao == 2:
        id_jogador = int(input('ID do Jogador: '))
    if opcao == 3:
        id_clube = int(input('ID do Clube: '))
    return id_contrato, id_jogador, id_clube

def exibir_jogadores(jogadores):
    if not jogadores:
        print('=' * 30)
        print('NENHUM JOGADOR ENCONTRADO'.center(30))
        print('=' * 30)
        return
    
    print('=' * 65)
    print(f"{'ID':<5} | {'NOME COMPLETO':<35} | {'POSIÇÃO':<15}")
    print('-' * 65)
    
    for j in jogadores:
        nome_completo = f"{j[1]} {j[2]}"
        print(f"{j[0]:<5} | {nome_completo:<35} | {j[6]:<15}")
    print('=' * 65)

def exibir_clubes(clubes):
    if not clubes:
        print('=' * 30)
        print('NENHUM CLUBE ENCONTRADO'.center(30))
        print('=' * 30)
        return
    print('=' * 80)
    print(f"{'ID':<5} | {'NOME DO CLUBE':<35} | {'CIDADE':<20} | {'UF':<5}")
    print('-' * 80)
    for c in clubes:
        print(f"{c[0]:<5} | {c[1]:<35} | {c[3]:<20} | {c[4]:<5}")
    print('=' * 80)

def exibir_contratos(contratos):
    if not contratos:
        print('=' * 30)
        print('NENHUM CONTRATO ENCONTRADO'.center(30))
        print('=' * 30)
        return
    print('=' * 85)
    print(f"{'ID':<5} | {'ID CLUBE':<10} | {'ID JOGADOR':<10} | {'DATA FIM':<15} | {'SALÁRIO':<15}")
    print('-' * 85)
    for co in contratos:
        print(f"{co[0]:<5} | {co[1]:<10} | {co[2]:<10} | {co[3]:<15} | {co[4]:<15}")
    print('=' * 85)

def confirmar_operacao(mensagem):
    print('=' * 40)
    print(f'ATENÇÃO: Deseja realmente {mensagem}?')
    while True:
        resp = str(input('Confirma? [S/N]: ')).strip().upper()
        if resp == 'S':
            return True
        if resp == 'N':
            print('Operação cancelada pelo usuário.')
            return False
        print('ERRO: Digite apenas S para Sim ou N para Não!')
