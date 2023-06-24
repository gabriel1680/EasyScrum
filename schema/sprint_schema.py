from typing import List, Optional
from pydantic import BaseModel

from model.sprint import Sprint


class CreateSprintRequest(BaseModel):
    """Definição do objeto da requisição de criação 
    de uma nova sprint"""

    name: str = "Atualização de informações cadastrais"
    description: str = "Liberação do campo de CPF para cadastro de novos clientes"
    status: str = "done"


class SprintOutputResponse(BaseModel):
    """Definição da resposta de criação ou busca de uma
    sprint"""

    id: int = 1
    name: str = "Atualização de informações cadastrais"
    description: str = "Liberação do campo de CPF para cadastro de novos clientes"
    status: str = "done"
    is_done: Optional[bool] = False


class SprintListResponse(BaseModel):
    """Definição da resposta de listagem de
    usuários"""

    sprints: List[SprintOutputResponse]


def sprint_to_output(sprint: Sprint) -> dict:
    """Mapeia o mdelo de sprint para a visualização do cliente
    """
    return {
        "id": sprint.id,
        "name": sprint.name,
        "description": sprint.description,
        "status": sprint.status,
    }
