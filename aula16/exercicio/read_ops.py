from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import text


# Supondo que o banco de dados seja SQLite e esteja no arquivo `database.db`
engine = create_engine("sqlite:///database.db")

# Criação da sessão
with Session(engine) as session:
    # Sua consulta SQL
    statement = text("SELECT * FROM hero;") # neste caso permitiria uma injeção SQL maliciosa, portanto não usamos tanto esse método
    
    # Executando a consulta
    results = session.exec(statement)
    
    # Fetch dos resultados
    heroes = results.fetchall()
    
    # Imprimindo os resultados
    for hero in heroes:
        print(hero)