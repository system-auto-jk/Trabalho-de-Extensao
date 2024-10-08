# Agenda de Contatos para Escritório de Advocacia

Este é um sistema de agenda desenvolvido para gerenciar contatos e processos de um escritório de advocacia. O programa foi construído em Python utilizando a biblioteca Tkinter para a interface gráfica e SQLite para o banco de dados. O sistema permite o cadastro, visualização, alteração e exclusão de clientes e seus respectivos processos, além de outras funcionalidades, como exportação de dados para Excel.

## Estrutura do Projeto

```bash
/agenda_advogada
│
├── main.py           # Arquivo principal que inicia a aplicação
├── database.py       # Contém funções relacionadas ao banco de dados
├── interface.py      # Contém a interface gráfica e interações do usuário
└── functions.py      # Contém funções auxiliares para manipulação de dados e outras utilidades
```

## Funcionalidades

- **Cadastro de Clientes:** Permite adicionar novos clientes ao banco de dados.
- **Gerenciamento de Processos:** Associa processos jurídicos aos clientes cadastrados.
- **Busca de Clientes:** Pesquisa clientes por nome, código, número, email, número do processo, local do processo, data, tipo do processo, status ou vara.
- **Exportação para Excel:** Exporta os dados dos clientes para um arquivo Excel.
- **Interface Gráfica:** UI intuitiva usando Tkinter com menus, botões, entradas e lista de exibição.
- **Calendário:** Escolha de datas usando um calendário integrado.
- **Limpeza da Tela:** Limpa os campos de entrada e outras informações exibidas.
- **Alteração de Cadastro:** Permite atualizar as informações de um cliente existente.
- **Exclusão de Cadastro:** Permite remover um cliente do banco de dados.

## Instalação

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/SeuUsuario/agenda_advogada.git
   cd agenda_advogada
   ```

2. **Instale as Dependências:**

   Certifique-se de ter o Python instalado. Em seguida, instale as dependências necessárias:

   ```bash
   pip install tkcalendar openpyxl
   ```

3. **Execute o Programa:**

   ```bash
   python main.py
   ```

## Uso

1. **Cadastro de Cliente:**
   - Preencha os campos necessários e clique no botão "Adicionar".
   - O cliente será salvo no banco de dados SQLite.

2. **Busca de Cliente:**
   - Utilize a função de busca para encontrar clientes específicos.
   - A lista exibirá os resultados da pesquisa.

3. **Alteração de Cadastro:**
   - Selecione um cliente na lista.
   - Edite os campos necessários e clique no botão "Alterar" para atualizar as informações no banco de dados.

4. **Exclusão de Cadastro:**
   - Selecione um cliente na lista e clique no botão "Excluir".
   - O cliente será removido do banco de dados.

5. **Limpeza da Tela:**
   - Clique no botão "Limpar" para apagar os dados dos campos de entrada e limpar a visualização de dados.

6. **Exportação para Excel:**
   - Selecione um cliente na lista e escolha a opção de exportar para Excel.

7. **Suporte:**
   - Acesse o menu "Opções" e selecione "Suporte" para obter ajuda.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas:
  - `tkinter`
  - `tkcalendar`
  - `openpyxl`
  - `webbrowser`

## Contribuição

O desenvolvimento deste programa contou com a valiosa contribuição dos usuários do escritório de advocacia, que forneceram feedback e sugestões para melhorar a funcionalidade e usabilidade da aplicação.

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues.

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Desenvolvido por Erick e [System Auto JK - Soluções Tecnológicas](https://www.instagram.com/systemautojk/). Para dúvidas ou suporte, entre em contato através das nossas redes sociais.