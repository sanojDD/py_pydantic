from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

  name:Annotated[str,Field(max_length=50, title='Name of the patient', description='give the name of the patient in less than 50 characters', examples=['Sanoj','Nitish'])]
  email:EmailStr
  linkedin_url:AnyUrl
  age:int = Field(gt=0 , lt=80)
  weight:Annotated[float,Field(gt=0, strict=True)]
  isMarried:Annotated[bool, Field(default=None , description="is the patient married or not")]
  allergies:Annotated[Optional[List[str]] , Field(default=None ,max_length=5)]
  contact_details:Dict[str, str]



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


def update_patient_data(patient: Patient):

  print(patient.name)
  print(patient.email)
  print(patient.age)
  print(patient.weight)
  print(patient.isMarried)
  print(patient.allergies)
  print(patient.contact_details)
  print('updated into the DB....')


patient_info = {'name':'sanoj','email':'abc@gmail.com' ,'linkedin_url':'http://linkedin.com/1322','age':30 ,'weight': 75.2, 'isMarried':True,'allergies':['pollen','dust'],  'contact_details':{
   'phone':'100'
}}


patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
update_patient_data(patient1)