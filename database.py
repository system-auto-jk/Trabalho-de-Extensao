import sqlite3

class Database:
    def conecta_db(self):
        self.conn = sqlite3.connect('clientes.db')
        self.cursor = self.conn.cursor()
        print('Banco de dados Criado')

    def desconecta_db(self):
        self.conn.close()
        print('Banco de dados desconectado')

    def montaTabelas(self):
        self.conecta_db()
        print('Conectando ao banco de dados')

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                            cod INTEGER PRIMARY KEY,
                            nome_cliente CHAR(40) NOT NULL,
                            telefone INTEGER(20),
                            email CHAR(40),
                            numero_processo CHAR(40),
                            local_processo CHAR(40),
                            tipo_processo CHAR(40),
                            status CHAR(40),
                            vara CHAR(40),
                            observacao CHAR(300),
                            data CHAR(20)
                            );
                        """)
        self.conn.commit()
        self.desconecta_db()
