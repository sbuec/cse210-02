class Score:
    '''
    Holds and manages the players score.
    '''

    def __init__(self, starting_score:int, point_gain:int, point_loss:int):
        self.score = starting_score
        self.p_gain = point_gain
        self.p_loss = point_loss
    
    def remove_points(self):
        '''Removes a set amount of points from the player score.'''
        self.score -= self.p_loss
    
    def add_points(self):
        '''Adds a set amount of points to the player score.'''
        self.score += self.p_gain
    
    def is_zero(self) -> bool:
        '''Checks if the player score is Zero.'''
        if self.score <= 0: return True
        else: return False