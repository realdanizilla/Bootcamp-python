from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import models
import database
from typing import List
from schema import Item, ItemCreate

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def home():
    return {"qualquer":"coisa"}

@app.post("/items/", response_model=Item) # response_model é o que precisa ser retornado quando cria o item, deve retornar o item completo (name, price, offer e id)
# é similar à notação de saída de formula '->', indica o tipo do return dessa função, o tipo de db_item
def create_item(item: ItemCreate, db: Session = Depends(database.get_db)): # vou receber um item do modelo ItemCreate e o resto é para popular o db (qual conexão vou usar?)
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/", response_model=List[Item]) # equivale ao select *
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all() # offset faz a paginação
    return items

@app.get("/items/{item_id}", response_model=Item) # equivale ao select de um item com base on item_id
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None: # se mandar deletar um item que não tem no banco aí quebra, por isso esse if
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item