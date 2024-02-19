# In this implementation a item (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each item of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_items(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the items from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     for i, item in enumerate(deck):
         if i%2==0:
             dealer.append(item)
         else: 
             other.append(item)
     return (dealer, other)


import random
def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are items represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    def count_occurrences(rank, ranks_list):
        return sum(1 for r in ranks_list if r == rank)

    ranks_list = [item[:-1] if len(item) == 3 else item[0] for item in l]
    
    for card in l:
        rank = card[:-1] if len(card) == 3 else card[0]
        
        if rank in ranks_list: 
            if count_occurrences(rank, ranks_list) % 2 == 1 and card not in no_pairs:
                no_pairs.append(card)
            while rank in ranks_list:
                ranks_list.remove(rank)
    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    print(' '.join(deck))
    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     while True:
         user_input=int(input(f'Give me an integer between 1 and {n}: '))
         if 1 <= user_input <= n:
             return user_input
         else:
             print(f'invalid input. Please eneter a number between 1 and {n}: ')

def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_items(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my item game!")
     print("Your current deck of items is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your items")

     print("Now discarding all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE
     while human and dealer:
        print(f'''Your turn.
        Your current deck of items is:''')
        print_deck(human)
        print(f'I have {len(dealer)} cards. If 1 stands for my first item and {len(dealer)} for my last card, which of my cards would you like?')
        item_choice = get_valid_input(len(dealer))
        chosen = dealer.pop(item_choice - 1)
        human.append(chosen)
        print(f'''You asked for my {item_choice}th card. 
        Here it is. It is {chosen}
        with {chosen} added, your current deck of cards is:''')
        print_deck(human)
        print(f'And after discarding pairs and shuffling, your deck is:')
        human = remove_pairs(human)
        print_deck(human)
        wait_for_player()

        if dealer:
            print(f'My turn.')
            dealer_item_choice = random.randint(0,len(human)-1)
            dealer_chosen = human.pop(dealer_item_choice)
            dealer.append(dealer_chosen)
            human = remove_pairs(human)
            dealer = remove_pairs(dealer)
            print(f'I took your {dealer_item_choice}th card.')
            print_deck(human)
            wait_for_player()
     if not human:
         print(f'''Ups. You do not have any more cards
               Congratulations! You, Human, Win''')
     elif not dealer:
         print(f'''I have no more cards.
               You lost!, I, Robot, win.''')
	 

# main
play_game()

