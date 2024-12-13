# tambem conhecido como controller

from sqlalchemy.orm import Session
from schema import ProductUpdate, ProductCreate  # o product response vai na rota(API)
from models import ProductModel

# aqui sao as funcoes que falam com o banco de dados
# get all - select * from
def get_products(db: Session):
    """Essa funcao retorna todos os produtos da tabela Product

    Args:
        db (Session): a sessao do db

    Returns:
        _type_: query com todos os produtos da tabela product 
    """
    return db.query(ProductModel).all()


# get where id = 1
def get_product(db: Session, product_id: int):
    """Essa funcao retorna um produto da tabela product

    Args:
        db (Session): a sessao do db
        product_id (int): o id to produto a ser retornado

    Returns:
        _type_: query com a informacao do produto a ser retornado
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

# insert into (create)
def create_product(db: Session, product: ProductCreate):
    """Essa funcao cria um produto na tabela product

    Args:
        db (Session): a sessao do db
        product (ProductCreate): informacoes do produto de acordo com o schema ProductCreate

    Returns:
        _type_: o item criado na tabela product
    """
    # transformar a view para ORM. to recebendo em schema de pydantic mas vo salvar como schema do ORM (meu model)
    db_product = ProductModel(**product.model_dump()) # os dois asteriscos significa 'desempacotar'. 
    #O model dump 'baixa o modelo'. só consigo fazer o model_dump por causa do class config no schema

    # adicionar na tabela
    db.add(db_product)

    # commitar na tabela
    db.commit()

    # fazer o refresh do banco (busque no banco)
    db.refresh(db_product)

    # retornar para o usuario o item criado
    return db_product


# delete where id = 1
def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit() # aqui nao tem refresh pq eu deletei o item
    return db_product

# update where id = 1 (mais chatinho pq é cheio de if)
def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.categoria is not None:
        db_product.categoria = product.categoria
    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit()
    return db_product