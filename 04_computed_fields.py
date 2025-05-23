from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

  name: str
  age: int
  email:EmailStr
  linkedin_url:AnyUrl
  weight: float
  height: float
  isMarried: bool
  allergies:List[str]
  contact_details:Dict[str, str]

  @computed_field
  @property
  def bmi(self) -> float:
    bmi = round(self.weight/(self.height ** 2),2)
    return bmi

 
def insert_patient_data(patient: Patient):

  print(patient.name)
  print(patient.email)
  print(patient.linkedin_url)
  print(patient.age)
  print(patient.weight)
  print(patient.height)
  print(patient.bmi)
  print(patient.isMarried)
  print(patient.allergies)
  print(patient.contact_details)
  print('inserted into the DB....')


patient_info = {'name':'sanoj','email':'abc@icici.com' ,'age':'65','linkedin_url':'http://linkedin.com/1322' ,'weight': 60.2,'height':5.9, 'isMarried':False,'allergies':['girls','dust'],  'contact_details':{
   'phone':'100'
}}


patient1 = Patient(**patient_info) # validaton = type coercion

insert_patient_data(patient1)