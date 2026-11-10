# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Crie uma API REST para gerenciar tarefas usando FastAPI. Você praticará a criação de rotas, validação de dados com modelos Pydantic, operações CRUD e respostas HTTP para recursos que não existem. A documentação interativa do FastAPI ajudará você a testar cada endpoint.

## 📝 Tarefas

### 🛠️ Criar a Aplicação e Consultar Tarefas

#### Descrição
Configure a aplicação FastAPI e crie endpoints para consultar todas as tarefas e uma tarefa específica pelo identificador.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI com o título `Task Tracker API`
- Implementar `GET /tasks` para retornar a lista de tarefas
- Implementar `GET /tasks/{task_id}` para retornar uma tarefa ou responder com HTTP 404 quando ela não existir


### 🛠️ Criar e Atualizar Tarefas

#### Descrição
Use modelos Pydantic para validar os dados enviados pelo cliente e implemente endpoints para adicionar tarefas e atualizar os campos informados.

#### Requisitos
O programa concluído deve:

- Definir modelos para criar, atualizar e representar tarefas, incluindo título, descrição, identificador e estado de conclusão
- Implementar `POST /tasks` para criar uma tarefa e retornar HTTP 201
- Implementar `PATCH /tasks/{task_id}` para atualizar os campos enviados sem apagar os demais e responder com HTTP 404 se a tarefa não existir


### 🛠️ Excluir e Testar Tarefas

#### Descrição
Complete as operações da API implementando a exclusão de tarefas e teste os endpoints usando a documentação interativa do FastAPI.

#### Requisitos
O programa concluído deve:

- Implementar `DELETE /tasks/{task_id}` para excluir uma tarefa existente
- Responder com HTTP 404 quando uma tarefa solicitada para exclusão não existir
- Iniciar a API com `uvicorn starter-code:app --reload` e testar as operações em `http://127.0.0.1:8000/docs`

## 🚀 Como Começar

Instale as dependências no ambiente Python:

```bash
python -m pip install fastapi uvicorn
```

Complete os TODOs em `starter-code.py`. Inicie o servidor a partir desta pasta com o comando acima. Os dados ficam em memória e serão reiniciados quando o servidor parar.
