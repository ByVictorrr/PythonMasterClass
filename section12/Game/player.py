class Player(object):
    
    def  __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0


    def _get_lives(self):
            return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("lives cannot be neggative")
            self._lives = 0
    

    def _get_level(self):
            return self._level

    def _set_level(self, level):
        # see how much to decrease/increase the _score 
        if not (level > 0):
           print("cant go below level one") 
        else:
            x = level - self.level
            self._level = level
            self._score += 1000 * x

        
    level = property(fget=_get_level,fset=_set_level)
    lives = property(fget=_get_lives,fset=_set_lives)

    """ Decarators - alternative for property ()"""
    @property # called a decarator
    def score(self):
        return self._score
    
    
    # _score = property(fget=_get__score,fset=_set__score)
    @score.setter 
    def score(self, score):
        self._score = score

    
    # in java its like the toString method
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0._score}".format(self)
    
    
   
