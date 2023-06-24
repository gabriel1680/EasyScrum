from sqlalchemy import Boolean, Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from model.model import Model
from typing import Optional, Union
from datetime import datetime


class Task(Model):
    """Representa o modelo persistência de uma tarefa"""

    __tablename__ = 'tasks'

    id = Column('id', Integer, primary_key=True)
    sprint_id = Column('sprint_id', Integer)
    title = Column('title', String(255))
    story = Column('story', String(1000))
    due_date = Column('due_date', DateTime)
    is_done = Column('is_done', Boolean, default=False)
    created_at = Column('created_at', DateTime, default=datetime.now)

    sprint = Column(Integer, ForeignKey("sprints.id"), nullable=False)
    category = relationship("Category")

    def __init__(self, sprint_id: int, title: str, due_date: datetime, story: str,
                is_done: Optional[bool] = False, 
                created_at: Union[DateTime, None] = None) -> None:
        """
        Cria uma instância de Task

        Arguments:
            sprint_id: id da sprint em que a task pertence
            title: título da tarefa
            story: user story da tarefa
            due_date: prazo para conclusão
            is_done: se a task está finalizada
            created_at: data de criação da tarefa
        """
        self.sprint_id = sprint_id
        self.title = title
        self.story = story
        self.due_date = due_date
        self.is_done = is_done

        if created_at:
            self.created_at = created_at
