from pydantic import BaseModel


class Schema(BaseModel):
    class Config:
        arbitrary_types_allowed = True
