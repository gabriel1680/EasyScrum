from typing import List, Optional
from flask_openapi3.models.common import Field
from pydantic import BaseModel

from model.sprint import Sprint
from schema.task_schema import TaskResponse, task_to_output


class CreateSprintRequest(BaseModel):
    """Definição do objeto da requisição de criação 
    de uma nova sprint"""

    name: str = "Atualização de informações cadastrais"
    description: str = "Liberação do campo de CPF para cadastro de novos clientes"
    is_done: Optional[bool] = False


class SprintResponse(BaseModel):
    """Definição da resposta de criação ou busca de uma
    sprint"""

    id: int = 1
    name: str = "Atualização de informações cadastrais"
    description: str = "Liberação do campo de CPF para cadastro de novos clientes"
    is_done: Optional[bool] = False
    tasks: List[TaskResponse]


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
        "is_done": sprint.is_done,
        "tasks": list(map(lambda task: task_to_output(task), sprint.tasks))
    }


class SprintListResponse(BaseModel):
    """Definição da resposta de listagem de
    usuários"""

    id: int
    name: str
    description: str = "Liberação do campo de CPF para cadastro de novos clientes"
    is_done: Optional[bool] = False


def sprint_list_to_output(sprints: List[Sprint]):
    result = []
    for sprint in sprints:
        result.append({
            "id": sprint.id,
            "name": sprint.name,
            "description": sprint.description,
            "is_done": sprint.is_done,
        })
    return {"sprints": result}


class UpdateSprintRequest(BaseModel):
    """Definição do payload de atualização da sprint"""

    is_done: bool = True

