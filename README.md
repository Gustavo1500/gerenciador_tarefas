Um **gerenciador de tarefas CLI**, escrito em Python3. Utiliza *Argsparse* para os comandos, *PostgreSQL* (*Psycopg*) para a base de dados, e *Dotenv* para segurança das credenciais da base de dados.

## 📦 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/taskmanager-cli.git
cd taskmanager-cli
```

### 2. Crie um ambiente virtual
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
Instale via pip:
```bash
pip install psycopg2-binary python-dotenv
```

### 4. Configuração do Banco de Dados
Acesse o seu PostgreSQL (via pgAdmin ou psql) e crie a tabela necessária para o projeto funcionar:

```sql
CREATE TABLE tasks (
    nome VARCHAR(255) PRIMARY KEY,
    descricao TEXT
);
```

### 5. Configuração do Ambiente (.env)
Crie um arquivo chamado `.env` na raiz do projeto e preencha com as suas credenciais do PostgreSQL:

```ini
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nome_do_seu_banco
DB_USER=seu_usuario_postgres
DB_PASSWORD=sua_senha_postgres
```

Exemplo de comando para a criação de uma tarefa, instruções mais detalhadas no main.py:
```
python main.py adicionar "Estudar X" "Estudar X na segunda-feira"
```

---
**Desenvolvido por [Gustavo1500]**
