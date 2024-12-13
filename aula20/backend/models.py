# fazer o modelo do database, a representacao
# escolhe uma tabela que faz sentido para atividade da empresa
# se tivermos mutios models podemos ter uma pasta ao inves de um arquivo, cada arquivo seria uma tabela
# note que aqui nao citamos o banco, ja que isso é coberto no arquivo database (agnostico)
# porem o model vai se conectar com obanco

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class ProductModel(Base):
    __tablename__=  "products" #nome da tabela

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    categoria = Column(String)
    email_fornecedor = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
