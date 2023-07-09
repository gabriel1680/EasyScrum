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
    due_date = Column('due_date', DateTime)
    description = Column('description', String(1000))
    created_at = Column('created_at', DateTime, default=datetime.now)

    tasks = relationship('Task', backref='sprint')

    def __init__(self, name: str, description: str, due_date: datetime,
                 created_at: Union[DateTime, None] = None) -> None:
        """
        Cria uma instância de Sprint

        Arguments:
            name: nome da sprint
            description: descrição da sprint
            due_date: data de fim da sprint
            created_at: data de criação da tarefa
        """
        self.name = name
        self.description = description
        self.due_date = due_date

        if created_at:
            self.created_at = created_at

