
class Song:
    """ Class to Represent a song
    
    Atrributes:
        title (str): THe title of the song 
        artist (Artist): An artist object representing the songs creator
        duration (int): the Duration of the song in seconds. May be zero

    """
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration
    

class Album:
    """ Class to represent an Album, using its track list
    
    Attributes:
        name (str): The name of the album.
        year (int): The year was album was released.
        artist (Artist): The artist responsible for the album. If not specifed,
        the artist will default to an artist with the name "Various Artist"
        tracks (List[Song]): a list of songs on the album.
       
    Methods:
        add_song: Used to add a new song to the album's track list
    """
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        self.artist = artist
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to the track list

        Args:
            song (Song): A song to add.
            position (Optional[int]): if specified, the song will be added to that postion
                in the track list - inserting it between other songs if necessarys.
                Otherwise, the song will be added to the end of the list.
        """

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.
    
    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection, it is 
            not an exhaustive list of the artist's published albums.
        
    Methods:
        add_album: Use to add a new album to the artist's albums list
    """
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not added again.
        """
        self.albums.append(album)

def find_object(field, object_list):
    for item in object_list:
        if item.name == field:
            return item
    return None
    
    
def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))
            
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # We have just read details for a new arrist
                # retrive the artist object if there is one,
                # otherwise create a new artist object and add it to the artist list.
                new_artist = find_object(artist_field, artist_list)
                if(new_artist is None):
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None


            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # We've just read a new album for the current artist
                # Retrieve the album object if there is one,
                # ohterwise create a new object and store it in the artist's collection
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # Create a new song object and add it to the current albums's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)
                
        # After reading the last line of the text file, we will have an artist and album that havent been store
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list




def create_check_file(artist_list):
    """Creates a check file from the object data for comparison with the original file"""
    with open("checkFile.txt","w") as checkFile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for song in new_album.tracks:
                    # data row should consist of (artist, album, year, song)
                    print("{}\t{}\t{}\t{}".format(new_artist.name, new_album.name, new_album.year, song.title),file=checkFile)
    

if __name__ == "__main__":
    artists = load_data()
    print("There are {} artist".format(len(artists)))
    create_check_file(artists)
