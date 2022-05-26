import json
from lyricsgenius import Genius
from IPython.core.display import HTML
import api_key
import requests
import pandas as pd
#from IPython.core.display import HTMLget_image_html()
#df = pd.read_json('C:\\Users\\Alfonso\\Dropbox\\python ciencia de datos\\salon.json')
#print(df.to_string())
token= api_key.your_client_access_token


client_access_token= api_key.your_client_access_token


search_term = "Gorillaz"
genius_search_url = f"http://api.genius.com/search?q="+search_term+"m&access_token="+client_access_token
#print(genius_search_url)
response = requests.get(genius_search_url)
json_data = response.json()

#print(json_data['response']['hits'][0])

#Obtener títulos de canciones
#for song in json_data['response']['hits']:
 #   print(song['result']['full_title'])
#Obtener mosaicos de canciones y recuentos de páginas  vistas
print("_________________________")

#for song in json_data['response']['hits']:
 #  print(song['result']['full_title'], song['result']['stats'])


missy_songs = []
for song in json_data['response']['hits']:
    missy_songs.append([song['result']['full_title'], song['result']['stats']
    ['pageviews']])
#Make a Pandas dataframe from a list
missy_df = pd.DataFrame(missy_songs)
missy_df.columns = ['song_title', 'page_views']
print(missy_df)
print("_____________________________")

def get_image_html(link):
    image_html = f"<img src='{link}' width='500px'>"
    return image_html
missy_songs = []
for song in json_data['response']['hits']:
    missy_songs.append([song['result']['full_title'], song['result']['stats']
    ['pageviews'], song['result']['song_art_image_url']])
missy_df = pd.DataFrame(missy_songs)
missy_df.columns = ['song_title', 'page_views','album_cover_url']
#Use the function get_image_html()
missy_df['album_cover'] = missy_df['album_cover_url'].apply(get_image_html)
print(missy_df)

HTML(missy_df[['album_cover', 'page_views', 'song_title']].to_html(escape=False))