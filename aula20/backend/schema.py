# esse arquivo cuida das validacoes de dados para cada funcao CRUD
# podemos rodar regras de negocio voltadas para validacao, principalmente usando decoradores
# nao é igual ao model pq cada funcao precisa passar determinados argumentos diferente das outras

from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional

# criando as categorias
class CategoriaBase(Enum):
    categoria1 = "Eletrônico"
    categoria2 = "Eletrodoméstico"
    categoria3 = "Móveis"
    categoria4 = "Roupas"
    categoria5 = "Calçados"

# criando uma classe base que é denominador comum de todas as classes (todas tem essa / herdam essa)
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

    @validator("categoria")
    def check_categoria(cls,v):
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")

class ProductCreate(ProductBase): # este valida a criacao de produto
    pass # nao muda nada pois ao criar um produto seguimos exatamente o schema da productbase (ex sem id)

class ProductResponse(ProductBase): # este valida a leitura de produto
    id: int # queremos id quando formos receber informacao de um produto
    created_at: datetime # queremos created_at quando formos receber informacao de um produto

    class config: # usamos este pq ele é o único que interage com o orm (para fazer o model_dump no crud)
        from_attributes = True

class ProductUpdate(BaseModel): # este valida o update, que é mais chatinho pq td é optional, podemos atualizar um campo ou todos
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None

    @validator("categoria", pre=True, always=True)
    def check_categoria(cls,v):
        if v is None:
            return v
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")