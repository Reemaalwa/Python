def cad_cashier(price,payment):
    '''takes two real nonnegative numbers with two decimal
    places as input, where payment>=price and where the 
    second decimal in payment is 0 or 5. They represent 
    a price and payment in Canadian dollars. The function 
    should return a real number with 2 decimal places 
    representing the change the customer should get in 
    Canadian dollars.'''
    c= payment - price
    yourChange= round( 0.05 * round (c/0.05),2 )
    return (yourChange)

######################################################################
def min_CAD_coins(price,payment):
    ''' returns five numbers (t,l,q,d,n) that represent 
    the smallest number of coins 
    (toonies, loonies, quarters, dimes, and nickels) 
    that add up to the amount owed to the customer '''
    change = cad_cashier (price, payment)
    toonie = int(change/2)
    twos= toonie*2
    loonie = int(change-twos)
    quarters = int((change - (twos+loonie))/0.25)
    twentyFive = quarters*0.25
    dimes = int((change-(twos+loonie+twentyFive))/0.1)
    tens = dimes*0.1
    remainder = round(change-(twos+loonie+twentyFive+tens),2)
    nickels = int(remainder/0.05)
    giveBack = (toonie, loonie, quarters, dimes, nickels)
    return (giveBack)
