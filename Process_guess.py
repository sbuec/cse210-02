def process_guess(display_msg:str) -> str:
    '''
    Takes in and checks player input for incorrect input.\n
    Returns player input.
    '''
    user_input = ''
    try:
        user_input = input(f'{display_msg}').lower()
        
        if user_input == 'h' or user_input == 'higher':
            user_input = 'higher'
        elif user_input == 'l' or user_input == 'lower':
            user_input = 'lower'
        else:
            user_input = ''
            raise ValueError

    except (ValueError, KeyError):
        print('You did not enter an accepted input, please try again.')
        sleep(3)
        
    return user_input