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

    title: str = Field(..., description='Título da tarefa',
                       example='Alterar o status da terfa arrastando os cards')
    story: str = Field(..., description='User story da tarefa',
                       example='Eu como usuário quero poder alterar o status da tarefa apenas arrastando os cards...')
    due_date: datetime = Field(..., description='Data de término da tarefa',
                               example='2024-11-25T00:00:00')
    status: TaskStatus = Field(
        ..., description='Status da tarefa (done, in progress, revision, backlog)', example='backlog')


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

    sprint_id: int = Field(...,
                           description='Id da sprint que a tarefa pertence', example=1)
    task_id: int = Field(..., description='Id da tarefa', example=1)


class GetTasksRequest(BaseModel):
    """Definição da busca de tarefas de uma sprint"""

    sprint_id: int = Field(...,
                           description='Id da sprint que a tarefa pertence', example=1)


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

    title: str = Field(..., description='Título da tarefa',
                       example='Alterar o status da terfa clicando nos cards')
    story: str = Field(..., description='User story da tarefa',
                       example='Eu como usuário quero poder alterar o status da tarefa apenas clianco em um único botão no card...')
    due_date: datetime = Field(..., description='Data de término da tarefa',
                               example='2024-11-25T00:00:00')
    status: TaskStatus = Field(
        ..., description='Status da tarefa (done, in progress, revision, backlog)', example='backlog')
