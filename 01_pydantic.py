from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):

  name:str
  age:int
  weight:float
  isMarried:bool = False
  allergies:Optional[List[str]] = None
  contact_details:Dict[str, str]



def insert_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print(patient.weight)
  print(patient.isMarried)
  print(patient.allergies)
  print(patient.contact_details)
  print('inserted into the DB....')


def update_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print(patient.weight)
  print(patient.isMarried)
  print(patient.allergies)
  print(patient.contact_details)
  print('updated into the DB....')


patient_info = {'name':'sanoj', 'age':30, 'weight': 75.2, 'isMarried':True,'allergies':['pollen','dust'],  'contact_details':{
  'email':'abc7@gmail.com', 'phone':'100'
}}


patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)