class EntityValidationException(Exception):
    """Representa um erro gerado por uma regra de negócio
    que pode ser lançado por qualquer modelo
    """

    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message
