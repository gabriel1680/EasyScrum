from typing import List, Optional
from pydantic import BaseModel

from model.sprint import Sprint
from schema.task_schema import TaskOutputResponse, task_to_output


class CreateSprintRequest(BaseModel):
    """Definição do objeto da requisição de criação 
    de uma nova sprint"""

    name: str = "Atualização de informações cadastrais"
    description: str = "Liberação do campo de CPF para cadastro de novos clientes"
    is_done: Optional[bool] = False


class SprintOutputResponse(BaseModel):
    """Definição da resposta de criação ou busca de uma
    sprint"""

    id: int = 1
    name: str = "Atualização de informações cadastrais"
    description: str = "Liberação do campo de CPF para cadastro de novos clientes"
    is_done: Optional[bool] = False


def sprint_to_output(sprint: Sprint) -> dict:
    """Mapeia o modelo de sprint para a visualização do cliente
    """
    return {
        "id": sprint.id,
        "name": sprint.name,
        "description": sprint.description,
        "is_done": sprint.is_done
    }


class SprintListOutputResponse(BaseModel):
    """Definição da resposta de listagem de
    usuários"""
    id: int
    name: str
    tasks: List[TaskOutputResponse]


def sprint_list_to_output(sprints: List[Sprint]):
    result = []
    for sprint in sprints:
        result.append({
            "id": sprint.id,
            "name": sprint.name,
            "description": sprint.description,
            "is_done": sprint.is_done,
            "tasks": list(map(lambda task: task_to_output(task), sprint.tasks))
        })
    return {"sprints": result}
