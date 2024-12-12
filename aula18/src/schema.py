from pydantic import BaseModel

class PokemonSchema(BaseModel): # contrato de dados, schema de dados, view da API, como eu quero que meu dado seja
    name: str # se por exemplo vier do banco um int, vai quebrar meu código pq ele ta esperando uma string
    type: str

    class Config:
        orm_mode = True