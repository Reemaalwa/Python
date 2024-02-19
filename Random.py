def impl2loz(w):
    ''' takes a non-negative number "w"as input and returns a pair of numbers
    (l,o) such that "w = l + o/16" and "l" is an integer and o is a 
    non-negative number smaller than 16.'''
    import random
    o = random.randint(0, 15)
    l = w - o /16
    return (l, o)

######################################################################
def pale(n):
    '''takes a positive integer n as input where n has four digits. 
    The function determines if n is a pale number. A number is not pale if 
    and only if it has at least two consecutive digits each equal to 3, or
    if its last digit is divisible by 4. THe function returns in a boolean value'''
    first = int(n/1000)
    thousands = first*1000
    second = int((n-(thousands))/100)
    hundreds = second *100 
    third = int((n-thousands-hundreds)/10)
    tens = third *10
    fourth = n-(thousands+hundreds+tens)
    return ((fourth%4==0 or first + second == 3 or second + third ==3 or third + fourth ==3) is False)

######################################################################
def compound(x,y,z):
    '''takes three integers x, y and z and returns "True" if x is the only 
    even number among the 3 integers and if at least one pair of the three 
    integers adds up to a number greater than 100, otherwise false'''
    return((int(x)%2== 0 and not int(y)%2==0 and not int(z)%2==0) and (x+y>100 or y+z>100 or x+z>100 )is True)

######################################################################
def funct(p):
    '''takes a positive number 'p' (greater or equal to 11) and 
    solves the following equation (5^(r^2)-p+10=0) for r and prints the
    sentence “The solution is r”, where r is replaced by the number that 
    solves the equation for the given p.'''
    import math
    r = math.sqrt((math.log(p-10,5)))
    return(print(f"the solution is {r}"))

######################################################################
def gol(n):
    ''' takes a number, n, where n is bigger or equal to 1, and returns the
    minimum number of times that n needs to be divided by 2 in order to get
    a number equal or smaller than 1.'''
    import math
    t=math.log(n,2)
    return(math.ceil(t))