import pandas as pd
from lyricsgenius import Genius
from IPython.core.display import HTML
import api_key
#df = pd.read_json('C:\\Users\\Alfonso\\Dropbox\\python ciencia de datos\\salon.json')
#print(df.to_string())
token= api_key.your_client_access_token

genius = Genius(token)
artist = genius.search_artist("Gorillaz", max_songs=3,sort="title")
print(artist.songs)
song= genius.search_song("feel good inc", artist.name)
print(song.lyrics)




