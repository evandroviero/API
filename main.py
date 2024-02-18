from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
    "id": 1,
    "nome" : "Smartphone",
    "descricao": "Um telefone que inteligente",
    "preco": 1500.0
    },
    {
    "id": 2,
    "nome" : "Notebook",
    "descricao": "Um computador movel",
    "preco": 3500.0
    },
    {
    "id": 3,
    "nome" : "Tablet",
    "descricao": "Um computador movel",
    "preco": 2500.0
    },
]

@app.get("/")
def ola_mundo():
    return {"ola":"mundo"}

@app.get("/produtos/")
def listar_produtos():
    return produtos

@app.get("/produtos/{id}")
def buscar_produto(id:int):
    for produto in produtos:
        if produto.get("id") == id:
            return produto
    return {"Status": 401, "Mensagem":"Produto nao encontrado"}