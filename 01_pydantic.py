def insert_patient_data(name:str, age:int):

  if type(name) == str and type(age) == int:

    if age < 0 :
      raise ValueError('Age cannot be nagative')
    
    else:

      print(name)
      print(age)
      print('inserted into the DB....')

  else:
    raise TypeError('incorrect data type..')
  

def update_patient_data(name:str, age:int):

  if type(name) == str and type(age) == int:

    print(name)
    print(age)
    print('updated into the DB....')

  else:
    raise TypeError('incorrect data type..')



insert_patient_data("sanoj", 30)