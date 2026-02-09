from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
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

@app.post("/seashells", response_model=schemas.Message)
def create_seashell(shell: schemas.SeashellCreate, db: Session = Depends(get_db)):
    """
    Function to create a seashell and add it to the database.
    
    :param shell: Description
    :type shell: schemas.SeashellCreate
    :param db: Description
    :type db: Session
    """
    db_shell = models.Seashell(**shell.model_dump())
    
    try:
        db.add(db_shell)
        db.commit()
        db.refresh(db_shell)
        return {"message": f"Seashell added successfully with id {db_shell.id}!"}
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Could not save to the database")

@app.get("/seashells", response_model=List[schemas.SeashellResponse])
def get_all_seashells(db: Session = Depends(get_db)):
    """
    Function to fetch and list all seashells in the database.
    
    :param db: Description
    :type db: Session
    """
    shells = db.query(models.Seashell).all()
    if not shells:
        raise HTTPException(status_code=404, detail="Database is empty.")
    else:
        return shells

@app.delete("/seashells/{shell_id}", response_model=schemas.Message)
def remove_seashell(shell_id: int, db: Session = Depends(get_db)):
    """
    Function to remove a single seashell from the database based on it's id.
    
    :param shell_id: Description
    :type shell_id: int
    :param db: Description
    :type db: Session
    """
    db_shell = db.query(models.Seashell).filter(models.Seashell.id == shell_id).first()
    if db_shell is None:
        raise HTTPException(status_code=404, detail="Seashell not found")
    db.delete(db_shell)
    db.commit()
    
    return {"message": "Seashell deleted successfully!"}

@app.put("/seashells", response_model=schemas.SeashellResponse)
def edit_seashell(shell_id: int, db: Session = Depends(get_db)):
    pass