# 📘 Assignment: Reading List with SQLite

## 🎯 Objective

Crie um catálogo de livros em Python que salva informações em um banco SQLite. Você vai praticar tabelas, consultas SQL e as operações básicas de criar, ler, atualizar e excluir registros.

## 📝 Tasks

### 🛠️ Create and Read Book Records

#### Descrição
Use o arquivo `starter-code.py` para criar uma tabela `books` no banco `reading_list.db`. Complete as funções para adicionar livros e exibir os livros salvos.

#### Requisitos
O programa concluído deve:

- Criar uma tabela `books` com `id`, `title` e `author`; o `id` deve ser uma chave primária
- Permitir adicionar um livro informando título e autor
- Exibir todos os livros com seus IDs, títulos e autores
- Inserir pelo menos três livros e confirmar que eles continuam salvos após fechar e executar o programa novamente
- Usar consultas parametrizadas com `?` para inserir valores

### 🛠️ Manage the Reading List

#### Descrição
Crie um menu no terminal para gerenciar os livros. O menu deve continuar funcionando até que a pessoa escolha sair.

#### Requisitos
O programa concluído deve:

- Oferecer opções para adicionar, listar, atualizar e excluir livros
- Atualizar o título e o autor de um livro escolhido pelo ID
- Excluir um livro escolhido pelo ID
- Usar consultas parametrizadas com `?` em todas as operações que recebem dados da pessoa usuária
- Mostrar uma mensagem clara quando o ID informado não corresponder a um livro
- Fechar cada conexão com o banco após concluir a operação