from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, database, schemas, crud

#app = FastAPI()

myapp = FastAPI()

# if we use app than ERROR:    Error loading ASGI app. Attribute "myapp" not found in module "main". because uvicorn main:myapp --reload --host 127.0.0.1 --port 8010
# name main.py is also can be changed
# Create MySQL Tables
models.Base.metadata.create_all(bind=database.engine)

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# first api reads line by line means 1st it will check for line 23 function than 27 funiction and so on
@myapp.post("/employees/", response_model=schemas.EmployeeResponse)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

@myapp.get("/employees/", response_model=list[schemas.EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@myapp.get("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def get_employee_by_id(employee_id: int, db: Session = Depends(get_db)):

    employee = crud.get_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail=f" employee with id {employee_id} not found in DB")
    return employee

@myapp.put("/employees/{employee_id}", response_model=schemas.EmployeeResponse)
def update_employee(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    updated_employee = crud.update_employee(db, employee_id, employee)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

@myapp.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    deleted_employee = crud.delete_employee(db, employee_id)
    if not deleted_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}



@myapp.get("/greet")
def greeting():
    return {'greet': 'Welcome to my Page'}

@myapp.get("/greeting")
def greeting():
    return {'greeting': 'Welcome to my 2nd Page'}

# Function name doesnot matter wht metter is decoretor i.e @myapp.get("/greet")

@myapp.get("/author")
def author():
    return {'about':{'Author': 'Mohan', 'Location' : 'Bangalore'}}
