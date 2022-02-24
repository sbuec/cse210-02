def process_guess(display_msg:str) -> str:
    '''
    Takes in and checks player input for incorrect input.\n
    Returns player input.
    '''
    validInput = False
    user_input = ''
    while not validInput:
        user_input = input(f'{display_msg}').lower()
        
        if user_input.lower() == 'h' or user_input.lower() == 'higher':
            validInput = True
            user_input = 'higher'
        elif user_input.lower() == 'l' or user_input.lower() == 'lower':
            validInput = True
            user_input = 'lower'
        else:
            print('You did not enter an accepted input, please try again.')
    
    return user_input