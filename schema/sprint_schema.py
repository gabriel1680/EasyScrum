from typing import List
from flask_openapi3.models.common import Field
from pydantic import BaseModel
from datetime import datetime

from model.sprint import Sprint
from schema.task_schema import TaskResponse, task_to_output


class CreateSprintRequest(BaseModel):
    """Definição do objeto da requisição de criação 
    de uma nova sprint"""

    name: str = Field(..., description='Nome da sprint')
    description: str = Field(..., description='Descrição da sprint')
    due_date: datetime = Field(..., description='Data de término da sprint')


class SprintResponse(BaseModel):
    """Definição da resposta de criação ou busca de uma
    sprint"""

    id: int = 1
    name: str = 'Atualização de informações cadastrais'
    description: str = 'Liberação do campo de CPF para cadastro de novos clientes'
    due_date: str = '2018-11-15T00:00:00'


class GetSprintRequest(BaseModel):
    """Definição dos parâmetros de busca
    de uma sprint"""

    id: int = Field(..., description='id da sprint')


def sprint_to_output(sprint: Sprint) -> dict:
    """Mapeia o modelo de sprint para a visualização do cliente
    """

    return {
        "id": sprint.id,
        "name": sprint.name,
        "description": sprint.description,
        "due_date": sprint.due_date,
    }


class SprintList(BaseModel):
    """Definição dos dados da resposta de listagem de
    usuários"""

    id: int = 1
    name: str = 'Novas informações de clientes'
    description: str = 'Liberação do campo de CPF para cadastro de novos clientes'
    due_date: str = '2018-11-15'
    tasks: List[TaskResponse]


class SprintListResponse(BaseModel):
    """Definição da resposta de listagem de
    usuários"""

    sprints: List[SprintList]


def sprint_list_to_output(sprints: List[Sprint]):
    result = []
    for sprint in sprints:
        result.append({
            'id': sprint.id,
            'name': sprint.name,
            'description': sprint.description,
            'due_date': sprint.due_date,
            "tasks": list(map(lambda task: task_to_output(task), sprint.tasks))
        })
    return {'sprints': result}

