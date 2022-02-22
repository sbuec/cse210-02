from random import randint
from operator import gt, lt
OPERATORS = {'higher': gt, 'lower': lt}


class Card:
    '''
    Holds and manages the current_card, new_card, and user_guess.
    '''

    def __init__(self):
        '''current_card and new_card are automatically assigned a value on the creation of an instance.'''
        self.current_card = randint(1,13)
        self.new_card = randint(1,13)
        self.roll_check()

    def roll_new_card(self):
        '''Assigns new_card a new value.'''
        self.current_card = self.new_card
        self.new_card = randint(1,13)
        self.roll_check()
    
    def roll_check(self):
        '''Checks if new_card is equall to current_card. If it is, a new value is assigned to new_card.'''
        same_num = True
        while same_num:
            if self.current_card == self.new_card:
                self.new_card = randint(1,13)
            else:
                same_num = False
    
    def card_guess_check(self, user_guess:str) -> bool:
        '''Checks to see if user_guess is correct.'''
        if OPERATORS[user_guess](self.new_card, self.current_card):
            return True
        else:
            return False