import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector




clientes = Tk()



class funcs():
    def clean_tela(self):
        self.bi_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.morada_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = mysql.connector.connect(host='localhost', database='vooware', user='root', password='#asisBD12')
        self.cursor = self.conn.cursor()
    def desconecta_db(self):
        self.conn.close()
    def variaveis(self):
        self.bi = self.bi_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.morada = self.morada_entry.get()                                   
    def new_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.clean_tela()
        dados = " INSERT INTO clientes (bi, nome, telefone, morada) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(dados, (self.bi, self.nome, self.telefone, self.morada))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        self.cursor.execute(" SELECT bi, nome, telefone, morada FROM clientes ORDER BY nome ASC; ")
        lista =  self.cursor.fetchall()
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_db()
    def ondoubleclik(self, event):
        self.clean_tela()
        self.listaCli.selection()
        print(self)
        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.bi_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.morada_entry.insert(END, col4)
    def delete_cliente(self):
        self.variaveis()
        self.conecta_bd() 
        print(self.bi)
        dados2 = "DELETE FROM clientes WHERE bi = {}" .format(self.bi)
        self.cursor.execute(dados2)
        self.conn.commit()
        self.desconecta_db()
        self.clean_tela()
        self.select_lista()
    def alter_cliente(self):
        self.variaveis()
        self.conecta_bd()
        dados = "UPDATE clientes SET bi = %s, nome = %s, telefone = %s, morada = %s"
        self.cursor.execute( dados, (self.bi, self.nome, self.telefone, self.morada))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.clean_tela()
    def search_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())
        self.bi_entry.insert(END, '%')
        bi = self.bi_entry.get()
        self.cursor.execute("""SELECT bi, nome, telefone, morada FROM clientes WHERE bi LIKE '%s' ORDER BY bi ASC""" % bi)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", END, values=i)
        self.clean_tela()
        self.desconecta_db()
        
        
        
class application(funcs):

    def __init__(self):
        self.clientes = clientes
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.select_lista()
        clientes.mainloop()
    def tela(self):
        self.clientes.title("CLIENTES")
        self.clientes.configure(background= '#1e3743')
        self.clientes.geometry("800x600")
        self.clientes.resizable(True, True)
        self.clientes.maxsize(width= 1000, height= 800)
        self.clientes.minsize(width= 400, height= 300)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.clientes, bd = 4, bg = '#dfe3ee',
                             highlightbackground= '#759fe6', highlightthickness= 3)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.clientes, bd = 4, bg = '#dfe3ee',
                             highlightbackground= '#759fe6', highlightthickness= 3)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)
    def widgets_frame1(self):
        ### criação do botão CLEAN
        self.bt_clean = Button(self.frame_1, text= "CLEAN", bd= 2, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'), command= self.clean_tela)
        self.bt_clean.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        ### criação do botão SEARCH
        self.bt_search = Button(self.frame_1, text= "SEARCH", bd= 2, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'), command= self.search_cliente)
        self.bt_search.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)

         ### criação do botão NEW
        self.bt_new = Button(self.frame_1, text= "NEW", bd= 2, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'), command= self.new_cliente)
        self.bt_new.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        ### criação do botão ALTER
        self.bt_alter = Button(self.frame_1, text= "ALTER", bd= 2, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'), command= self.alter_cliente)
        self.bt_alter.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        
        ### criação do botão DELETE
        self.bt_delete = Button(self.frame_1, text= "DELETE", bd= 2, bg= '#107db2', fg= 'white', font= ('verdana', 8, 'bold'), command= self.delete_cliente)
        self.bt_delete.place(relx= 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.15)


        
        
        ### criação da label e entrada do bi
        self.lb_bi = Label(self.frame_1, text= "BI", bg = '#dfe3ee', fg= '#107db2')
        self.lb_bi.place(relx= 0.05, rely= 0.05) 

        self.bi_entry = Entry(self.frame_1)
        self.bi_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08)

         ### criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text= "Nome", bg = '#dfe3ee', fg= '#107db2')
        self.lb_nome.place(relx= 0.05, rely= 0.35) 

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.05, rely= 0.45, relwidth= 0.8)

        ### criação da label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text= "Telefone", bg = '#dfe3ee', fg= '#107db2')
        self.lb_telefone.place(relx= 0.05, rely= 0.6) 

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx= 0.05, rely= 0.7, relwidth= 0.4)

        ### criação da label e entrada da morada
        self.lb_morada = Label(self.frame_1, text= "Morada", bg = '#dfe3ee', fg= '#107db2')
        self.lb_morada.place(relx= 0.5, rely= 0.6) 

        self.morada_entry = Entry(self.frame_1)
        self.morada_entry.place(relx= 0.5, rely= 0.7, relwidth= 0.4)
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, columns=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="bi")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Morada")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        ### Criando a barra de rolagem

        self.scroollista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroollista.set)
        self.scroollista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.ondoubleclik)


application()
