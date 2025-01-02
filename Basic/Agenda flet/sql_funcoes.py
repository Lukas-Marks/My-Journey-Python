# Biblioteca do Curso Python 536 para Banco de Dados

# Obs: As funções ter as 4 etapas: 
#   1. Iniciar a Conexão  
#   2. CRUD/Query 
#   3. Commit  
#   4. Finalizar a Conexão

import sqlite3


# ---------------------- CRIAR TABELA ---------------------------
# entrada: nome do banco de dados vai ser db
def criarTabelaContatos(db):

    # 1.
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # 2.
    queryCriarTabela = '''CREATE TABLE IF NOT EXISTS "Contatos" (
        "id"	INTEGER,
        "nome"	TEXT,
        "sobrenome"	TEXT,
        "email"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
    );'''

    cursor.execute(queryCriarTabela)

    # 3. COMMIT
    conn.commit()

    # 4. Fechar conexão
    conn.close()
# ---------------------- INSERIR DADOS --------------------------
def inserirDados(db, nome, sobrenome, email):

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    queryInserirRegistro = f'''
                INSERT INTO "Contatos" (nome, sobrenome, email)
                VALUES ("{nome}", "{sobrenome}", "{email}");
    '''
    cursor.execute(queryInserirRegistro)

    conn.commit()
    conn.close()

# ---------------------- ATUALIZAR DADOS ------------------------
def atualizarDados(db, nome, sobrenome, email, numRegistro):

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    if len(nome) != 0 and nome != '\r':

        queryAtualizarRegistro = f'''
                UPDATE "Contatos" 
                SET nome = "{nome}" 
                WHERE id="{numRegistro}"
        '''
        cursor.execute(queryAtualizarRegistro)

    if len(sobrenome) != 0 and sobrenome != '\r':

        queryAtualizarRegistro = f'''
                UPDATE "Contatos" 
                SET sobrenome = "{sobrenome}" 
                WHERE id="{numRegistro}"
        '''
        cursor.execute(queryAtualizarRegistro)

    if len(email) != 0 and email != '\r':

        queryAtualizarRegistro = f'''
                UPDATE "Contatos" 
                SET email = "{email}" 
                WHERE id="{numRegistro}"
        '''
        cursor.execute(queryAtualizarRegistro)
        

    conn.commit()
    conn.close()



# ---------------------- APAGAR DADOS ---------------------------
def apagarDados(db, numRegistro):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    queryApagarRegistro = f'''
            DELETE FROM "Contatos" 
            WHERE id="{numRegistro}"
    '''
    cursor.execute(queryApagarRegistro)

    conn.commit()
    conn.close()

# ---------------------- SELECIONAR DADOS - TODOS ----------------
def selecionarDadosId(db, numRegistro):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    querySelecionarRegistros = f'''
                SELECT * FROM "Contatos"
                WHERE id = "{numRegistro}"
    '''
    cursor.execute(querySelecionarRegistros)
    dados = cursor.fetchall()
 
    conn.commit()
    conn.close()

    return dados
# ---------------------- SELECIONAR DADOS - PARCIAL --------------

def selecionarDadosParcial(db, primeiraRegistro, quantidade):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    querySelecionarRegistros = f'''
        SELECT * FROM "Contatos" 
        WHERE id>="{primeiraRegistro}"
        LIMIT {quantidade}
    '''
    cursor.execute(querySelecionarRegistros)
    dados = cursor.fetchall()

    conn.commit()
    conn.close()
    
    return dados

# ---------------------- SELECIONAR DADOS - ID -------------------

def selecionarTodosDados(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    querySelecionarRegistros = '''
                SELECT * FROM "Contatos"
    '''
    cursor.execute(querySelecionarRegistros)
    dados = cursor.fetchall()

    conn.commit()
    conn.close()

    return dados