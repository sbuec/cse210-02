def process_guess(display_msg:str) -> str:
    '''
    Takes in and checks player input for incorrect input.\n
    Returns player input.
    '''
    while True:
        user_input = input(f'{display_msg}').lower()
        
        if user_input.lower() == 'h' or user_input.lower() == 'higher':
            return 'higher'
        elif user_input.lower() == 'l' or user_input.lower() == 'lower':
            return 'lower'
        else:
            print('You did not enter an accepted input, please try again.')