""" 

Ce script importe les données csv issues des différentes bases disponibles 
dans le dossier data et leur effectue en partie un traitement préliminaire. 
Les objets créées ici seront appelées dans le script Fonctions.

"""

import pandas as pd
import re

"Importation des données"

df_artists=pd.read_csv("../Data/artists.csv")
df_top200=pd.read_csv("../Data/spotify_top200_global.csv")
df_tracks=pd.read_csv("../Data/tracks.csv")

"Copie"
artists = df_artists.copy()
top200 = df_top200.copy()
tracks = df_tracks.copy()

"Nettoyage"

"On remplace les valeurs manquantes"
artists.fillna({'followers': 0}, inplace = True)
tracks.fillna({'name': 'Nom de la chanson inconnu'}, inplace = True)

"Format colonne artists"
tracks['artists'] = tracks['artists'].str.replace(r'[^a-z0-9\s]','', regex = True, flags = re.IGNORECASE)

"Changer format de release_date"
tracks["release_date"]=pd.to_datetime(tracks["release_date"], format = "%Y-%m-%d")
tracks["release_year"]=tracks["release_date"].dt.year


"Artistes et leurs nombre de chansons dans le top 200 global de 2020"
top_artists = pd.DataFrame(top200.groupby('Artist')['Title']
                           .nunique().sort_values(ascending = False).reset_index(name = 'Count'))

"Convertir les chaines de caractère des df en minuscules pour un meilleur appariement lorsque l'utilisateur entre une chaine de caractère dans l'interface"
artists['name'] = artists['name'].str.lower()
tracks['artists'] = tracks['artists'].str.lower()
top200['Artist'] = top200['Artist'].str.lower()
top_artists['Artist'] = top_artists['Artist'].str.lower()
artists['genres'] = artists['genres'].str.lower()

"On crée un nouveau dataframe pour éviter le problème de doublon avec les artistes"
artists_unique = artists.groupby(['name']).max('followers').reset_index()


