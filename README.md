1. Por que usar IF NOT EXISTS na criação da tabela?
   O comando IF NOT EXISTS evita que ocorra um erro caso a tabela já exista no banco de dados, Ou seja, ele verifica se a tabela já está criada antes de tentar criar novamente.
2. Para que servem os comandos commit() e close()?
   Commit() serve para salvar mudanças enquanto o close() encerra a conexão com o banco de dados
3. Como este banco.py poderia ser aproveitado em outros projetos?
   O banco.py pode servir como base para qualquer projeto que use banco de dados SQLite. Como por exemplo em um sistema de cadastro de médicos, onde o banco de dados iria guardar as informações
   de cadastro deles.

Atividade dia 15 de outubro
o sistema é bem básico, com espaços digitáveis para inserir os dados básicos(CPF, Nome etc..)
Você pode adicionar, consultar(terminar a interação com o usuário selecionado), atualizar(atualizar os dados do usuario seleciobado) e excluir(excluir o usuário selecionado do banco de dados)
Tem uma função de busca onde você insere o nome do usuário que deseja encontra e se quer ver apenas usuários com mesmo nome ativos
