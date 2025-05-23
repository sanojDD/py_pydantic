from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

  name: str
  age: int
  email:EmailStr
  linkedin_url:AnyUrl
  weight: float
  isMarried: bool
  allergies:List[str]
  contact_details:Dict[str, str]

  @model_validator(mode='after')
  def validate_emergency_contact(cls, model):
    if model.age > 60 and 'emergency' not in model.contact_details:
      raise ValueError('patients older than 60 must have an emergency number')
    
    else:
      return model


def insert_patient_data(patient: Patient):

  print(patient.name)
  print(patient.email)
  print(patient.linkedin_url)
  print(patient.age)
  print(patient.weight)
  print(patient.isMarried)
  print(patient.allergies)
  print(patient.contact_details)
  print('inserted into the DB....')


patient_info = {'name':'sanoj','email':'abc@icici.com' ,'age':'65','linkedin_url':'http://linkedin.com/1322' ,'weight': 75.2, 'isMarried':True,'allergies':['girls','dust'],  'contact_details':{
   'phone':'100', 'emergency':'12344343'
}}


patient1 = Patient(**patient_info) # validaton = type coercion

insert_patient_data(patient1)