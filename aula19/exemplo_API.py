from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/") # esse decorador faz a sua função virar uma API
def read_root():
    return {"Hello": "World"}

@app.get("/jornada")
def read_jornada():
    return {"Nossa Primeira": "API"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None): # aqui já tem pydantic fazendo a tipagem e validação dos dados
    return {"item_id": item_id, "q": q} # o q é um queryable, que vem depois do '?' na URL ou path - usamos xxx/item_id?q=query

@app.get("/multiply/{item_id}")
def mult_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id * 2}

#response = request.get("http://127.0.0.1:8000/") # se eu bater aqui eu já recebo o retorno da função "read_root", já é uma API
