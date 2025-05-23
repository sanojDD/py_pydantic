from pydantic import BaseModel


class Address(BaseModel):
  city:str
  state:str
  pin:str


class Patient(BaseModel):
  name:str
  gender:str
  age:int
  address:Address

address_list = {'city':'brt', 'state':'koshi', 'pin':'007'}

address1 = Address(**address_list)

patient_list = {'name':'sanoj', 'gender':'male', 'age':35, 'address':address1}

patient1 = Patient(**patient_list)

print(patient1)
print(patient1.name)
print(patient1.address.city)