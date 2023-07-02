from typing import Optional
from sqlalchemy import Column, String, Integer, DateTime, Boolean
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
    is_done = Column('is_done', Boolean, default=False)
    created_at = Column('created_at', DateTime, default=datetime.now)

    tasks = relationship('Task', backref='sprint')

    def __init__(self, name: str, description: str, due_date: datetime,
                 is_done: Optional[bool] = False,
                 created_at: Union[DateTime, None] = None) -> None:
        """
        Cria uma instância de Sprint

        Arguments:
            name: nome da sprint
            description: descrição da sprint
            due_date: data de fim da sprint
            is_done: se a sprint está finalizada ou não
            created_at: data de criação da tarefa
        """
        self.name = name
        self.description = description
        self.due_date = due_date
        self.is_done = is_done

        if created_at:
            self.created_at = created_at
