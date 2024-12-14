from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schema import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import(
    create_product,
    get_product,
    get_products,
    delete_product,
    update_product
)

router = APIRouter()

### criar minha rota de buscar todos os itens
@router.get("/products/", response_model=List[ProductResponse]) # sempre vamos ter 2 atributos obrigatorios (path-endereco da API e response-retorno da aPI)
def read_all_products(db: Session = Depends(get_db)):
    """Essa é a rota para ler todos os produtos do banco de dados

    Args:
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    products = get_products(db) # aqui só invocamos as funcoes
    return products

### criar rota de buscar 1 item
@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="voce está buscando um produto que nao existe")
    return db_product

### criar rota de adicionar 1 item
@router.post("/products/", response_model=ProductResponse)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)

### criar rota de deletar 1 item
@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product_route(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_product(db, product_id=product_id)
    if db_product is None:
         raise HTTPException(status_code=404, detail="voce está deletando um produto que nao existe")
    return db_product

### criar rota de fazer update nos itens
@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product_route(product_id: int, product: ProductUpdate , db: Session = Depends(get_db)):
    db_product = update_product(db, product_id=product_id, product=product)
    if db_product is None:
         raise HTTPException(status_code=404, detail="voce está fazendo update em um produto que nao existe")
    return db_product
