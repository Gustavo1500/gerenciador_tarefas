import argparse

from db import feito_task, insert_task, listar_task, mod_task, re_task

"""
Descrição de como funciona
"""


# --- Classe das Tarefas ---
class TaskManager:
    # --- Funções ---
    @staticmethod
    def criar_tarefa(obj):
        insert_task(obj)
        print(f"Tarefa criada: {obj}")

    @staticmethod
    def mod_tarefa(obj):
        mod_task(obj)
        print(f"Tarefa modificada: {obj}")

    @staticmethod
    def remover_tarefa(obj):
        re_task(obj.nome)
        print(f"Tarefa removida: {obj}")

    @staticmethod
    def listar_tarefas(obj):
        listar_task()
        print("Lista:")

    @staticmethod
    def feito_tarefa(obj):
        feito_task(obj.nome)
        print(f"Tarefa concluída: {obj}")

    @staticmethod
    def add_arg(op):
        op.add_argument("nome", help="Nome da tarefa")
        op.add_argument("descricao", help="Descrição da tarefa")


# --- Parsers ---
parser = argparse.ArgumentParser(description="Um gerenciador de tarefas.")
sub_parsers = parser.add_subparsers(
    dest="Comando", required=True, help="Comandos disponíveis"
)

# Criar Tarefa
adicionar = sub_parsers.add_parser(name="adicionar", help="Adiciona uma tarefa")
TaskManager.add_arg(adicionar)
adicionar.set_defaults(function=TaskManager.criar_tarefa)

# Modificar Tarefa
modificar = sub_parsers.add_parser(name="modificar", help="Modifica uma tarefa")
TaskManager.add_arg(modificar)
modificar.set_defaults(function=TaskManager.mod_tarefa)

# Remover Tarefa
remover = sub_parsers.add_parser(name="remover", help="Remove uma tarefa")
remover.add_argument("nome", help="Nome da tarefa")
remover.set_defaults(function=TaskManager.remover_tarefa)

# Lista de Tarefas
lista = sub_parsers.add_parser(name="lista", help="Lista todas as tarefas abertas")
lista.set_defaults(function=TaskManager.listar_tarefas)

# Tarefa Feita
feito = sub_parsers.add_parser(name="feito", help="Completa uma tarefa")
feito.add_argument("nome", help="Nome da tarefa")
feito.set_defaults(function=TaskManager.feito_tarefa)

args = parser.parse_args()

if hasattr(args, "function"):
    args.function(args)

print("Done")
