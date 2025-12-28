import argparse
from dataclasses import dataclass

"""
Tasks:
ADD:
- Name of Task
- Description
Example: python main.py add "Walk" "Go for a walk on saturday."

MODIFY:
- Name of Task
- Description
Example: python main.py modify "Walk" "Go for a walk on wednesday."

REMOVE:
- Name of Task
Example: python main.py remove "Walk"

LIST:
Example: python main.py list

DONE:
- Name of Task
Example: python main.py done "Walk"
"""


# --- Classe das Tarefas ---
@dataclass
class TaskManager:
    nome: str
    desc: str

    # --- Funções ---
    def criar_tarefa(self, obj):
        print(f"Tarefa criada: {obj}")

    def mod_tarefa(self, obj):
        print(f"Tarefa modificada: {obj}")

    def remover_tarefa(self, obj):
        print(f"Tarefa removida: {obj}")

    @staticmethod
    def listar_tarefas():
        print("Lista:")

    def feito_tarefa(self, obj):
        print(f"Tarefa concluída: {obj}")

    @staticmethod
    def add_arg(op):
        op.add_argument("nome", help="Nome da tarefa")
        op.add_argument("descricao", help="Descrição da tarefa")

    # --- Handlers ---
    @staticmethod
    def handler_add(c):
        task = TaskManager(c.nome, c.descricao)
        task.criar_tarefa(task)

    @staticmethod
    def handler_mod(c):
        task = TaskManager(c.nome, c.descricao)
        task.mod_tarefa(task)

    @staticmethod
    def handler_re(c):
        task = TaskManager(c.nome, c.descricao)
        task.remover_tarefa(task)

    @staticmethod
    def handler_list(c):
        task = TaskManager(c.nome, c.descricao)
        task.listar_tarefas()

    @staticmethod
    def handler_done(c):
        task = TaskManager(c.nome, c.descricao)
        task.feito_tarefa(task)


# --- Parsers ---
parser = argparse.ArgumentParser(description="Um gerenciador de tarefas.")
sub_parsers = parser.add_subparsers(
    dest="Comando", required=True, help="Comandos disponíveis"
)

# Criar Tarefa
adicionar = sub_parsers.add_parser(name="adicionar", help="Adiciona uma tarefa")
TaskManager.add_arg(adicionar)
adicionar.set_defaults(function=TaskManager.handler_add)

# Modificar Tarefa
modificar = sub_parsers.add_parser(name="modificar", help="Modifica uma tarefa")
TaskManager.add_arg(modificar)
modificar.set_defaults(function=TaskManager.handler_mod)

# Remover Tarefa
remover = sub_parsers.add_parser(name="remover", help="Remove uma tarefa")
TaskManager.add_arg(remover)
remover.set_defaults(function=TaskManager.handler_re)

# Lista de Tarefas
lista = sub_parsers.add_parser(name="lista", help="Lista todas as tarefas abertas")
TaskManager.listar_tarefas()
lista.set_defaults(function=TaskManager.handler_list)

# Tarefa Feita
feito = sub_parsers.add_parser(name="feito", help="Completa uma tarefa")
TaskManager.add_arg(feito)
feito.set_defaults(function=TaskManager.handler_done)

args = parser.parse_args()

if hasattr(args, "function"):
    args.function(args)

print("Done")
