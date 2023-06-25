from datetime import datetime
from typing import List
from pydantic import BaseModel

from model.task import Task


class CreateTaskRequest(BaseModel):
    """Definição do objeto da requisição de criação 
    de uma nova tarefa"""

    id: int = 1
    sprint_id: int = 1
    title: str = "Criação da tela de login"
    story: str = "Eu como usuário quero poder logar no sistema..."
    due_date: datetime = datetime.fromisoformat("2018-11-15T00:00:00")
    status: str = "em andamento"


class TaskOutputResponse(BaseModel):
    """Definição da resposta de criação ou busca de uma
    tarefa"""

    id: int = 1
    sprint_id: int = 1
    title: str = "Criação da tela de login"
    story: str = "Eu como usuário quero poder logar no sistema..."
    due_date: str = "2018-11-15T00:00:00"
    status: str = "em andamento"


class TaskListResponse(BaseModel):
    """Definição da resposta de listagem de
    usuários"""

    tasks: List[TaskOutputResponse]


def task_to_output(task: Task) -> dict:
    """Mapeia o modelo de tarefa para a visualização do cliente
    """
    return {
        "id": task.id,
        "sprint_id": task.sprint_id,
        "title": task.title,
        "story": task.story,
        "due_date": task.due_date,
        "status": task.status
    }
