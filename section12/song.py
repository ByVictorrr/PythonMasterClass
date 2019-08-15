class Song:
    """ Class to Represent a song
    
    Atrributes:
        title (str): THe title of the song 
        artist (Artist): An artist object representing the songs creator
        duration (int): the Duration of the song in seconds. May be zero

    """
    def __init__(self, title, article, duration=0):
        """Song init Method

        Args:
            title (str):  Initaiates  the 'title' attribute
            artist (Artist): At Artist object representing the song's creator.
            duration (Optional[int]): Iniital value for the 'duration' attribute.
                Will defualt to zero if not specified
    
        """

        self.title = title
        self.artist = artist
        self.duration = duration
    
#help(Song)    
#help(Song.__init__)
print(Song.__doc__)
print(Song.__init__.__doc__)
    
    