from pydantic import BaseModel
from typing import List

class ModeloPokemon(BaseModel):
    nombre: str
    habilidades: List[str]
    altura: int
    movimientos: List[str]
    tipos: List[str]
    peso: int