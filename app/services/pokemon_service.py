import requests
from fastapi import HTTPException
from app.client import db_pokemon
from app.schemas.pokemon_schema import pokemon_datos

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/"


def guardar_pokemon(nombre: str):
    respuesta = requests.get(f"{POKEAPI_URL}{nombre.lower()}")

    if respuesta.status_code != 200:
        raise HTTPException(status_code=404, detail="El Pokemon no fue encontrado")

    data = respuesta.json()

    pokemon = {
        "nombre": data["name"],
        "habilidades": [h["ability"]["name"] for h in data["abilities"]],
        "altura": data["height"],
        "movimientos": [m["move"]["name"] for m in data["moves"]],
        "tipos": [t["type"]["name"] for t in data["types"]],
        "peso": data["weight"],
    }

    if db_pokemon.find_one({"nombre": pokemon["nombre"]}):
        raise HTTPException(status_code=400, detail="El pokemon ya existe")

    result = db_pokemon.insert_one(pokemon)

    nuevo_pokemon = db_pokemon.find_one({"_id": result.inserted_id})

    return pokemon_datos(nuevo_pokemon)


def pokemones():
    pokemones = db_pokemon.find()

    return [pokemon_datos(p) for p in pokemones]

def eliminar_pokemon(nombre: str):
    resultado = db_pokemon.delete_one({"nombre": nombre.lower()})

    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="El pokemon no fue encontrado")

    return {"mensaje": "Pokemon eliminado"}

def moves_pokemon(nombre: str):
    pokemon = db_pokemon.find_one({"nombre" : nombre.lower()})
    
    if not pokemon:
        raise HTTPException(status_code=404, detail="El pokemon no fue encontrado")

    return {"movimientos": pokemon.get("movimientos", [])}
