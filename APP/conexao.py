import mysql.connector
from logs import Log

banco_dados = "membros"
banco_celula ="celula"

class Dados:
    def __init__(self):
        self.banco = conexao()
        self.cursor = self.banco.cursor()
        self.ac = None
        self.log_dados =Log()
    def inserir(self, nome = None,celula = None,email = None,telefone= None,data= None, id= None,tabela= None, lider =None, observacao =None,endereco =None):
        if tabela ==banco_dados:
            try:
                self.cursor.execute(f"INSERT INTO {tabela} (id,nome,celula,email,telefone,nascimento) VALUES ('{int(id)}','{nome}', '{celula}','{email}','{telefone}' ,'{data}')")
                self.banco.commit()
                self.log_dados.info(f"COMANDO = INSERT INTO {tabela} (id,nome,celula,email,telefone,nascimento) VALUES ('{int(id)}','{nome}', '{celula}','{email}','{telefone}' ,'{data}')")
                return True
            except:
                self.log_dados.error(f"ID JÁ EXISTE = INSERT INTO {tabela} (id,nome,celula,email,telefone,nascimento) VALUES ('{int(id)}','{nome}', '{celula}','{email}','{telefone}' ,'{data}')")
                return False
        elif tabela ==banco_celula:
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
            self.cursor.execute(f"DELETE FROM {banco_dados} WHERE ID={id}")
            self.banco.commit()
            return True
        except:
            return False
    def alterar(self, nome,celula,email,telefone,data, id):
        try:
            self.cursor.execute(f"UPDATE {banco_dados} SET nome ='{nome}', celula='{celula}',email='{email}', telefone='{telefone}', nascimento='{data}' where id={id}")
            self.banco.commit()
            return True
        except:
            return False

class Login:
    def __init__(self):
        self.banco = conexao()
        self.cursor = self.banco.cursor()
    def entrar(self):
        self.cursor.execute(f"SELECT usuario FROM login ORDER BY id")
        usuario = self.cursor.fetchall()
        senha = self.cursor.execute(f"SELECT senha FROM login ORDER BY id")
        senha = self.cursor.fetchall()
        return usuario, senha
    def inserir(self, usuario,senha):
        try:
            self.cursor.execute(f"INSERT INTO login (usuario,senha) VALUES ('{usuario}','{senha}')")
            self.banco.commit()
            return True
        except:
            return False
    def ver (self,variavel, tabela,ac):
        self.cursor.execute(f"SELECT {variavel} FROM {tabela} {ac}")
        return self.cursor.fetchall()

