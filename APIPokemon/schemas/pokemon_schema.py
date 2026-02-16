def pokemon_datos(pokemon) -> dict:
    return {
        "id": str(pokemon["_id"]),
        "nombre": pokemon["nombre"],
        "habilidades": pokemon["habilidades"],
        "altura": pokemon["altura"],
        "movimientos": pokemon["movimientos"],
        "tipos": pokemon["tipos"],
        "peso": pokemon["peso"]
    }
