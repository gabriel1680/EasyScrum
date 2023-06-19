from sqlalchemy import Boolean, Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from model.base_model import BaseModel
from typing import Optional, Union
from datetime import datetime


class Task(BaseModel):
    """Representa o modelo persistência de uma tarefa"""

    __tabletitle__ = 'tasks'

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(255))
    story = Column('story', String(1000))
    due_date = Column('due_date', DateTime)
    is_done = Column('is_done', Boolean, default=False)
    created_at = Column('created_at', DateTime, default=datetime.now)

    category = relationship("Category")

    def __init__(self, title: str, due_date: datetime, story: str, is_done: Optional[bool] = False,
                 created_at: Union[DateTime, None] = None) -> None:
        """
        Cria uma instância de Task
        
        Arguments:
            title: título da tarefa
            story: user story da tarefa
            due_date: prazo para conclusão
            is_done: se a task está finalizada
            created_at: data de criação da tarefa
        """
        self.title = title
        self.story = story
        self.due_date = due_date
        self.is_done = is_done

        if created_at:
            self.created_at = created_at

