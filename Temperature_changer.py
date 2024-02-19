def f_to_k (t):
    '''Returns the temperature in kelvin when given in fahrenheit.'''
    n =((t-32)*5/9+273.15)
    return(round(n,3))

f_to_k()
