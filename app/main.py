from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List
from . import database, models, schemas


# Create all tables based on the models defined in models.py.
models.Base.metadata.create_all(bind=database.engine)

# Create the FastAPI application.
app = FastAPI()

# Creates a connection for each request and closes it after.
def get_db():
    db = database.SessionLocal() # Create a new session.
    try:
        yield db # Provide the session to the route function.
    finally: 
        db.close() # Close the connection.

@app.post("/seashells", response_model=schemas.SeashellResponse, status_code=201)
def create_seashell(shell: schemas.SeashellCreate, db: Session = Depends(get_db)):
    """
    Creates a new seashell entry and saves it to the database.
    
    Args:
        shell (schemas.SeashellCreate): The seashell data (name and species are required).
        db (Session): The database session dependency.

    Returns:
        Message: A confirmation message and the newly created seashell object.
    """
    # Convert the Pydantic data into a SQLAlchemy object.
    db_shell = models.Seashell(**shell.model_dump())
    
    try:
        db.add(db_shell) # Add the new shell to staging.
        db.commit() # Save the changes to the database.
        db.refresh(db_shell) # Refresh the database so that the newly created shells id is available.
        return db_shell
    except SQLAlchemyError:
        db.rollback() # Undo changes if saving fails.
        raise HTTPException(status_code=500, detail="Could not save to the database") 

@app.get("/seashells", response_model=List[schemas.SeashellResponse])
def get_all_seashells(db: Session = Depends(get_db)):
    """
    Function to fetch and list all seashells in the database.
    
    Args:
        db (Session): The database session.

    Raises:
        HTTPException: 404 error if no seashells are found.
    
    Returns:
        A list of all Seashells in the database.
    """
    # Query the database for all the shells in the database.
    shells = db.query(models.Seashell).all()
    
    # Check if the database is empty.
    if not shells:
        raise HTTPException(status_code=404, detail="Database is empty.")
    return shells

@app.delete("/seashells/{shell_id}", response_model=schemas.Message)
def remove_seashell(shell_id: int, db: Session = Depends(get_db)):
    """
    Function to remove a single seashell from the database based on it's ID.
    
    Args:
        shell_id (int): The ID of the seashell to remove.
        db (Session): The database session.

    Returns:
        Message: A success message confirming deletion.
    """
    # Search the database for a specific entry based on its ID.
    db_shell = db.query(models.Seashell).filter(models.Seashell.id == shell_id).first()

    # If the shell with corresponding ID is not found return 404 error.
    if db_shell is None:
        raise HTTPException(status_code=404, detail="Seashell not found")
    
    # Delete the shell from the database and commit the changes.
    db.delete(db_shell)
    db.commit()
    
    return {"message": "Seashell deleted successfully!"}

@app.put("/seashells/{shell_id}", response_model=schemas.SeashellResponse)
def edit_seashell(shell_id: int, shell_update: schemas.SeashellUpdate, db: Session = Depends(get_db)):
    """
    Function to edit a seashell in the database by its ID.
    
    Args:
        shell_id (int): The ID of the seashell to edit.
        shell_update (schemas.SeashellUpdate): The fields to update (all are optional).
        db (Session): The database session.

    Returns:
        Message: A success message confirming successful editing and the updated seashell object.
    """
    # Fetch the corresponding shell by its ID from the database.
    db_shell = db.query(models.Seashell).filter(models.Seashell.id == shell_id).first()

    #
    if not db_shell:
        raise HTTPException(status_code=404, detail="Seashell with that ID not found.")

    # Convert the pydantic data to a dictionary.
    update_data = shell_update.model_dump(exclude_unset=True)

    # 
    for key, value in update_data.items(): 
        setattr(db_shell, key, value)
    # ERROR SHELL WITH ID NOT FOUND!
    try:
        # Commit the changes to PostgreSQL
        db.commit()
        # Refresh to get the latest state from the DB
        db.refresh(db_shell)
        return db_shell
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to update the seashell")