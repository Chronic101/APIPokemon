from fastapi import APIRouter
from app.services.pokemon_service import guardar_pokemon, pokemones, eliminar_pokemon, moves_pokemon

router = APIRouter(prefix="/pokemon", tags=["Pokemon"])

# Se agrega un nuevo pokemon con sus caracteristicas
@router.post("/{nombre}")
async def importar_pokemon(nombre: str):
    return guardar_pokemon(nombre)

# Se muestra todos los pokemones con sus caracteristicas
@router.get("/")
async def obtener_pokemones():
    return pokemones()

# Se elimina un determinado pokemon
@router.delete("/{nombre}")
async def delete_pokemon(nombre: str):
    return eliminar_pokemon(nombre)

# Se obtienen los movimientos de un determinado pokemon
@router.get("/{nombre}/moves")
async def movimientos_pokemon(nombre: str):
    return moves_pokemon(nombre)