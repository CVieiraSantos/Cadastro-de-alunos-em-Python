from os import curdir
import sqlite3


def conect():
    conn = sqlite3.connect('F:\Temp\Python\Sistema_De_Cadastro_AV2\cadastro.db')
    cursor = conn.cursor()    
    cursor.execute('''CREATE TABLE IF NOT EXISTS aluno(matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    nome text,
    av1 REAL, 
    av2 REAL, 
    av3 REAL, 
    avd REAL, 
    avds REAL, 
    email TEXT, 
    endereco TEXT, 
    campus TEXT, 
    periodo TEXT) ''')

    conn.commit()
    conn.close()


def inserir(nome, av1, av2, av3, avd, avds, email, endereco, campus, periodo):
    conn = sqlite3.connect('F:\Temp\Python\Sistema_De_Cadastro_AV2\cadastro.db')
    cursor = conn.cursor() 
    cursor.execute('INSERT INTO aluno VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )', (nome, av1, av2, av3, avd, avds, email, endereco, campus, periodo))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('F:\Temp\Python\Sistema_De_Cadastro_AV2\cadastro.db')
    cursor = conn.cursor() 
    cursor.execute('SELECT * FROM aluno')
    linhas = cursor.fetchall()    
    conn.close()
    return linhas
    
def delete(matricula):
    conn = sqlite3.connect('F:\Temp\Python\Sistema_De_Cadastro_AV2\cadastro.db')
    cursor = conn.cursor() 
    cursor.execute('DELETE FROM aluno WHERE MATRICULA = ?', (matricula,))
    conn.commit()
    conn.close()

def update(matricula, nome, av1, av2, av3, avd, avds, email, endereco, campus, periodo):
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE aluno SET nome=?, av1=?, av2=?, av3=?, avd=?, avds=?, email=?, endereco=?, campus=?, periodo=? WHERE matricula = ?', (nome, av1, av2, av3, avd, avds, email, endereco, campus, periodo, matricula))
    conn.commit()
    conn.close()
    
conect()



