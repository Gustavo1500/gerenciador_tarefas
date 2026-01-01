import os

import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# Conecção com Base de Dados
def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


# --- Operações ---
# Adicionar Tarefa na Base de Dados
def insert_task(task):
    """Coloca uma tarefa na base de dados."""
    print("Adicionando Tarefa...")
    task_sql = """INSERT INTO tasks (nome, descricao) VALUES (%s, %s);"""
    task_data = (task.nome, task.descricao)
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(task_sql, task_data)
                conn.commit()
                print("Tarefa adicionada")
    except Exception as error:
        print(f"Ocorreu um erro na DB: {error}")


# Modificar Tarefa na Base de Dados
def mod_task(task):
    """Modificando uma tarefa na base de dados."""
    print("Modificando Tarefa...")
    task_sql = """
    UPDATE tasks
    SET descricao = %s
    WHERE nome = %s;"""
    task_data = (task.descricao, task.nome)
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(task_sql, task_data)
                conn.commit()
                print("Tarefa modificada")
    except Exception as error:
        print(f"Ocorreu um erro na DB: {error}")


# Remover Tarefa na Base de Dados
def re_task(task):
    """Remover uma tarefa na base de dados."""
    print("Removendo Tarefa...")
    task_sql = """DELETE FROM tasks WHERE nome = %s;"""
    task_data = (task,)
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(task_sql, task_data)
                conn.commit()
                print("Tarefa removida")
    except Exception as error:
        print(f"Ocorreu um erro na DB: {error}")


# Listar Tarefa na Base de Dados
def listar_task():
    """Listar tarefas na base de dados."""
    print("Listando Tarefa...")
    task_sql = """SELECT nome, descricao FROM tasks;"""
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(task_sql)
                results = cur.fetchall()

                for row in results:
                    nome = row[0]
                    descricao = row[1]
                    print(f"Nome: {nome} | Descrição: {descricao}")
                print("Tarefas listadas")
    except Exception as error:
        print(f"Ocorreu um erro na DB: {error}")


# Completar Tarefa na Base de Dados
def feito_task(task):
    """Completar uma tarefa na base de dados."""
    print("Completando Tarefa...")
    task_sql = """DELETE FROM tasks WHERE nome = %s;"""
    task_data = (task,)
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(task_sql, task_data)
                conn.commit()
                print("Tarefa completada")
    except Exception as error:
        print(f"Ocorreu um erro na DB: {error}")
