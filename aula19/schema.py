from pydantic import BaseModel, PositiveFloat, PositiveInt #pydanti tem tipos que não sao padrão no python e vale usar
from typing import Union

class ItemBase(BaseModel): # valida o que o usuário vai passar mas nao cria ID
    name: str
    price: PositiveFloat    
    is_offer: Union[bool, None] = None

class ItemCreate(ItemBase): # quando vou criar o item eu nao sei o ID, então não quero, logo usuário não precisa passar o ID
    pass

class Item(ItemBase): #quando eu puxo/consumo do banco eu quero ID, quando eu crio eu não quero
    id: PositiveInt
