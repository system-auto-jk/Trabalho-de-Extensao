from tkinter import messagebox
from openpyxl import Workbook
import os

class Funcs:
    def LimparTela(self):
        self.entry_codigo.delete(0, 'end')
        self.entry_nome.delete(0, 'end')
        self.entry_numero.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.String_tipo_processo.set('Selecione o Tipo')
        self.entry_numero_processo.delete(0, 'end')
        self.String_tipo_status.set('Selecione o Status')
        self.String_vara.set('Selecione a Vara')
        self.entry_local_processo.delete(0, 'end')
        self.entry_observacao.delete(1.0, 'end')
        self.entry_data.delete(0, 'end')
        self.entry_nome.focus()

    def Variaveis(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.numero = self.entry_numero.get()
        self.email = self.entry_email.get()
        self.tipo_processo = self.String_tipo_processo.get()
        self.n_processo = self.entry_numero_processo.get()
        self.status = self.String_tipo_status.get()
        self.observacao = self.entry_observacao.get(1.0, 'end')
        self.local_processo = self.entry_local_processo.get()
        self.vara = self.String_vara.get()
        self.data1 = self.entry_data.get()

    def Exportar_Excel(self):
        if self.entry_nome.get() == '':
            messagebox.showwarning('Campo em branco', 'Escolha quem quer exportar')
        else:
            self.retorno_exportar = messagebox.askyesno('Exportar Cadastro', f'Deseja o cadastro de {self.entry_nome.get()} no excel?')
            if self.retorno_exportar == True:
                self.book = Workbook()
                self.info_excel = self.book.active
                self.info_excel.append(['ID', 'Nome', 'Numero', 'Email', 'Nº Processo', 'Local do Processo', 'Tipo do Processo', 'Status', 'Vara', 'Observação', 'Data'])
                self.info_excel.append([self.col1, self.col2, self.col3, self.col4, self.col5, self.col6, self.col7, self.col8, self.col9, self.col10, self.col11])
                
                self.book.save(f'{self.col2}.xlsx')
                os.startfile(f'{self.col2}.xlsx')
