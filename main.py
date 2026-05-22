from fastapi import FastAPI,Path,Query,HTTPException#importing required modules from FastAPI
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
import json

app = FastAPI() #object created from FastAPI class, which is used to create the API application

class Patient(BaseModel): #class that represents a patient with various attributes
    id:Annotated[str,Field(...,description="ID of the Patient",example=['POO1]','POO2'])]
    name : Annotated[str,Field(...,description="Name of the Patient",example='Sachin')] #Annotated is used to specify
    city : Annotated[str,Field(...,description="City of the Patient",example='Gurgaon')] #Annotated is used to specify  
    age : Annotated[int,Field(...,gt=0,lt=120,description="Age")] #Annotated is used to specify  
    gender : Annotated[Literal["male","female","other"],Field(...,description="Gender of patient")]                                                                                               
    height : Annotated[float,Field(...,gt=0,description="Height of the patient")]
    weight : Annotated[float,Field(...,gt=0,description="Weight of the patient")]
    
@computed_field
@property
def bmi(self) -> float :
    bmi=round(self.weight / (self.height ** 2),2)
    return bmi
@computed_field
@property
def health_verdict(self) -> str:
    if self.bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= self.bmi < 25:
        return 'Normal weight'
    elif 25 <= self.bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data 

@app.get("/")#decorator that defines a route for the root URL ("/") and specifies that it will handle GET requests
def hello():
    return { 'message': 'Patient Management System API'}

@app.get('/about')#decorator that defines a route for the "/about" URL and specifies that it will handle GET requests
def about():
    return { 'message': 'A fully funmctional API for managing patient data, including BMI calculation and health verdicts.'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')#decorator that defines a route for the "/patient/{patient_id}" URL, where {patient_id} is a path parameter that can be accessed in the function
def get_patient(patient_id: str=Path(..., description="ID of the patient to retrieve",example="P001")): #function that takes a patient_id as a path parameter and returns the corresponding patient data
    data=load_data()
    
    if patient_id in data:
        return data[patient_id]
    return {'message': 'Patient not found'}
    raise HTTPException(status_code=404, detail='Patient not found')    #function that takes a patient_id as a path parameter and returns the corresponding patient data


@app.get('/sort')
def sort_patients(sort_by: str=Query(..., description="Field to sort by (age, bmi, name)", example="age"),order: str =Query('asc')): #function that takes a sort_by parameter as a query parameter and returns the patient data sorted by the specified field
    data = load_data()
    if sort_by not in ['age', 'bmi', 'name']:
        return {'message': 'Invalid sort field. Please choose from age, bmi, or name.'}
    
    if order not in ['asc', 'desc']:
        return {'message': 'Invalid sort order. Please choose from asc or desc.'}   
    
    
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1][sort_by]))
    return sorted_data


@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        return {'message': 'Patient with this ID already exists.'}
    
    data[patient.id] = patient.model_dump()
    
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    return {'message': 'Patient created successfully.', 'patient': patient.model_dump()}