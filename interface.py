from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import messagebox
import webbrowser
from database import Database
from functions import Funcs

class ProgramaAgenda(Funcs, Database):
    def __init__(self, root):
        self.root = root
        self.montaTabelas()
        self.tela()
        self.Frames_da_tela()
        self.Criar_botoes()
        self.Criar_Labels()
        self.Criar_Entrys()
        self.Criar_Lista_T_Processo()
        self.Adicionar_Menu()
        self.Lista_Frame2()
        self.Select_lista()
        self.root.mainloop()

    def tela(self):
        self.root.title('Agenda Advogada')
        self.root.geometry('1300x700')
        self.root.maxsize(width=1350, height=800)
        self.root.minsize(width=500, height=400)
        self.root.configure(background='#f4f4f4')

    def Frames_da_tela(self):
        # Frame de cadastro
        self.frame_1 = Frame(self.root, bg='#ffffff', bd=2, relief=SOLID, highlightbackground='#91B5A9', highlightthickness=2)
        self.frame_1.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.46)

        # Frames de Exibição da lista de clientes cadastrados
        self.frame_2 = Frame(self.root, bg='#ffffff', bd=2, relief=SOLID, highlightbackground='#91B5A9', highlightthickness=2)
        self.frame_2.place(relx=0.01, rely=0.54, relwidth=0.98, relheight=0.4)

        # Titulo - Cadastro
        self.frame_3 = Frame(self.root, bg='#91B5A9', bd=2, relief=SOLID)
        self.frame_3.place(relx=0.01, rely=0.023, relwidth=0.98, relheight=0.05)

        # Titulo = Lista de Clientes
        self.frame_4 = Frame(self.root, bg='#91B5A9', bd=2, relief=SOLID)
        self.frame_4.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.05)

    def Criar_botoes(self):
        button_style = {
            'bd': 2,
            'relief': SOLID,
            'font': 'Arial 11 bold',
            'bg': '#91B5A9',  # Azul escuro
            'fg': 'Black',
            'padx': 10,
            'pady': 5,
            'highlightthickness': 1,
            'highlightbackground': '#004d40'  # Verde escuro
        }
        
        self.botão_limpar = Button(self.frame_1, text='Limpar', **button_style, command=self.LimparTela)
        self.botão_limpar.place(relx=0.05, rely=0.8, relheight=0.1, relwidth=0.14)

        self.botão_buscar = Button(self.frame_1, text='Buscar', **button_style, command=self.Busca_Cliente)
        self.botão_buscar.place(relx=0.2, rely=0.8, relheight=0.1, relwidth=0.14)

        self.botão_exportar = Button(self.frame_1, text='Exportar', **button_style, command=self.Exportar_Excel)
        self.botão_exportar.place(relx=0.35, rely=0.8, relheight=0.1, relwidth=0.14)

        self.botão_novo = Button(self.frame_1, text='Cadastrar', font='Arial 12 bold', bg='#91B5A9', fg='Black', bd = 3, relief=SOLID,command=self.Add_cliente)
        self.botão_novo.place(relx=0.5, rely=0.8, relheight=0.1, relwidth=0.14)

        self.botão_alterar = Button(self.frame_1, text='Alterar', **button_style, command=self.Alterar_cliente)
        self.botão_alterar.place(relx=0.65, rely=0.8, relheight=0.1, relwidth=0.14)

        self.botão_apagar = Button(self.frame_1, text='Apagar', **button_style, command=self.Deleta_cliente)
        self.botão_apagar.place(relx=0.8, rely=0.8, relheight=0.1, relwidth=0.14)

        self.botão_calendario = Button(self.frame_1, text='📆', font='Arial', bg='#91B5A9', fg='white', command=self.Calendario)
        self.botão_calendario.place(relx=0.895, rely=0.23, relheight=0.06, relwidth=0.02)

        # Criar as labels  / Configuração de Labels
    def Criar_Labels(self):
        label_style = {
            'bg': '#ffffff',
            'fg': '#333333',
            'font': 'Arial 11 bold'
        }
        
        self.label_codigo = Label(self.frame_1, text='ID', **label_style)
        self.label_codigo.place(relx=0.02, rely=0.14, relheight=0.1, relwidth=0.06)

        self.label_nome = Label(self.frame_1, text='Nome', **label_style)
        self.label_nome.place(relx=0.12, rely=0.14, relheight=0.1, relwidth=0.1)

        self.label_numero = Label(self.frame_1, text='Número', **label_style)
        self.label_numero.place(relx=0.24, rely=0.14, relheight=0.1, relwidth=0.12)

        self.label_email = Label(self.frame_1, text='Email', **label_style)
        self.label_email.place(relx=0.33, rely=0.14, relheight=0.1, relwidth=0.2)

        self.label_numero_processo = Label(self.frame_1, text='Nº Processo', **label_style)
        self.label_numero_processo.place(relx=0.53, rely=0.14, relheight=0.1, relwidth=0.12)

        self.label_local_processo = Label(self.frame_1, text='Local do Processo', **label_style)
        self.label_local_processo.place(relx=0.65, rely=0.14, relheight=0.1, relwidth=0.16)

        self.label_tipo_de_processo = Label(self.frame_1, text='Tipo Processo', **label_style)
        self.label_tipo_de_processo.place(relx=0.027, rely=0.35, relheight=0.1, relwidth=0.12)

        self.label_status = Label(self.frame_1, text='Status', **label_style)
        self.label_status.place(relx=0.225, rely=0.35, relheight=0.1, relwidth=0.12)

        self.label_vara = Label(self.frame_1, text='Vara', **label_style)
        self.label_vara.place(relx=0.46, rely=0.35, relheight=0.1, relwidth=0.12)

        self.label_observacao = Label(self.frame_1, text='Observação', **label_style)
        self.label_observacao.place(relx=0.69, rely=0.35, relheight=0.1, relwidth=0.15)

        self.label_data = Label(self.frame_1, text='Data', **label_style)
        self.label_data.place(relx=0.815, rely=0.14, relheight=0.1, relwidth=0.07)

        self.label_titulo_cadastro = Label(self.frame_3, text='CADASTRO', fg='Black', bg='#91B5A9', font='Arial 15 bold')
        self.label_titulo_cadastro.pack(anchor='center')

        self.label_titulo_lista_cli = Label(self.frame_4, text='LISTA DE CLIENTES', fg='Black', bg='#91B5A9' ,font='Arial 15 bold')
        self.label_titulo_lista_cli.pack(anchor='center')

        # Criar as Entrys / Configuração das Entrys
    def Criar_Entrys(self):
        entry_style = {
            'font': 'Arial 11',
            'bg': '#f0f0f0',
            'bd': 0,
            'highlightthickness': 1,
            'highlightbackground': '#91B5A9'  # Azul escuro
        }

        self.entry_codigo = Entry(self.frame_1, **entry_style)
        self.entry_codigo.place(relx=0.02, rely=0.23, relheight=0.07, relwidth=0.06)

        self.entry_nome = Entry(self.frame_1, **entry_style)
        self.entry_nome.place(relx=0.1, rely=0.23, relheight=0.07, relwidth=0.13)

        self.entry_numero = Entry(self.frame_1, **entry_style)
        self.entry_numero.place(relx=0.25, rely=0.23, relheight=0.07, relwidth=0.1)

        self.entry_email = Entry(self.frame_1, **entry_style)
        self.entry_email.place(relx=0.37, rely=0.23, relheight=0.07, relwidth=0.13)

        self.entry_numero_processo = Entry(self.frame_1, **entry_style)
        self.entry_numero_processo.place(relx=0.52, rely=0.23, relheight=0.07, relwidth=0.14)

        self.entry_local_processo = Entry(self.frame_1, **entry_style)
        self.entry_local_processo.place(relx=0.68, rely=0.23, relheight=0.07, relwidth=0.1)

        self.entry_observacao = Text(self.frame_1, font='Arial 10', bg='#f0f0f0', bd=0, highlightthickness=1, highlightbackground='#91B5A9')
        self.entry_observacao.place(relx=0.65, rely=0.45, relheight=0.16, relwidth=0.25)

        self.entry_data = Entry(self.frame_1, **entry_style)
        self.entry_data.place(relx=0.81, rely=0.23, relheight=0.07, relwidth=0.08)
        
        # Cria a lista com alguma opções predefinidas para o cadastro
    def Criar_Lista_T_Processo(self):
        self.String_tipo_processo = StringVar(self.frame_1)
        Lista_StringVar_processo = ('Conhecimento','Cautelar','Execução')
        self.String_tipo_processo.set('Selecione o Tipo')

        self.menu_tipo_processo = OptionMenu (self.frame_1, self.String_tipo_processo, *Lista_StringVar_processo)
        self.menu_tipo_processo.place(relx=0.02, rely=0.45, relheight=0.12,relwidth=0.13)

        self.String_tipo_status = StringVar(self.frame_1)
        Lista_String_status = ('FINALIZADO  ','FINALIZADO - SUBSTITUIÇÃO','PENDENTE ASSISTENTE SOSCIAL','PENDENTE - ASSISTIDO (REPONSÁVEL) ERIC'
                               ,'PENDENTE - ASSISTIDO (REPONSÁVEL) MARIA EDUARDA','PENDENTE - DEFENSOR PUBLICO','PENDENTE - ERIC','PENDENTE -  MARIA EDUARDA','PENDENTE - JUDICIÁRIO'
                               ,'PENDENTE - NÚCLEO DE CONCILIAÇÃO','PENDENTE - OUTROS','PENDENTE - TRIAGEM','OUTROS','NÃO SE APLICA','PENDENTE - GREVE')
        self.String_tipo_status.set('Selecione o Status')

        menu_tipo_status = OptionMenu (self.frame_1, self.String_tipo_status, *Lista_String_status)
        menu_tipo_status.place(relx=0.16, rely=0.45, relheight=0.12,relwidth=0.26)

        self.String_vara = StringVar(self.frame_1)
        Lista_String_vara = ('1ª FAMÍLIA','2ª FAMÍLIA','3ª FAMÍLIA' ,'4ª FAMÍLIA','5ª FAMÍLIA','6ª FAMÍLIA' ,'7ª FAMÍLIA'
                             ,'8ª FAMÍLIA','9ª FAMÍLIA','10ª FAMÍLIA','1º SUCESSÕES','2º SUCESSÕES','3º SUCESSÕES','4º SUCESSÕES'
                             ,'CEJUSC','VARA DE OUTRA COMARCA DA BAHIA','VARA DE OUTRO ESTADO','TRIBUNAL DE JUSTIÇA','VARA FEDERAL'
                             ,'OUTROS','NÃO SE APLICA')
        self.String_vara.set('Selecione a Vara')

        menu_vara = OptionMenu (self.frame_1, self.String_vara, *Lista_String_vara)
        menu_vara.place(relx=0.43, rely=0.45, relheight=0.12,relwidth=0.2)

    def Adicionar_Menu(self):
        meuMenu = Menu(self.root)
        fileMenu = Menu(meuMenu, tearoff=0)
        fileMenu.add_command(label='Limpar', command=self.LimparTela)
        fileMenu.add_command(label='Suporte', command=lambda: webbrowser.open('https://www.instagram.com/systemautojk/'))
        fileMenu.add_command(label='Sair', command=self.root.destroy)
        meuMenu.add_cascade(label='Opções', menu=fileMenu)
        self.root.config(menu=meuMenu)

    def Lista_Frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=('self.col1','col2','self.col3','self.col4','self.col5', 'self.col6','self.col7', 'self.col8','self.col9','self.col10','self.col11'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='ID')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Email')
        self.listaCli.heading('#5', text='Nº/Processo')
        self.listaCli.heading('#6', text='L Processo')
        self.listaCli.heading('#7', text='T/Processo')
        self.listaCli.heading('#8', text='Status')
        self.listaCli.heading('#9', text='Vara')
        self.listaCli.heading('#10', text='Observação')
        self.listaCli.heading('#11', text='Data')
        self.listaCli.column('#0', width='1')
        self.listaCli.column('#1', width='30')
        self.listaCli.column('#2', width='130')
        self.listaCli.column('#3', width='30')
        self.listaCli.column('#4', width='40')
        self.listaCli.column('#5', width='30')
        self.listaCli.column('#6', width='50')
        self.listaCli.column('#7', width='40')
        self.listaCli.column('#8', width='30')
        self.listaCli.column('#9', width='40')
        self.listaCli.column('#10', width='30')
        self.listaCli.column('#11', width='30')

        self.listaCli.place(relx=0.01, rely=0.07, relheight=0.85, relwidth=0.96)
        self.scrollLista =Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollc=self.scrollLista.set)
        self.scrollLista.place(relx=0.97,rely=0.07, relheight=0.85, relwidth=0.02)

        self.listaCli.bind('<Double-1>', self.OnDoubleClick)
    

    def Select_lista(self):
        
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, email, numero_processo, local_processo, tipo_processo, status, vara, observacao, data FROM clientes
                                    ORDER BY nome_cliente ASC; """)

        for i in lista:
            self.listaCli.insert("",END, values=i)
        self.desconecta_db()

        # Função que acontece ao clicar duas vezes em alguem da lista, ele mostra as informações de quem vc clicou.

    def OnDoubleClick(self, event):
        self.LimparTela()
        self.listaCli.selection()
        for n in self.listaCli.selection():
            self.col1, self.col2, self.col3, self.col4, self.col5, self.col6, self.col7, self.col8, self.col9, self.col10, self.col11 = self.listaCli.item(n, 'values')
            
            self.entry_codigo.insert(END, self.col1)
            self.entry_nome.insert(END, self.col2)
            self.entry_numero.insert(END, self.col3)
            self.entry_email.insert(END, self.col4)
            self.entry_numero_processo.insert(END, self.col5)
            self.entry_local_processo.insert(END, self.col6)
            self.String_tipo_processo.set(self.col7)
            self.String_tipo_status.set(self.col8)
            self.String_vara.set(self.col9)
            self.entry_observacao.insert(END, self.col10)
            self.entry_data.insert(END, self.col11)

    def Add_cliente(self):
        self.Variaveis()
        if self.entry_nome.get() == '':
            messagebox.showwarning('Campo em branco','O campo nome está em branco')
        else:
            self.retorno = messagebox.askyesno('Cadastro',f'Concluir Cadastro de {self.entry_nome.get()}')
            if self.retorno == True:
                self.conecta_db()
                self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, email, numero_processo, local_processo, tipo_processo, status, vara, observacao , data)
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",(self.nome, self.numero, self.email , self.n_processo, self.local_processo, self.tipo_processo , self.status, self.vara, self.observacao, self.data1))
                self.conn.commit()
                self.desconecta_db()
                self.Select_lista()
                self.LimparTela()
                messagebox.showinfo('Cadastro Concluído',f'Cadastro de {self.nome} conclído')
            else:
                messagebox.showerror('Cadastro Cancelado','Cadastro Cancelado')

    def Deleta_cliente(self):
        self.Variaveis()
        if self.entry_nome.get() == '':
            messagebox.showwarning('Campo em branco','Escolha quem quer deletar')
        else:
            self.retorno_apagar= messagebox.askyesno('Deletar Cadastro',f'Tem certeza que deseja deletar {self.entry_nome.get()}')
            if self.retorno_apagar == True:
                self.conecta_db()
                self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""", [self.codigo])
                self.conn.commit()  

                self.desconecta_db()
                self.LimparTela()
                self.Select_lista()
                messagebox.showinfo('Cadastro Deletado','Cadastro Deletado')
            else:
                messagebox.showerror('Deletar Cadastro','Cancelado')

    def Alterar_cliente(self):
        self.Variaveis()
        if self.entry_nome.get() == '':
            messagebox.showwarning('Campo em branco','Escolha quem quer alterar')
        else:
            self.retorno_alterar = messagebox.askyesno('Alterar Cadastro',f'Tem certeza que quer alterar o cadastro de {self.col2}')
            if self.retorno_alterar == True:
                self.conecta_db()
                self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, email = ?, numero_processo = ?, local_processo = ?, tipo_processo = ?, status = ?, vara = ?, observacao = ?, data = ?
                                    WHERE cod = ?""", (self.nome, self.numero, self.email, self.n_processo,  self.local_processo, self.tipo_processo, self.status, self.vara ,self.observacao, self.data1,self.codigo))
                self.conn.commit()
                self.desconecta_db()
                self.Select_lista()
                self.LimparTela()
                messagebox.showinfo('Alteração Concluída',f'Alteração de {self.col2} Concluída')
            else:
                messagebox.showerror('Alteração Cancelada','Alteração Cancelada')

    def Calendario(self):
        self.calendario1 = Calendar(self.frame_1, fg='black',font='Arial 10 bold', locale='pt_br')
        self.calendario1.place(relx=0.75, rely=0.3)

        self.calData = Button(self.frame_1, text='Inserir Data', command=self.Print_cal)
        self.calData.place(relx=0.78, rely=0.92, height=25, width=100)

        self.calData_cancel = Button(self.frame_1, text='Cancelar', command=self.Cancel_calendario)
        self.calData_cancel.place(relx=0.86, rely=0.92, height=25, width=100)

    def Print_cal(self):
        dataIni = self.calendario1.get_date()
        self.calData.destroy()
        self.calendario1.destroy()
        self.entry_data.delete(0, END)
        self.entry_data.insert(END, dataIni)
        self.calData_cancel.destroy()
        
        # Cancelar o calendário.
    def Cancel_calendario(self):
        self.calData.destroy()
        self.calendario1.destroy()
        self.calData_cancel.destroy()

        # Buscar o cliente por qualquer tipó de informação.
    def Busca_Cliente(self):
        self.conecta_db()
        self.listaCli.delete(*self.listaCli.get_children())
        
        filtros = []
        valores = []
        
        if self.entry_nome.get():
            filtros.append("nome_cliente LIKE ?")
            valores.append(self.entry_nome.get() + '%')
        
        if self.entry_numero.get():
            filtros.append("telefone LIKE ?")
            valores.append(self.entry_numero.get() + '%')
        
        if self.entry_codigo.get():
            filtros.append("cod LIKE ?")
            valores.append(self.entry_codigo.get() + '%')
        
        if self.entry_email.get():
            filtros.append("email LIKE ?")
            valores.append(self.entry_email.get() + '%')
        
        if self.entry_numero_processo.get():
            filtros.append("numero_processo LIKE ?")
            valores.append(self.entry_numero_processo.get() + '%')
        
        if self.entry_local_processo.get():
            filtros.append("local_processo LIKE ?")
            valores.append(self.entry_local_processo.get() + '%')
        
        if self.String_tipo_processo.get() != 'Selecione o Tipo':
            filtros.append("tipo_processo LIKE ?")
            valores.append(self.String_tipo_processo.get() + '%')
        
        if self.String_tipo_status.get() != 'Selecione o Status':
            filtros.append("status LIKE ?")
            valores.append(self.String_tipo_status.get() + '%')
        
        if self.String_vara.get() != 'Selecione a Vara':
            filtros.append("vara LIKE ?")
            valores.append(self.String_vara.get() + '%')
        
        if self.entry_data.get():
            filtros.append("data LIKE ?")
            valores.append(self.entry_data.get() + '%')
        
        query = "SELECT cod, nome_cliente, telefone, email, numero_processo, local_processo, tipo_processo, status, vara, observacao, data FROM clientes"
        
        if filtros:
            query += " WHERE " + " AND ".join(filtros)
        
        query += " ORDER BY nome_cliente ASC"
        
        self.cursor.execute(query, valores)
        
        buscaNomeCli = self.cursor.fetchall()
        for i in buscaNomeCli:
            self.listaCli.insert("", END, values=i)
        
        self.LimparTela()
        self.desconecta_db()
        
        # Criar um excel com nome e dados do cliente selecionado.
