from pydantic import BaseModel

class address(BaseModel):
    city: str
    state: str
    pin:str
class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: address
    
address_dict = {'city': 'gurgaon','state':'haryana','pin': '12300'}     # pyright: ignore[reportUndefinedVariable]

address1=address(**address_dict)

patient_dict={'name':'sachin','gender':'male','age': 45,'address':address}# pyright: ignore[reportUndefinedVariable]

patient1 = Patient(**patient_dict)
print(patient1)
    