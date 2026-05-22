from pydantic import BaseModel

class address(BaseModel):
    city: str
    state: str
    pin:str
class Patient(BaseModel):
    name: str
    gender: str = 'Male' 
    age: int
    address: address
    
address_dict = {'city': 'gurgaon','state':'haryana','pin': '12300'}     # pyright: ignore[reportUndefinedVariable]

address1=address(**address_dict)

patient_dict={'name':'sachin','gender':'male','age': 45,'address':address}# pyright: ignore[reportUndefinedVariable]

patient1 = Patient(**patient_dict)

temp=patient1.model_dump(include=['name','gender','age'])#converting the patient1 object to a dictionary using the model_dump method
print(temp)
temp=patient1.model_dump(exclude={'address':['state']})#converting the patient1 object to a dictionary using the model_dump method
print(temp)
print(type(temp))#printing the type of the temp variable, which is a dictionary

temp1=patient1.model_dump_json()#converting the patient1 object to a JSON string using the model_dump_json method
print(temp1)
print(type(temp1))#printing the type of the temp1 variable, which is a string   


temp2=patient1.model_dump(exclude_unset=True)#converting the patient1 object to a dictionary using the model_dump method, excluding any fields that were not explicitly set
print(temp2)