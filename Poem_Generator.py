def poem_generator():
    '''prompts the user for the name and city of birth and then prints a 
    poem that includes that name and city of birth'''
    name = str (input("What is your name?"))
    city = str (input("What city is your place of birth?"))
    print ( f'''
      There was human called {name}
      {name} was born in  {city},  
      {name} was sad in  {city},  
      But {name} moved to ottawa! 
      {name} became so happy! 
    ''')

poem_generator()
