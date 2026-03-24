
# API CRUD - Inventário de Jogos

Este projeto é uma API REST desenvolvida com **Flask** e **SQLite** para gerenciar um **inventário de jogos**.

## Tema
O sistema permite cadastrar, listar, buscar, atualizar e remover jogos de um inventário.

Cada jogo possui os seguintes campos:
- `id`
- `titulo`
- `genero`
- `plataforma`
- `ano_lancamento`
- `quantidade`

---

## Estrutura do projeto

```bash
crud_api_jogos/
│-- app.py
│-- init_db.py
│-- jogos.db   # criado após executar o script de inicialização
│-- requirements.txt
│-- README.md
```

---

## Requisitos

- Python 3
- pip

---

## Instalação

### 1. Clone o repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd crud_api_jogos
```

### 2. Crie o ambiente virtual (opcional, mas recomendado)

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

No Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicialize o banco de dados

```bash
python init_db.py
```

### 5. Execute a aplicação

```bash
python app.py
```

A API ficará disponível em:

```bash
http://127.0.0.1:5000
```

---

## Endpoints

### GET - Listar todos os jogos

```http
GET /jogos
```

### GET - Buscar jogo por ID

```http
GET /jogos/<id>
```

### POST - Inserir novo jogo

```http
POST /jogos
```

### PUT - Atualizar jogo existente

```http
PUT /jogos/<id>
```

### DELETE - Remover jogo

```http
DELETE /jogos/<id>
```

---

## Roteiro de testes com cURL

### 1. Inserir um jogo

No Windows CMD:

```bash
curl -X POST http://127.0.0.1:5000/jogos -H "Content-Type: application/json" -d "{\"titulo\":\"The Witcher 3\",\"genero\":\"RPG\",\"plataforma\":\"PC\",\"ano_lancamento\":2015,\"quantidade\":10}"
```

No PowerShell:

```bash
curl -X POST http://127.0.0.1:5000/jogos -H 'Content-Type: application/json' -d '{"titulo":"The Witcher 3","genero":"RPG","plataforma":"PC","ano_lancamento":2015,"quantidade":10}'
```

---

### 2. Listar todos os jogos

```bash
curl http://127.0.0.1:5000/jogos
```

---

### 3. Buscar um jogo por ID

```bash
curl http://127.0.0.1:5000/jogos/1
```

---

### 4. Atualizar um jogo

No Windows CMD:

```bash
curl -X PUT http://127.0.0.1:5000/jogos/1 -H "Content-Type: application/json" -d "{\"titulo\":\"The Witcher 3: Wild Hunt\",\"genero\":\"RPG\",\"plataforma\":\"PC\",\"ano_lancamento\":2015,\"quantidade\":8}"
```

No PowerShell:

```bash
curl -X PUT http://127.0.0.1:5000/jogos/1 -H 'Content-Type: application/json' -d '{"titulo":"The Witcher 3: Wild Hunt","genero":"RPG","plataforma":"PC","ano_lancamento":2015,"quantidade":8}'
```

---

### 5. Remover um jogo

```bash
curl -X DELETE http://127.0.0.1:5000/jogos/1
```

---

### 6. Testar erro 404 ao buscar ID inexistente

```bash
curl http://127.0.0.1:5000/jogos/999
```

---

## Exemplo de retorno JSON

### GET /jogos

```json
[
  {
    "id": 1,
    "titulo": "The Witcher 3",
    "genero": "RPG",
    "plataforma": "PC",
    "ano_lancamento": 2015,
    "quantidade": 10
  }
]
```

### GET /jogos/999

```json
{
  "erro": "Jogo não encontrado"
}
```

---

## Observações

- O banco utilizado é o **SQLite**.
- O arquivo `init_db.py` é responsável por criar o banco `.db` e a tabela necessária.
- O projeto segue padrão REST com respostas em JSON.
- O endpoint `PUT` retorna **204 No Content** em caso de atualização com sucesso.
- O endpoint `DELETE` retorna **204 No Content** em caso de exclusão com sucesso.

---

## Sugestão de envio

1. Criar um repositório no GitHub.
2. Enviar os arquivos do projeto.
3. Confirmar que o `README.md` contém as instruções de execução e testes.
