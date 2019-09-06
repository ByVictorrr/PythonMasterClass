import sqlite3
try:
	import tkinter
except ImportError: # for python 2
	import Tkinter as tkinter


conn = sqlite3.connect("music.sqlite")

class Scrollbox(tkinter.Listbox):

	def __init__(self, window, **kwargs):
		# tktiner.Listbox.__init__(self, windows, **kwargs) # python2 
		super().__init__(window, **kwargs)
		self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)
	
	def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, **kwargs):
		super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan =columnspan, **kwargs)
		self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
		self['yscrollcommand'] = self.scrollbar.set



def get_albums(event):
		"""get_albums: returns a list of albums for a given artist"""
		lb = event.widget
		index = lb.curselection()[0]
		artist_name = (lb.get(index),)
		# get the artist ID from the db row
		albums = []
		for album in conn.execute("SELECT albums.name FROM albums INNER JOIN artists ON artists._id = albums.artist WHERE artists.name = ? ORDER BY albums.name", artist_name):
			albums.append(album[0])
		albumLV.set(tuple(albums))
		songLV.set("Choose an album",)



def get_songs(event):
	lb = event.widget
	index = lb.curselection()[0]
	album_name = (lb.get(index),)
	# get songs from query
	songs = []
	for song in conn.execute("SELECT songs.title FROM songs INNER JOIN albums ON albums._id = songs.album WHERE albums.name = ? ORDER BY songs.title", album_name):
		songs.append(song[0])
	songLV.set(tuple(songs))




mainWindow = tkinter.Tk()

mainWindow.title("Juke Box")
mainWindow.geometry("1024x768")


mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1) # spacer column on right

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ========= labels ==============#
tkinter.Label(mainWindow, text="Artist").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)


#==========Arists Listbox===========#
artistList = Scrollbox(mainWindow)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30,0))
artistList.config(border=2, relief='sunken')

for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
	artistList.insert(tkinter.END, artist[0])

artistList.bind("<<ListboxSelect>>", get_albums)


#==========Albums Listbox===========#
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Select an album",))
albumList = Scrollbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30,0))
albumList.config(border=2, relief='sunken')


albumList.bind("<<ListboxSelect>>", get_songs)

#==========Songs Listbox===========#
songLV = tkinter.Variable(mainWindow)
songLV.set(("Select a song",))
songList = Scrollbox(mainWindow,listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30,0))
songList.config(border=2, relief='sunken')


#==========main looop====================#
albumLV.set((1,2,3,3)) # example to set the variable to it
mainWindow.mainloop()
print("closing data")
conn.close()




