from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from model.model import Model
from typing import Union
from datetime import datetime


class Sprint(Model):
    """Representa o modelo persistência de uma sprint"""

    __tablename__ = 'sprints'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255))
    description = Column('description', String(1000))
    status = Column('status', String(50))
    created_at = Column('created_at', DateTime, default=datetime.now)

    tasks = relationship('Task')

    def __init__(self, name: str, description: str, status: str,
                 created_at: Union[DateTime, None] = None) -> None:
        """
        Cria uma instância de Sprint

        Arguments:
            name: nome da sprint
            description: descrição da sprint
            status: status da sprint
            created_at: data de criação da tarefa
        """
        self.name = name
        self.description = description
        self.status = status

        if created_at:
            self.created_at = created_at
