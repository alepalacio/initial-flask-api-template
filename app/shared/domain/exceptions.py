class NotFoundException(Exception):
    """ Common not found exception. """
    
    def __init__(self, entity, message="no encontrado."):
        super().__init__(self, entity, message)
        self.entity = entity
        self.message = message
        
    def __str__(self) -> str:
        return f"{self.entity} {self.message}"
