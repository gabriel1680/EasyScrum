from typing import List, Optional

from schema.schema import Schema
from model.sprint import Sprint


class CreateSprintRequest(Schema):
    """Definição do objeto da requisição de criação 
    de uma nova sprint"""

    name: str = "Atualização de informações cadastrais"
    description: str = "Liberação do campo de CPF para cadastro de novos clientes"
    status: str = "done"


class SprintOutputResponse(Schema):
    """Definição da resposta de criação ou busca de uma
    sprint"""

    name: str = "Atualização de informações cadastrais"
    description: str = "Liberação do campo de CPF para cadastro de novos clientes"
    status: str = "done"
    is_done: Optional[bool] = False


class SprintListResponse(Schema):
    """Definição da resposta de listagem de
    usuários"""

    sprints: List[Sprint]


def sprint_to_output(sprint: Sprint) -> dict:
    """Mapeia o mdelo de sprint para a visualização do cliente
    """
    return {
        "name": sprint.name,
        "description": sprint.description,
        "status": sprint.status,
    }
