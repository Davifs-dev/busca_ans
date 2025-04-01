from fastapi import FastAPI
from typing import List
from services.operadoras_service import buscar_operadoras_por_texto
from fastapi.middleware.cors import CORSMiddleware
from settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
)

# Adicionando o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://localhost",
        "http://127.0.0.1:8080",
    ],  # Define quais origens podem acessar
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)


# rota que recebe o termo de pesquisa
@app.get("/operadoras/buscar/")
async def buscar_operadoras(query: str):

    operadoras = buscar_operadoras_por_texto(query)
    return operadoras
