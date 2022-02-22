def display_info(is_guess_stage:bool, current_card:int, new_card:int=None, user_guess:str=None, score:int=None):
    '''
    Displays the current game information.
    '''
    if is_guess_stage:
        print(f'Current Card: {current_card}')
        print(f'Your Score: {score}')
    else:
        print(f'Current Card: {current_card}')
        print(f'Your Guess: {user_guess}')
        print(f'Next Card Was: {new_card}')
        print(f'Your Score: {score}')
