from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
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

  @field_validator('email')
  @classmethod
  def email_validator(cls, value):

    valid_domains = ['hdfc.com', 'icici.com']

    # abc@gmail.com
    domain_name = value.split('@')[-1]

    if domain_name not in valid_domains:
      raise ValueError("not a valid domain")
    
    return value
  
  @field_validator("name")
  @classmethod
  def transform_name(cls, value):
    return value.upper()
  

  @field_validator('age', mode='after')
  @classmethod
  def validate_age(cls, value):
    if 0 < value <100:
      return value
    else:
      raise ValueError('age should be greater than 0 and less than 100')



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


patient_info = {'name':'sanoj','email':'abc@icici.com' ,'age':'30','linkedin_url':'http://linkedin.com/1322' ,'weight': 75.2, 'isMarried':True,'allergies':['girls','dust'],  'contact_details':{
   'phone':'100'
}}


patient1 = Patient(**patient_info) # validaton = type coercion

insert_patient_data(patient1)
# update_patient_data(patient1)