import requests
from pydantic import BaseModel

#requests.get #select - para APIs publicas normalmente só temos essa
#requests.post # create
#requests.put # update
#requests.delete # delete

class PokemonSchema(BaseModel): # contrato de dados, schema de dados, view da API, como eu quero que meu dado seja
    name: str # se por exemplo vier do banco um int, vai quebrar meu código pq ele ta esperando uma string
    type: str

    class Config:
        orm_mode = True

def pegar_pokemon(id: int) -> PokemonSchema:

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}", timeout=10)
    data = response.json()
    data_types = data['types'] # supondo que 'data' é o dicionario com os dados
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchema(name=data['name'],type=types) # jogamos o nome e o tipo do pokemon dentro da classe


if __name__ == "__main__":
    print(pegar_pokemon(10))
    print(pegar_pokemon(6))
    print(pegar_pokemon(13))