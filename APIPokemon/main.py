from fastapi import FastAPI
from app.routers import pokemon_router

app = FastAPI()

app.include_router(pokemon_router.router)
