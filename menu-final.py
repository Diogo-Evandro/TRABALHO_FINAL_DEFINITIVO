from tkinter import *
from tkinter import ttk
import tkinter as tk

num = 0

root = Tk()
class menu():
    def __init__(self):
        self.root = root
        self.tela()
        # self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()
    def tela(self):
        self.root.title("Final")
        self.root.configure(background= '#0074eb')
        self.root.geometry("400x100")
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height= 700)
        self.root.minsize(width= 500, height= 400)
    # def frames_da_tela(self):
    #     self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 3)
    #     self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)
        
    #     self.frame_2 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground = '#759fe6', highlightthickness = 3)
    #     self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)
    def widgets_frame1(self):
        ### criação do botão limpar
        self.bt_clientes = Button(text="Clientes", bd=3, bg='#107db2', fg='white', font= ('Verdana', 10, 'bold'), command = import_clientes)
        self.bt_clientes.place(relx= 0, rely= 0.4, relwidth=1, relheight=0.2)
        ### criação do botão buscar
        self.bt_funcionarios = Button(text="Funcionarios", bd=3, bg='#107db2', fg='white', font= ('Verdana', 10, 'bold'), command = import_funcionarios)
        self.bt_funcionarios.place(relx= 0, rely= 0.6, relwidth=1, relheight=0.2)
        ### criação do botão novo
        self.bt_fornecedores = Button(text="Fornecedores", bd=3, bg='#107db2', fg='white', font= ('Verdana', 10, 'bold'), command = import_fornecedores)
        self.bt_fornecedores.place(relx= 0, rely= 0.8, relwidth=1, relheight=0.2)
def import_funcionarios():
    if num <= 0:
        import final_funcionarios
        num + 1
    else:
        final_funcionarios.Application()

def import_clientes():
    if num <= 0:
        import final_cliente
        num + 1
    else:
        final_cliente.Application()
    
def import_fornecedores():
    if num <= 0:
        import final_fornecedores
        num + 1
    else:
        final_fornecedores.Application()   
    
menu()