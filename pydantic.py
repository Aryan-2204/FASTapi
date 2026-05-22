from pydantic import BaseModel, EmailStr, AnyUrl,Field ,field_validator,model_validator,computed_field
from typing import List, Dict,Annotated

class Patient(BaseModel): #class that represents a patient with various attributes
    name: Annotated[str, Field(min_length=1,title='Name')] #name is required and must be at least 1 character long 
    email: EmailStr
    linkdin: AnyUrl
    age: int
    weight: Annotated[float, Field(gt=0, strict=True)] #weight must be greater than 0
    married: bool #=false
    allergies: List[str] #Optional[List[str]] = None
    contact_info: Dict[str, str]
    
    
    
    @computed_field #computed field method that calculates the BMI of a patient
    @property
    def bmi(self) -> float:
        bmi=round(self.weight / (self.age ** 2),2)
        return bmi
    
    

    
    @model_validator(mode='before') #model validator function that checks if the age is greater than 0 before validation
    def validate_emergency_contact(cls, values):
        if values.get('age', 0) > 60 and 'emergency' not in values.get('contact_info', {}):
            raise ValueError('Emergency contact information is required for patients over 60 years old')
        return values

    @field_validator('email') #validator function that checks if the email is 2 modes before andd after
    
    @classmethod
    def validate_email(cls, value):
        if not value.endswith('@gmail.com'):
            raise ValueError('Email must be a Gmail address')
        return value
    
    
    @field_validator('name',mode='after') #validator function that transforms the name to uppercase before validation
    @classmethod
    def transform_name(cls,value):
        return value.upper()#transforming the name to uppercase using a validator function
    
    
    
     
def insert_patient_data(patient: Patient): 
       print(patient.name)
       print(patient.age)
       print('inserted')
       
def update_patient_data(patient: Patient):
       print(patient.name)
       print(patient.age)
       print(patient.allergies)
       print(patient.married)
       print('BMI',patient.bmi)
       print('updated')       
 
 
 
 
       
patient_info = {'name': 'nitish','email': 'nitish@gmail.com', 'linkdin':'https://www.linkedin.com/in/nitish', 'age': 30, 'weight': 70, 'married':True, 'allergies': ['nuts', 'fish'], 'contact_info':{'email':'nitish'}} #creating a dictionary with patient information, including name, age, and weight
patient1 = Patient(**patient_info) #creating an instance of the Patient class using the patient_info dictionary




insert_patient_data(patient1) #inserting patient data using the insert_patient_data function
update_patient_data(patient1) #updating patient data using the update_patient_data function