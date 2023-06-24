from datetime import datetime
from typing import List, Optional

from schema.schema import Schema
from model.task import Task


class CreateTaskRequest(Schema):
    """Definição do objeto da requisição de criação 
    de uma nova tarefa"""

    sprint_id: int = 1
    title: str = "Criação da tela de login"
    story: str = "Eu como usuário quero poder logar no sistema..."
    due_date: datetime = datetime.fromisoformat("2018-11-15T00:00:00")
    is_done: Optional[bool] = False


class TaskOutputResponse(Schema):
    """Definição da resposta de criação ou busca de uma
    tarefa"""

    sprint_id: int = 1
    title: str = "Criação da tela de login"
    story: str = "Eu como usuário quero poder logar no sistema..."
    due_date: str = "2018-11-15T00:00:00"
    is_done: Optional[bool] = False


class TaskListResponse(Schema):
    """Definição da resposta de listagem de
    usuários"""

    tasks: List[Task]


def task_to_output(task: Task) -> dict:
    """Mapeia o modelo de tarefa para a visualização do cliente
    """
    return {
        "sprint_id": task.sprint_id,
        "title": task.title,
        "story": task.story,
        "due_date": task.due_date,
        "is_done": task.is_done
    }
