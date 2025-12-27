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
    def criar_tarefa(self, nome, desc):
        pass

    def mod_tarefa(self, nome, desc):
        pass

    def remover_tarefa(self, nome, desc):
        pass

    def listar_tarefas(self):
        pass

    def feito_tarefa(self, nome, desc):
        pass


def add_arg(op):
    op.add_argument("nome", help="Nome da tarefa")
    op.add_argument("descricao", help="Descrição da tarefa")


# --- Parsers ---
parser = argparse.ArgumentParser(description="Um gerenciador de tarefas.")
sub_parsers = parser.add_subparsers(
    dest="Comando", required=True, help="Comandos disponíveis"
)

adicionar = sub_parsers.add_parser(name="adicionar", help="Adiciona uma tarefa")
add_arg(adicionar)

modificar = sub_parsers.add_parser(name="modificar", help="Modifica uma tarefa")
add_arg(modificar)

remover = sub_parsers.add_parser(name="remover", help="Remove uma tarefa")
add_arg(remover)

lista = sub_parsers.add_parser(name="lista", help="Lista todas as tarefas abertas")

feito = sub_parsers.add_parser(name="feito", help="Completa uma tarefa")
add_arg(feito)

args = parser.parse_args()


print("Done")
