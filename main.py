from fastapi import FastAPI,Path,Query #importing required modules from FastAPI
import json

app = FastAPI() #object created from FastAPI class, which is used to create the API application

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