def bibformat(author,title,city,publisher,year): 
    '''returns a string of the form of a citation'''
    result = f'{author} ({year}). {title}. {city}: {publisher}.'
    return (result)

######################################################################
def bibformat_display():
    ''' prompts the user for a book title, name of the author, year of 
    publication, publisher and the headquarter city of the publisher. The 
    function should then print the information about the book in the same format
    as bib_format()'''
    title = str(input("Enter the book title:  "))
    author = str(input("Enter the author of the book:  "))
    year = int(input("Enter the year the book was published:  "))
    publisher = str(input("Enter the name of the publisher:  "))
    city = str(input("In what city are the headquarters:  "))
    x = bibformat(author,title,city,publisher,year)
    return (x)
