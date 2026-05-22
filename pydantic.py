from pydantic import BaseModel, EmailStr, AnyUrl,Field ,field_validator
from typing import List, Dict,Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(min_length=1,title='Name')] #name is required and must be at least 1 character long 
    email: EmailStr
    linkdin: AnyUrl
    age: int
    weight: Annotated[float, Field(gt=0, strict=True)] #weight must be greater than 0
    married: bool #=false
    allergies: List[str] #Optional[List[str]] = None
    contact_info: Dict[str, str]
    
    @field_validator('email') #validator function that checks if the email is 2 modes before andd after
    
    @classmethod
    def validate_email(cls, value):
        if not value.endswith('@gmail.com'):
            raise ValueError('Email must be a Gmail address')
        return value
     
def insert_patient_data(patient: Patient):
       print(patient.name)
       print(patient.age)
       print('inserted')
       
def update_patient_data(patient: Patient):
       print(patient.name)
       print(patient.age)
       print('updated')       
       
patient_info = {'name': 'nitish','email': 'nitish@gmail.com', 'linkdin':'https://www.linkedin.com/in/nitish', 'age': 30, 'weight': 70, 'married':True, 'allergies': ['nuts', 'fish'], 'contact_info':{'email':'nitish'}} #creating a dictionary with patient information, including name, age, and weight
patient1 = Patient(**patient_info) #creating an instance of the Patient class using the patient_info dictionary

insert_patient_data(patient1) #inserting patient data using the insert_patient_data function
update_patient_data(patient1) #updating patient data using the update_patient_data function