from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from model.task import Task


class CreateTaskRequest(BaseModel):
    """Definição do objeto da requisição de criação 
    de uma nova tarefa"""

    title: str = "Criação da tela de login"
    story: str = "Eu como usuário quero poder logar no sistem..."
    due_date: datetime = datetime.fromisoformat("2018-11-15T00:00:00")
    is_done: Optional[bool] = False


class TaskOutputResponse(BaseModel):
    """Definição da resposta de criação ou busca de uma
    tarefa"""

    title: str = "Criação da tela de login"
    story: str = "Eu como usuário quero poder logar no sistem..."
    due_date: str = "2018-11-15T00:00:00"
    is_done: Optional[bool] = False


class TaskListResponse(BaseModel):
    """Definição da resposta de listagem de
    usuários"""

    tasks: List[Task]


def task_to_output(task: Task) -> dict:
    """Mapeia o mdelo de tarefa para a visualização do cliente
    """
    return {
        "title": task.title,
        "story": task.story,
        "due_date": task.due_date,
        "is_done": task.is_done
    }
