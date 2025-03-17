import sqlite3

def conectar_banco():
    conexao = sqlite3.connect("trvl.db")
    return conexao 

def criar_tabelas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''create table if not exists usuarios
                   (email text primary key,nome text,senha text)''')
    
    cursor.execute('''create table if not exists projetos_de_viagem
                   (id integer primary key,id_usuario text,destino text,data_prevista text,
                   status text,imagem text,gastos real,dinheiro_guardado real)''')
    
    conexao.commit()

def criar_usuario(email, nome, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO CRIAR UM NOVO USUÁRIO
        cursor.execute('insert into usuarios(email, nome, senha) values (?, ?, ?)', 
                       (email, nome, senha))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()

def deletar_usuario(email):
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO DELETAR UM USUÁRIO
        cursor.execute('DELETE FROM usuarios WHERE email = ?',
                       (email, ))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def mudar_usuario(email, nome):
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO MUDAR UM USUÁRIO
        cursor.execute("UPDATE usuarios SET nome = 'SeuGalisteu' WHERE email = ? and nome = ?",
                       (email, nome, ))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def mudar_senha(email, senha):
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO MUDAR UMA SENHA
        cursor.execute("UPDATE usuarios SET senha = '4321' WHERE email = ? and senha = ?",
                       (email, senha, ))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def criar_projeto(id_usuario,destino,data_prevista,status,imagem,gastos,dinheiro_guardado):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('''INSERT INTO projetos_de_viagem(id_usuario,destino,data_prevista,
                       status,imagem,gastos,dinheiro_guardado) values (?, ?, ? , ?, ?, ?, ?)'''
                       ,(id_usuario,destino,data_prevista,status,imagem,gastos,dinheiro_guardado,))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()  

def buscar_viagens(id_usuario):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    # PREENCHA AQUI, BUSCAR TODAS AS VIAGENS ordem: destino, data prevista, status, imagem
    cursor.execute('''SELECT destino, data_prevista, status, imagem FROM projetos_de_viagem
                   WHERE id_usuario = ?''', (id_usuario,))
    viagens = cursor.fetchall()
    conexao.close()

    return viagens

def apagar_viagem (id_viagem):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('DELETE FROM projetos_de_viagem WHERE id = ?', id_viagem)
        
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()
        
def mostrar_id_viagens (id_email):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        cursor.execute('SELECT * FROM projetos_de_viagem WHERE id_usuario = ?', (id_email,))
        conexao.commit()
        viagens = cursor.fetchall()
        return viagens
    
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()

def editar_viagem(email, senha):
    
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    try:
        # PREENCHA AQUI - QUAL O COMANDO MUDAR UMA VIAGEM
        cursor.execute("UPDATE projetos_de_viagem SET destino = ',data_prevista,status,imagem,gastos,dinheiro_guardado ",
                       (email, senha, ))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conexao.close()

if __name__ == '__main__': 
    conexao = conectar_banco()
    criar_tabelas ()
    #deletar_usuario("seugeronimo@email.com")
    
    #mudar_usuario ("seugeronimo@email.com", "SeuGeronimo")
    
    #mudar_senha ("seugeronimo@email.com", "1234")
    
   # viagens =  mostrar_id_viagens ("seugeronimo@email.com")
   # print (viagens)
   
apagar_viagem ("1")

    

    

           
        
 

    

    

