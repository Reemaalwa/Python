def is_up_monotone(X, d):
    cutBy = int(d)
    strlen = len(X)
    i = 0
    result = X[i:i+cutBy]
    answer = True
    while i+cutBy < strlen:
        current_str = X[i:i+cutBy]
        next_str = X[i+cutBy:i+2*cutBy]
        result =  result +', '+ next_str
        current = int(current_str)
        next = int(next_str)
        if current > next:
           answer = False
        elif len(X)% cutBy !=0:
            answer = False               
        i= i + cutBy
    print(result)
    return answer

print(f'''*******************************************
*                                         *
*    Welcome to my up-monotone inquiry    *
*                                         *
*******************************************''')
name=input("What is your name? ")
print(f'''**************************************************
*                                                *
*    {name} Welcome to my math quiz-generator    *
*                                                *
************************************************''')
flag=True
while flag:
    import random
    question=input(name+", would you like to test if a number admits an up-monotone split of given size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
        print(f'''****************************************
*                                       *
*                                       *
*      _ _Good bye {name}!_ _           *
****************************************''')
    elif question=='yes':
        flag=True
        print(f'Good choice!')
        X = input(f'Enter a positive integer: ')
        if not X.isdigit():
            print(f'The input can only contain digits. Try again.')
        elif not int(X) > 0:
            print(f'The input has to be a positive integer. Try again.')
            continue
        else:
            d= int(input(f'Input the split. The split has to divide the length of {X} i.e {random.randint(1,9)}'))
            lenX=int(len(X))
            if lenX% d !=0:
                print(f'{d} does not divide {X}')
                continue
            result = is_up_monotone(X,d)
            if result:
                print(f'The funtion is up-monotone' )
            else:
                print(f'The funtion is not up-monotone')
    else:
        print(f'Please enter yes or no. Try again.')
        question
    
    