from pydantic import BaseModel, EmailStr


class EmployeeBase(BaseModel):
    name: str
    email: EmailStr

#class EmployeeCreate(EmployeeBase):
#    pass
## without EmployeeBase No Inheritance → Each model is defined separately.
#class EmployeeResponse(EmployeeBase):
#    id: int

#BaseModel is a class from Pydantic, a Python library for data validation and serialization. It is used to define request and response models in FastAPI and other frameworks

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int

class Config:
    orm_mode = True
