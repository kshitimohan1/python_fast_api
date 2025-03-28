from sqlalchemy.orm import Session
import models, schemas

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    new_employee = models.Employee(name=employee.name, email=employee.email)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

#def get_employees(db: Session, skip: int = 0, limit: int = 10):        //If we want to retrieve only first 10 Employee records
#    return db.query(models.Employee).offset(skip).limit(limit).all()

def get_employees(db: Session, skip: int = 0):
    return db.query(models.Employee).offset(skip).all()

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee
