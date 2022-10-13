import sqlite3
from logs import Log
class Dados:
    def __init__(self):
        self.banco = sqlite3.connect('banco de dados\\dados.db')
        self.cursor = self.banco.cursor()
        self.ac = None
        self.log_dados =Log()
    def inserir(self, nome = None,celula = None,email = None,telefone= None,data= None, id= None,tabela= None, lider =None, observacao =None,endereco =None):
        if tabela =="dados":
            try:
                self.cursor.execute(f"INSERT INTO {tabela} (id,nome,celula,email,telefone,nascimento) VALUES ('{int(id)}','{nome}', '{celula}','{email}','{telefone}' ,'{data}')")
                self.banco.commit()
                self.log_dados.info(f"COMANDO = INSERT INTO {tabela} (id,nome,celula,email,telefone,nascimento) VALUES ('{int(id)}','{nome}', '{celula}','{email}','{telefone}' ,'{data}')")
                return True
            except:
                self.log_dados.error(f"ID JÁ EXISTE = INSERT INTO {tabela} (id,nome,celula,email,telefone,nascimento) VALUES ('{int(id)}','{nome}', '{celula}','{email}','{telefone}' ,'{data}')")
                return False
        elif tabela =="celula":
            try:    
                self.cursor.execute(f"INSERT INTO {tabela} (id,nome,lider,endereco,observacao) VALUES ('{id}','{nome}', '{lider}','{endereco}' ,'{observacao}')")
                self.banco.commit()
                self.log_dados.info(f"COMANDO = INSERT INTO {tabela} (id,nome,lider,endereco,observacao) VALUES ('{id}','{nome}', '{lider}','{endereco}' ,'{observacao}')")
                return True
            except:
                self.log_dados.error(f"ID JÁ EXISTE = INSERT INTO {tabela} (id,nome,lider,endereco,observacao) VALUES ('{id}','{nome}', '{lider}','{endereco}' ,'{observacao}')")
                return False
    def ver (self,variavel, tabela,ac):
        self.cursor.execute(f"SELECT {variavel} FROM {tabela} {ac}")
        return self.cursor.fetchall()

    def deletar(self,id):
        try:
            self.cursor.execute(f"DELETE FROM dados WHERE ID={id}")
            self.banco.commit()
            return True
        except:
            return False
    def alterar(self, nome,celula,email,telefone,data, id):
        try:
            self.cursor.execute(f"UPDATE dados SET nome ='{nome}', celula='{celula}',email='{email}', telefone='{telefone}', nascimento='{data}' where id={id}")
            self.banco.commit()
            return True
        except:
            return False
    pass

class Login:
    def __init__(self):
        self.banco = sqlite3.connect('banco de dados\\dados.db')
        self.cursor = self.banco.cursor()
    def entrar(self):
        usuario = self.cursor.execute(f"SELECT usuario FROM login")
        usuario =usuario.fetchall()
        senha = self.cursor.execute(f"SELECT senha FROM login")
        senha = senha.fetchall()
        return usuario, senha
    def inserir(self, usuario,senha):
        try:
            self.cursor.execute(f"INSERT INTO login (usuario,senha) VALUES ('{usuario}','{senha}')")
            self.banco.commit()
            return True
        except:
            return False
    pass