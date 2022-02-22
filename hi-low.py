'''
Author: Eric Woll, Daniel Jones, Steven Buechele, Connor Baltich
Assignment: Week 3 Hilo
'''

from operator import gt, lt
from os import system
from time import sleep

import Process_guess as pguess
import Display_info as dinfo
import Score 
import Card


POINT_GAIN = 100
POINT_LOSS = 75

# gt -> Greator Than | lt - > Less Than
OPERATORS = {'higher': gt, 'lower': lt}

YES_LIST = ['yes', 'ye', 'y']
NO_LIST = ['no', 'n']


def clear():
    '''Clears the Terminal.'''
    system('cls')   


def main():
    STARTING_SCORE = 300

    player_score = Score.Score(STARTING_SCORE, POINT_GAIN, POINT_LOSS)
    game_cards = Card.Card()

    run = True
    while run:
        user_guess = ''
        while user_guess == '':
            dinfo.display_info(is_guess_stage=True, current_card=game_cards.current_card, score=player_score.score)
            user_guess = pguess.process_guess('Next card: higher (h) or lower (l)? ')
            clear()

        is_correct_guess = game_cards.card_guess_check(user_guess)

        if is_correct_guess:
            player_score.add_points()
        else:
            player_score.remove_points()
    
        again = ''
        while again == '':

            if is_correct_guess:
                print('Correct, you now have 100 more points!\n')
            else:
                print('Incorrect, you have lost 75 points.\n')

            dinfo.display_info(is_guess_stage=False, current_card=game_cards.current_card, new_card=game_cards.new_card,
            user_guess=user_guess, score=player_score.score)
            print()
            
            if not player_score.is_zero():
                again = input('Would you like to continue (y/n)? ').lower()
            else:
                print('Your score is Zero, you lost!')
                sleep(3)

            if again in NO_LIST or player_score.is_zero():
                run = False
                again = 'False'
                clear()
                print('Thank you for playing!')
                print(f'Your score: {player_score.score}')
                sleep(3)
            elif again not in YES_LIST:
                again = ''

        clear()
        game_cards.roll_new_card()


if __name__ == '__main__':
    main()
