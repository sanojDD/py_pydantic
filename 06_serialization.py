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

#temp = patient1.model_dump(include=['name']) # export as dict only the name field
temp = patient1.model_dump(exclude={'address':['state']}) # export as dict only the name field
print(temp)
print(type(temp))
temp1 = patient1.model_dump_json() # export as json
print(temp1)
print(type(temp1))