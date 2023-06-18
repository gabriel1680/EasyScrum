from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """Representação da resposta com erro"""

    message: str
