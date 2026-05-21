from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool 
    allergies: List[str]
    contact_info: Dict[str, str]
    
def insert_patient_data(patient: Patient):
       print(patient.name)
       print(patient.age)
       print('inserted')
       
def update_patient_data(patient: Patient):
       print(patient.name)
       print(patient.age)
       print('updated')       
       
patient_info = {'name': 'nitish', 'age': 30, 'weight': 70, 'married':True, 'allergies': ['nuts', 'fish'], 'contact_info':{'email':'nitish'}} #creating a dictionary with patient information, including name, age, and weight
patient1 = Patient(**patient_info) #creating an instance of the Patient class using the patient_info dictionary

insert_patient_data(patient1) #inserting patient data using the insert_patient_data function
update_patient_data(patient1) #updating patient data using the update_patient_data function