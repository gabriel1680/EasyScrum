from sqlalchemy import Column, ForeignKey, Integer, DateTime
from model.model import Model
from typing import Union
from datetime import datetime


class Category(Model):
    """Representa o modelo persistência de 
    categoria de uma tarefa"""

    __tablename__ = 'categories'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', Integer)
    hex_color = Column('hex_color', Integer)
    task_id = Column('task_id', Integer)
    created_at = Column('created_at', DateTime, default=datetime.now())

    task = Column(Integer, ForeignKey("tasks.id"), nullable=False)

    def __init__(self, name: int, hex_color: int, task_id: int,
                 created_at: Union[DateTime, None] = None) -> None:
        """
        Cria uma instância de Category

        Arguments:
            name: nome da categoria
            hex_color: cor da categoria em hexadecimal
            task_id: id da tarefa
            created_at: data de criação da conta
        """
        self.name = name
        self.hex_color = hex_color
        self.task_id = task_id
        if created_at:
            self.created_at = created_at
