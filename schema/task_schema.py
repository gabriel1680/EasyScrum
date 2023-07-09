from datetime import datetime
from typing import List

from sqlalchemy import Enum
from flask_openapi3.models.common import Field
from pydantic import BaseModel

from model.task import Task


class TaskStatus(str, Enum):
    """Tipos de status que uma task pode ter
    """

    BACKLOG = 'backlog'
    IN_PROGRESS = 'in progress'
    REVISION = 'revision'
    DONE = 'done'


class CreateTaskRequest(BaseModel):
    """Definição do objeto da requisição de criação 
    de uma nova tarefa"""

    title: str = Field(..., description='Título da tarefa')
    story: str = Field(..., description='User story da tarefa')
    due_date: datetime = Field(..., description='Data de término da tarefa')
    status: TaskStatus = Field(..., description='Status da tarefa (done, in progress, revision, bakclog)')


class TaskResponse(BaseModel):
    """Definição da resposta de criação ou busca de uma
    tarefa"""

    id: int = 1
    sprint_id: int = 1
    title: str = 'Criação da tela de login'
    story: str = 'Eu como usuário quero poder logar no sistema...'
    due_date: str = '2018-11-15T00:00:00'
    status: str = 'em andamento'


class TaskListResponse(BaseModel):
    """Definição da resposta de listagem de
    usuários"""

    tasks: List[TaskResponse]


class GetTaskRequest(BaseModel):
    """Definição da busca de uma tarefa"""

    sprint_id: int = Field(..., description='Id da sprint que a tarefa pertence')
    task_id: int = Field(..., description='Id da tarefa')


class GetTasksRequest(BaseModel):
    """Definição da busca de tarefas de uma sprint"""

    sprint_id: int = Field(..., description='Id da sprint que a tarefa pertence')


def task_to_output(task: Task) -> dict:
    """Mapeia o modelo de tarefa para a visualização do cliente
    """
    return {
        'id': task.id,
        'sprint_id': task.sprint_id,
        'title': task.title,
        'story': task.story,
        'due_date': task.due_date.isoformat(),
        'status': task.status
    }


class UpdateTaskRequest(BaseModel):
    """Definição do payload de atualização
    de uma tarefa"""

    title: str = Field(..., description='Título da tarefa')
    story: str = Field(..., description='User story da tarefa')
    due_date: datetime = Field(..., description='Data de término da tarefa')
    status: TaskStatus = Field(..., description='Status da tarefa (done, in progress, revision, bakclog)')



