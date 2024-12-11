from sqlalchemy import create_engine

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

# exemplo
# URI = postgresql+pg8000://dbuser:kx%40jj5%2Fg@pghost10/appdb
# postgres é o banco
# pg8000 é o driver
# dbuser é o usuario
# kx%40jj5%2Fg é a senha
# pghost10 é o host
# appdb é o banco de dados

# genericamente temos:
#dialect+driver://username:password@host:port/database

# poderia passar o parametro pool_size=numero para definir qtde de conexões simultâneas no banco

print("Conexão com SQLite estabelecida.")

from sqlalchemy.orm import declarative_base #módulo de ORM do SQLAlchemy, permit a criação de instancia que faz o de-para
from sqlalchemy import Column, Integer, String # cuida do schema/type (string no python e varchar no banco)

Base = declarative_base()

class Usuario(Base): # isso é uma tabela
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True) # atributos são colunas
    nome = Column(String)
    idade = Column(Integer)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# adicionando usuário joao na tabela usuario
# novo_usuario = Usuario(nome='João', idade=28)
# session.add(novo_usuario)
# session.commit()

# print("Usuário inserido com sucesso.")

# rodando uma query procurando o usuário joao
# usuario = session.query(Usuario).filter_by(nome='João').first()
# print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")


with Session() as session:
    novo_usuario2 = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario2)
    session.commit()
    # O commit é feito automaticamente aqui, se não houver exceções
    # O rollback é automaticamente chamado se uma exceção ocorrer
    # A sessão é fechada automaticamente ao sair do bloco with