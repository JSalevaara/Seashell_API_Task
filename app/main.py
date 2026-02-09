from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import database, models, schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally: 
        db.close()

@app.post("/seashells/", response_model=schemas.SeashellResponse)
def create_seashell(shell: schemas.SeashellCreate, db: Session = Depends(get_db)):
    db_shell = models.Seashell(**shell.model_dump())
    db.add(db_shell)
    db.commit()
    db.refresh(db_shell)
    return db_shell

@app.get("/seashells/", response_model=List[schemas.SeashellResponse])
def get_all_seashells(db: Session = Depends(get_db)):
    return db.query(models.Seashell).all()