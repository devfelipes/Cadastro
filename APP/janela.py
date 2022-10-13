from conexao import Dados
from conexao import Login
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as showinfo
from logs import Log

banco_dados = "dados"
banco_celula ="celula"

fotos = {'fundo':"grafica\\fundo.png",
        'fundo_login':"grafica\\login.png",
        'fundo_cadastro': "grafica\\cadastro.png",
        'cadastro_Celula': "grafica\\cadastro_celula.png",
        'botao1':"grafica\\botao1.png",
        'botao2':"grafica\\botao2.png",
        'botao3': "grafica\\botao3.png",
        'botao4': "grafica\\botao4.png",
        'botao5': "grafica\\botao5.png",
        'botao6': "grafica\\botao6.png",
        'botao7': "grafica\\botao7.png"}
class Janela():

    def __init__(self, root,tela, geometria,icone, w, h):
        self.log = Log()
        try:
            self.root = root
            self.root.title(tela)
            self.titulo = tela
            self.root.geometry(geometria)
            self.root.maxsize(w,h)
            self.root.minsize(w,h)
            self.fotos()
            self.root.iconbitmap(default=icone)
            self.root.resizable(width=1, height=1)
            self.sairtela = None
            self.ftela()
            self.conexao = Dados()
            self.log.debug('Programa rodando')
            self.ftela_celula()
        except:
            self.log.error('PROGRAMA SEM RODAR NA FUNÇÃO JANELA')
        pass

    def fotos(self):
        try:
            self.fundo = PhotoImage(file=fotos["fundo"])
            self.fundo_login = PhotoImage(file=fotos['fundo_login'])
            self.fundo_cadastro = PhotoImage(file=fotos['fundo_cadastro'])
            self.botao1 = PhotoImage(file=fotos["botao1"])
            self.botao2 = PhotoImage(file=fotos["botao2"])
            self.botao3 = PhotoImage(file=fotos["botao3"])
            self.botao4 = PhotoImage(file=fotos["botao4"])
            self.botao5 = PhotoImage(file=fotos["botao5"])
            self.botao6 = PhotoImage(file=fotos["botao6"])
            self.botao7 = PhotoImage(file=fotos["botao7"])
            self.cadastro_celula = PhotoImage(file=fotos['cadastro_Celula'])
        except:
            self.log.error('PROGRAMA SEM RODAR NO METODO JANELA FUNÇÃO FOTOS')

    def ftela(self):
        try:
            Label(self.root, image=self.fundo).pack()
            self.texto_id()
            self.botao()
            self.entrada()
            self.lista()
            self.select(ver=True)
            self.conectar()
            self.barrademenu()
        except:
            self.log.error('PROGRAMA SEM RODAR NO METODO JANELA FUNÇÃO ftela')

    def run(self):
        self.root.mainloop()
        pass

    def atualizar(self):
        self.root.update()
        pass

    def botao (self):
        self.btcadastro =Button(self.root,bd=0, image=self.botao1, command= lambda: self.salvar())
        self.btcadastro.place(width=177, height=60, x= 66, y=78)
        self.btbuscar =Button(self.root,bd=0 ,image=self.botao2, command=self.buscar)
        self.btbuscar.place(width=177, height=60, x= 685, y=78)
        self.btalterar =Button(self.root,bd=0 ,image=self.botao3, command= lambda: self.values_verificacao('ALTERAR'))
        self.btalterar.place(width=177, height=60, x= 271, y=78)
        self.btapagar =Button(self.root,bd=0 ,image=self.botao4, command= lambda: self.values_verificacao('APAGAR'))
        self.btapagar.place(width=177, height=60, x= 476, y=78)

    def entrada(self):
        self.nome =Entry(self.root, bd=1, font=("calibre", 10), background='white', justify=LEFT, foreground='black')
        self.nome.place(width=456, height=31, x= 144, y=177)
        resultado = self.conexao.ver('nome','celula','order by nome')
        self.celula= ttk.Combobox(self.root, values=resultado, justify=LEFT, background='white', foreground='black')
        self.celula.place(width=233, height=31, x= 600, y=275)
        self.email =Entry(self.root,bd=1, font=("calibre", 10), background='white', justify=LEFT, foreground='black')
        self.email.place(width=325, height=31, x= 144, y=226)
        self.data =Entry(self.root,bd=1, font=("calibre", 10), background='white', justify=LEFT, foreground='black')
        self.data.place(width=180, height=31, x= 308, y=276)
        self.telefone =Entry(self.root,bd=1, font=("calibre", 10), background='white', justify=LEFT, foreground='black')
        self.telefone.place(width=233, height=31, x= 580, y=225)
        self.id =Entry(self.root,bd=1, font=("calibre", 10), background='white', justify=LEFT, foreground='black')
        self.id.place(width=85, height=31, x= 643, y=177)

    def limpar (self):
        self.nome.delete(0,END)
        self.celula.delete(0,END)
        self.email.delete(0,END)
        self.telefone.delete(0,END)
        self.data.delete(0,END)
        self.id.delete(0,END)
        self.texto_id()

    def values_entrada(self):
        self.values_id = self.id.get()
        self.values_nome = self.nome.get().upper()
        self.values_celula = self.resultado_combox(self.celula.get())
        self.values_celula = str(self.values_celula)
        if self.values_celula =='[]':
            self.values_celula =''
        else:
            self.values_celula = self.values_celula.replace(',','').replace('(','').replace(')','').replace('[','').replace(']','')
        self.values_data = self.data.get().upper()
        self.values_email = self.email.get().lower()
        self.values_telefone = self.telefone.get().upper()
        return self.values_id ,self.values_nome,self.values_celula,self.values_data,self.values_email,self.values_telefone

    def salvar (self):
        ins_id,nome, celula,data,email,telefone= self.values_entrada()
        if ins_id=='':
            ins_id= self.ver_id
            if ins_id =='None':
                ins_id ='1'
        else:
            pass
        try:
            data = str(data)
            if data in'':
                res_data = True
            else:
                if data[2] == '/' and data[5] == '/' and len(data) == 10:
                    res_data =True
                else:
                    showinfo.showerror(title='AVISO', message= 'ERRO!!\nDATA INVÁLIDA\nEXEMPLO:10/02/2003')
                    res_data =False
        except:
            showinfo.showerror(title='AVISO', message= 'ERRO!!\nDATA INVÁLIDA\nEXEMPLO:10/02/2003')

        if res_data ==True:
            if nome in '' and email in '' and telefone in '':
                showinfo.showerror(title='AVISO', message= 'ERRO!!\n NOME, EMAIL E TELEFONE SÃO OBRIGATÓRIO')
            elif email in '' and telefone in '':
                showinfo.showerror(title='AVISO', message= 'ERRO!!\n EMAIL E TELEFONE SÃO OBRIGATÓRIO')
            elif nome in '' and email in '':
                showinfo.showerror(title='AVISO', message= 'ERRO!!\n NOME E EMAIL SÃO OBRIGATÓRIO')
            elif nome in '' and telefone in '':
                showinfo.showerror(title='AVISO', message= 'ERRO!!\n NOME E TELEFONE SÃO OBRIGATÓRIO')
            elif nome in '':
                showinfo.showerror(title='AVISO', message= 'ERRO!!\n NOME É OBRIGATÓRIO')
            elif email in '' :
                showinfo.showerror(title='AVISO', message= 'ERRO!!\n EMAIL É OBRIGATÓRIO')
            elif telefone in '':
                showinfo.showerror(title='AVISO', message= 'ERRO!!\n TELEFONE É OBRIGATÓRIO')
            else:
                try:
                    tel = str(telefone)
                    email = str(email)
                    res_email = False
                    for x in email:
                        if x in '@':
                            res_email = True
                    if res_email==True:
                        if len(tel) ==11 or tel[0] =='(' and tel[3] ==')' and tel[4] ==' ' and tel[10] =='-' and len(tel) ==15:
                            if len(tel) ==11:
                                res_tel = f'({tel[0] + tel[1]}) {tel[2]}{tel[3] + tel[4] + tel[5] + tel[6]}-{tel[7] + tel[8] + tel[9] + tel[10]}'
                            else:
                                res_tel = tel
                            if celula == '':
                                celula ='1'
                                self.salvar_into(nome,celula,email,res_tel,data,ins_id, banco_dados)
                            else:
                                self.salvar_into(nome,celula,email,res_tel,data,ins_id, banco_dados)
                        else:
                            showinfo.showerror(title='AVISO', message= 'ERRO!!\nNÚMERO INVÁLIDO\nEXEMPLO: DDD + NUMERO\n71986481515 ou (71) 98648-1515')
                    else:
                        showinfo.showerror(title='AVISO', message= 'ERRO!!\nEMAIL INVÁLIDO\nEXEMPLO: exemploemail@hotmail.com')
                except:
                    print('ERROR')
        else:
            pass

    def salvar_into(self,nome =None,celula=None,email=None,telefone=None,data=None,id=None,tabela=None,obeservacao=None,endereco=None,lider=None):
        if tabela =="dados":
            run = self.conexao.inserir(nome = nome,celula =celula,email =email,telefone= telefone,data=data,id=id, tabela= tabela)
            if run ==True:
                showinfo.showinfo(title='AVISO', message= 'DADOS SALVO')
                self.limpar()
                self.texto_id()
                self.select(delete=True,ver=True)
                self.root.update()
            else:
                showinfo.showerror(title='AVISO', message= 'ERRO!!\n VERIFIQUE AS ENTRADAS!\n O ID PODE JÁ EXISTIR!')
                self.root.update()
        elif tabela =="celula":
            run = self.conexao.inserir(nome = nome,lider =lider,observacao=obeservacao,endereco=endereco,id=id, tabela= tabela)
            if run ==True:
                showinfo.showinfo(title='AVISO', message= 'DADOS SALVO')
                self.limpar()
                self.texto_id()
                self.select(delete=True,ver=True)
                self.root.update()
            else:
                showinfo.showerror(title='AVISO', message= 'ERRO!!\n VERIFIQUE AS ENTRADAS!\n O ID OU NOME, PODE JÁ EXISTIR!')
                self.root.update()

    def texto_id(self, tela='PRINCIPAL'):
        self.conexao = Dados()
        if tela=='PRINCIPAL':
            self.ver_id = self.conexao.ver('max(id)','dados', '')
            self.ver_id = str(self.ver_id[0]).replace(',','').replace('(','').replace(')','')
            if self.ver_id =='None':
                self.txt_id = Label(self.root, text=f'PROX ID:1', font=('calibre', 15), background='#FFFEA9', foreground='black')
                self.txt_id.place(width=135, height=30, x=730, y=175)
            else:
                self.ver_id = int(self.ver_id) + 1
                self.txt_id = Label(self.root, text=f'PROX ID:{self.ver_id}', font=('calibre', 15), background='#FFFEA9', foreground='black')
                self.txt_id.place(width=135, height=30, x=730, y=175)
            pass
        elif tela =='CELULA':
            self.ver_id = self.conexao.ver('max(id)','celula', '')
            self.ver_id = str(self.ver_id[0]).replace(',','').replace('(','').replace(')','')
            if self.ver_id =='None':
                self.txt_id = Label(self.tela_celula, text=f'PROX ID:1', font=('calibre', 10), background='white', foreground='#8F4E2C')
                self.txt_id.place(width=135, height=20, x=10, y=10)
            else:
                self.ver_id = int(self.ver_id) + 1
                self.txt_id = Label(self.tela_celula, text=f'PROX ID:{self.ver_id}', font=('calibre', 10), background='white', foreground='#8F4E2C')
                self.txt_id.place(width=135, height=20, x=160, y=50)

    def lista(self):
        self.resultado = ttk.Treeview(self.root, height=3,columns=('col1','col2','col3','col4', 'col5', 'col6'))
        self.resultado.heading('#0',text='')
        self.resultado.heading('#1',text='ID')
        self.resultado.heading('#2', text='NOME')
        self.resultado.heading('#3', text='CELULA')
        self.resultado.heading('#4', text='NASCIMENTO')
        self.resultado.heading('#5', text='TELEFONE')
        self.resultado.heading('#6', text='EMAIL')
        self.resultado.column('#0',width=0 )
        self.resultado.column('#1', width=20)
        self.resultado.column('#2', width=220)
        self.resultado.column('#3', width=150)
        self.resultado.column('#4', width=80)
        self.resultado.column('#5', width=90)
        self.resultado.column('#6', width=200)
        self.scrollvertical = Scrollbar(self.root, orient='vertical')
        self.resultado.place(width=828, height=311, x=46, y=350)
        self.resultado.configure(yscroll=self.scrollvertical.set)
        self.scrollvertical.place(width=20, height=311, x=874, y=350)
        self.resultado.bind('<Double-1>', self.duploclick)
        pass

    def limpar_lista(self):
        self.resultado.delete(*self.resultado.get_children())

    def select(self, delete=False, ver=False, order='d.id', banco='dados as d left outer join celula as c on c.id = d.celula', var='d.id,d.nome,c.nome,d.nascimento,d.telefone,d.email'):
        try:
            if delete==True:
                self.limpar_lista()
            else:
                pass
            if ver ==True:
                dados = self.conexao.ver(f'{var}',f'{banco}',f'order by {order}')
                for x in dados:
                    self.resultado.insert('',END, values=x )
            else:
                pass
        except:
            showinfo.showerror(title='AVISO', message= 'ERRO!!!!!')

    def buscar(self):
        id,nome,celula,data,email,telefone= self.values_entrada()
        if telefone != '':
            dados = self.conexao.ver('d.id,d.nome,c.nome,d.nascimento,d.telefone,d.email','dados as d left outer join celula as c on c.id = d.celula',f"where d.telefone like '{telefone}%' order by d.telefone")
            self.limpar_lista()
            for x in dados:
                self.resultado.insert('',END, values=x )
        if email != '':
            dados = self.conexao.ver('d.id,d.nome,c.nome,d.nascimento,d.telefone,d.email','dados as d left outer join celula as c on c.id = d.celula',f"where d.email like '{email}%' order by d.email")
            self.limpar_lista()
            for x in dados:
                self.resultado.insert('',END, values=x )
        if celula != '':
            dados = self.conexao.ver('d.id,d.nome,c.nome,d.nascimento,d.telefone,d.email','dados as d left outer join celula as c on c.id = d.celula',f"where d.celula like '{celula}%' order by d.celula")
            self.limpar_lista()
            for x in dados:
                self.resultado.insert('',END, values=x )
        if data != '':
            dados = self.conexao.ver('d.id,d.nome,c.nome,d.nascimento,d.telefone,d.email','dados as d left outer join celula as c on c.id = d.celula',f"where d.data like '{data}%' order by d.nascimento")
            self.limpar_lista()
            for x in dados:
                self.resultado.insert('',END, values=x )
        if nome != '':
            dados = self.conexao.ver('d.id,d.nome,c.nome,d.nascimento,d.telefone,d.email','dados as d left outer join celula as c on c.id = d.celula',f"where d.nome like '{nome}%' order by d.nome")
            self.limpar_lista()
            for x in dados:
                self.resultado.insert('',END, values=x )
        if id != '':
            dados = self.conexao.ver('d.id,d.nome,c.nome,d.nascimento,d.telefone,d.email','dados as d left outer join celula as c on c.id = d.celula',f'where d.id ={id} order by d.id')
            self.limpar_lista()
            for x in dados:
                self.resultado.insert('',END, values=x )
        if id in '' and celula in '' and nome in '' and email in '' and data in '' and telefone in '':
            self.select(delete=True, ver=True)
            self.texto_id()
            self.atualizar()

    def duploclick(self, event):
        self.limpar()
        self.resultado.selection()
        for n in self.resultado.selection():
            col1, col2, col3, col4, col5, col6 = self.resultado.item(n,'values')
            self.nome.insert(END,col2)
            self.celula.insert(END,col3)
            self.telefone.insert(END,col5)
            self.data.insert(END,col4)
            self.id.insert(END,col1)
            self.email.insert(END,col6)

    def apagar(self):
        ins_id,nome, celula,data,email,telefone= self.values_entrada()
        decisao= showinfo.askquestion(title='AVISO', message=f'TEM CERTEZA QUE DESEJA APAGAR ESSAS INFORMAÇÕES: \nId: {ins_id}\nNome: {nome}\nCelula: {celula}\nNascimento:{data}\nTelefone: {telefone}\nEmail: {email}')
        if decisao =='yes':
            self.conexao.deletar(ins_id)
            self.atualizar()
            self.select(delete=True,ver=True)
        else:
            pass

    def update(self):
        try:
            ins_id,nome, celula,data,email,telefone= self.values_entrada()
            decisao= showinfo.askquestion(title='AVISO', message=f'TEM CERTEZA QUE DESEJA ALTERAR ESSAS INFORMAÇÕES: \nId: {ins_id}\nNome: {nome}\nCelula: {celula}\nNascimento:{data}\nTelefone: {telefone}\nEmail: {email}')
            if decisao =='yes':
                try:
                    data = str(data)
                    if data in'':
                        res_data = True
                    else:
                        if data[2] == '/' and data[5] == '/' and len(data) == 10:
                            res_data =True
                        else:
                            showinfo.showerror(title='AVISO', message= 'ERRO!!\nDATA INVÁLIDA\nEXEMPLO:10/02/2003')
                            res_data =False
                except:
                    showinfo.showerror(title='AVISO', message= 'ERRO!!\nDATA INVÁLIDA\nEXEMPLO:10/02/2003')

                if res_data ==True:
                    if nome in '' and email in '' and telefone in '':
                        showinfo.showerror(title='AVISO', message= 'ERRO!!\n NOME, EMAIL E TELEFONE SÃO OBRIGATÓRIO')
                    elif email in '' and telefone in '':
                        showinfo.showerror(title='AVISO', message= 'ERRO!!\n EMAIL E TELEFONE SÃO OBRIGATÓRIO')
                    elif nome in '' and email in '':
                        showinfo.showerror(title='AVISO', message= 'ERRO!!\n NOME E EMAIL SÃO OBRIGATÓRIO')
                    elif nome in '' and telefone in '':
                        showinfo.showerror(title='AVISO', message= 'ERRO!!\n NOME E TELEFONE SÃO OBRIGATÓRIO')
                    elif nome in '':
                        showinfo.showerror(title='AVISO', message= 'ERRO!!\n NOME É OBRIGATÓRIO')
                    elif email in '' :
                        showinfo.showerror(title='AVISO', message= 'ERRO!!\n EMAIL É OBRIGATÓRIO')
                    elif telefone in '':
                        showinfo.showerror(title='AVISO', message= 'ERRO!!\n TELEFONE É OBRIGATÓRIO')
                    else:
                        try:
                            tel = str(telefone)
                            email = str(email)
                            res_email = False
                            for x in email:
                                if x in '@':
                                    res_email = True
                            if res_email==True:
                                if len(tel) ==11 or tel[0] =='(' and tel[3] ==')' and tel[4] ==' ' and tel[10] =='-' and len(tel) ==15:
                                    if len(tel) ==11:
                                        res_tel = f'({tel[0] + tel[1]}) {tel[2]}{tel[3] + tel[4] + tel[5] + tel[6]}-{tel[7] + tel[8] + tel[9] + tel[10]}'
                                    else:
                                        res_tel = tel
                                    if celula == '':
                                        celula ='1'
                                        self.conexao.alterar(nome,celula,email,res_tel,data,ins_id)
                                        self.select(delete=True,ver=True)
                                        self.atualizar()
                                    else:
                                        self.conexao.alterar(nome,celula,email,res_tel,data,ins_id)
                                        self.select(delete=True,ver=True)
                                        self.atualizar()
                                else:
                                    showinfo.showerror(title='AVISO', message= 'ERRO!!\nNÚMERO INVÁLIDO\nEXEMPLO: DDD + NUMERO\n71986481515 ou (71) 98648-1515')
                            else:
                                showinfo.showerror(title='AVISO', message= 'ERRO!!\nEMAIL INVÁLIDO\nEXEMPLO: exemploemail@hotmail.com')
                        except:
                            print('ERROR')
                else:
                    print('erro no res_data')
            else:
                print('erro no decisao')
        except:
            showinfo.showerror(title='AVISO', message= 'ERRO!!!!!\nNÃO ALTERE O ID.')

    def login(self, cadastro=False):
        self.tela_login = Toplevel()
        self.tela_login.title('Login')
        self.tela_login.geometry('300x300+600+250')
        self.tela_login.maxsize(300,300)
        self.tela_login.minsize(300,300)
        self.tela_login.iconbitmap(default='grafica\\ico.ico')
        self.tela_login.resizable(width=1, height=1)
        if cadastro == False:
            Label(self.tela_login, image=self.fundo_login).pack()
            self.entrar = Button(self.tela_login, bd=0,image=self.botao6, command=self.verificador)
            self.entrar.place(width=104, height=40, x=167, y=237)
        elif cadastro ==True:
            Label(self.tela_login, image=self.fundo_cadastro).pack()
            self.entrar = Button(self.tela_login, bd=0,image=self.botao6, command=self.inserir_cadastro)
            self.entrar.place(width=104, height=40, x=167, y=237)
        self.usuario = Entry(self.tela_login, bd=1, font=("calibre", 10), background='white', justify=LEFT, foreground='black')
        self.usuario.place(width=270, height=23, x= 13, y=122)
        self.senha = Entry(self.tela_login, bd=1, font=("calibre", 10), background='white', justify=LEFT, foreground='black', show='*')
        self.senha.place(width=270, height=23, x= 13, y=183)
        self.botao_voltar = Button(self.tela_login, bd=0,image=self.botao5, command= lambda: self.tela_login.destroy())
        self.botao_voltar.place(width=104, height=40, x=24, y=237)

    def verificador(self):
        conexao = Login()
        usuario,senha = conexao.entrar()
        usuario = str(usuario[0]).replace('(', '').replace(')', '').replace(',','').replace("'", "")
        senha = str(senha[0]).replace('(', '').replace(')', '').replace(',','').replace("'", "")
        tela_usuario = str(self.usuario.get())
        tela_senha = str(self.senha.get())
        if usuario in tela_usuario and senha in tela_senha:
            self.conectar(True)
        else:
            showinfo.showerror(title='ERRO', message= 'Usuário ou Senha inválida!\nTente novamente')
            self.login()

    def conectar(self, conexao=False):
        if conexao ==True:
            self.tela_login.destroy()
            self.verificacao = Label(self.root, text='Autorização: Conectado', justify=LEFT, background='white', foreground='green')
            self.verificacao.place(width=150, height=23, x=50, y=667)
            self.atualizar()
        else:
            self.verificacao = Button(self.root, text='Autorização: Desconectado', bd=0,justify=LEFT, background='white', foreground='red',command=lambda: self.login())
            self.verificacao.place(width=150, height=23, x=50, y=667)
            self.atualizar()
        self.valorvery = conexao
        if self.valorvery ==True:
            if self.valor_resultado =='ALTERAR':
                self.update()
            elif self.valor_resultado =='APAGAR':
                self.apagar()
            elif self.valor_resultado =='CADASTRO':
                self.login(True)

    def values_verificacao(self,resultado):
        self.valor_resultado = resultado
        if self.valorvery ==True:
            if resultado =='ALTERAR':
                self.update()
            elif resultado =='APAGAR':
                self.apagar()
            elif resultado =='CADASTRO':
                self.login(True)
            else:
                self.login()
        elif self.valorvery ==False:
            self.login()

    def sair(self):
        self.valorvery = False
        self.conectar(False)
        self.atualizar()

    def login_cadastro(self):
        if self.valorvery ==False:
            self.values_verificacao('CADASTRO')
        elif self.valorvery==True:
            self.login(True)

    def inserir_cadastro(self):
        usuario = str(self.usuario.get())
        senha = str(self.senha.get())
        login =Login()
        inserir = login.inserir(usuario,senha)
        if inserir == True:
            showinfo.showinfo(title='DADOS SALVOS', message= 'DADOS SALVOS COM SUCESSO')
            self.tela_login.destroy()
        if inserir == False:
            showinfo.showerror(title='ERRO', message= 'Usuário já existe!\nTente novamente')
            self.tela_login.destroy()
            self.login(True)

    def resultado_combox(self,nome):
        conexao = self.conexao.ver('id','celula',f'where nome="{nome}"')
        return conexao
    def resultado_combox_celula(self,nome):
        conexao = self.conexao.ver('id','dados',f'where nome="{nome}"')
        return conexao
    def ftela_celula(self):
        self.tela_celula = Toplevel()
        self.tela_celula.title('Cadastro de celula')
        self.tela_celula.geometry('300x500+640+170')
        self.tela_celula.maxsize(300,500)
        self.tela_celula.minsize(300,500)
        self.tela_celula.iconbitmap(default='grafica\\ico.ico')
        self.tela_celula.resizable(width=1, height=1)
        Label(self.tela_celula, image=self.cadastro_celula).pack()
        self.botao_voltar = Button(self.tela_celula, bd=0,image=self.botao5, command= lambda: self.tela_celula.destroy())
        self.botao_voltar.place(width=104, height=40, x=35, y=431)
        self.entrar = Button(self.tela_celula, bd=0,image=self.botao7, command= self.salvar_celula)
        self.entrar.place(width=104, height=40, x=167, y=431)
        self.texto_id('CELULA')
        self.nome_celula = Entry(self.tela_celula,bd=1, font=("calibre", 10), background='white', justify=LEFT, foreground='black')
        self.nome_celula.place(width=260, height=28, x= 21, y=87)
        self.endereco_celula = Entry(self.tela_celula,bd=1, font=("calibre", 10), background='white', justify=LEFT, foreground='black')
        self.endereco_celula.place(width=260, height=28, x= 21, y=151)
        self.observacao_celula = Text(self.tela_celula,bd=1, font=("calibre", 10))
        self.observacao_celula.place(width=262, height=120, x= 21, y=290)
        resultado = self.conexao.ver('nome','dados','order by nome')
        resultadotratado = []
        for c in resultado:
            c = str(c)
            resultadotratado.append(c.replace("_", " ").replace("(", "").replace(")", "").replace(",", "").replace("'", ""))
        self.lider_celula= ttk.Combobox(self.tela_celula, values=resultadotratado, justify=LEFT, background='white', foreground='black')
        self.lider_celula.place(width=260, height=28, x= 21, y=218)
    def values_ent_celula(self):
        self.values_nome_celula = self.nome_celula.get().upper()
        self.values_lider_celula = self.resultado_combox_celula(self.lider_celula.get())
        self.values_lider_celula = str(self.values_lider_celula)
        if self.values_lider_celula =='[]':
            self.values_lider_celula =''
        else:
            self.values_lider_celula = self.values_lider_celula.replace(',','').replace('(','').replace(')','').replace('[','').replace(']','').replace('{','').replace('}','')
        self.values_observacao_celula = self.observacao_celula.get('1.0',END).upper()
        self.values_endereco_celula = self.endereco_celula.get().upper()
        return self.values_nome_celula,self.values_lider_celula,self.values_observacao_celula, self.values_endereco_celula
    def salvar_celula(self):
        nome,lider,observacao,endereco = self.values_ent_celula()
        if nome in '' and lider in '' or nome in '' or lider in '':
            showinfo.showerror(title='AVISO', message= 'ERRO!!\n NOME E LIDER SÃO OBRIGATÓRIO')
        else:
            self.salvar_into(id =self.ver_id ,nome=nome,lider=lider,obeservacao=observacao,endereco=endereco,tabela=banco_celula)

    def barrademenu(self):
        self.barramenu =Menu(self.root)
        menuIrpara= Menu(self.barramenu, tearoff=0)
        menuLogin =Menu(self.barramenu, tearoff=0)
        menuIrpara.add_command(label="CADASTRO DE PESSOAS")
        menuIrpara.add_separator()
        menuIrpara.add_command(label="CADASTRO DE CELULAS",command=self.ftela_celula)
        menuIrpara.add_separator()
        menuIrpara.add_command(label="CADASTRO DE SENHAS", command=self.login_cadastro)
        menuLogin.add_cascade(label="ENTRAR", command=lambda: self.values_verificacao(None))
        menuLogin.add_separator()
        menuLogin.add_cascade(label="SAIR", command= self.sair)
        self.barramenu.add_cascade(label='.......')
        self.barramenu.add_cascade(label='LOGIN', menu=menuLogin)
        self.barramenu.add_cascade(label='CADASTRO', menu=menuIrpara)
        self.barramenu.add_cascade(label='BUSCAR')
        self.barramenu.add_cascade(label='SAIR', command= lambda: self.root.destroy())
        self.root.config(menu=self.barramenu)

    pass

def fmenu():
    root = Tk()
    menu = Janela(root,"BANCO DE DADOS","920x700+310+50","grafica\\ico.ico",920,700)
    Janela.run(menu)
    return menu.sairtela

fmenu()
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%{asctime}s %{nome}s %{levelname}s %{message}s',
#     filename='/teste.log',
#     filemode='w')