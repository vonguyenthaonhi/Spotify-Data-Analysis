import pandas as pd 
import datetime as dt
import re

"Importation des fichiers"


df_artists=pd.read_csv(".../Data/artists.csv")
df_top200=pd.read_csv(".../Data/spotify_top200_global.csv")
df_tracks=pd.read_csv(".../Data/tracks.csv")

"copy"
artists = df_artists.copy()
top200 = df_top200.copy()
tracks = df_tracks.copy()

"Nettoyage"

"On remplace les valeurs manquantes"
artists.fillna({'followers': 0}, inplace = True)
tracks.fillna({'name': 'Nom de la chanson inconnu'}, inplace = True)

#Format column artists 
tracks['artists'] = tracks['artists'].str.replace(r'[^a-z0-9\s]','', regex = True, flags = re.IGNORECASE)


#Changer format de release_date 
tracks["release_date"]=pd.to_datetime(tracks["release_date"], format = "%Y-%m-%d")
tracks["release_year"]=tracks["release_date"].dt.year
tracks.head() # on vérifie que la nouvelle colonne existe

#Nom d'artiste unique pour éviter les doublons
artists_unique = artists.groupby(['name']).max('followers').reset_index()

#Artistes et son nombre de chansons dans le top 200 global de 2020
top_artists = pd.DataFrame(top200.groupby('Artist')['Title'].nunique().sort_values(ascending = False).reset_index(name = 'Count'))

#pour éviter le probleme de minuscule/majuscule
artists['name'] = artists['name'].str.lower()
artists_unique['name'] = artists_unique['name'].str.lower()
tracks['artists'] = tracks['artists'].str.lower()
top200['Artist'] = top200['Artist'].str.lower()
top_artists['Artist'] = top_artists['Artist'].str.lower()
tracks['name'] = tracks['name'].str.lower()
artists["genres"] = artists["genres"].str.lower()


"Question 1"

def Artiste_info ():
    
    """
    Cette fonction va demander au utilisateur un nom d'artiste 
    Elle enverra le résultat si l'artiste existe dans le dataframe
    output: son nombre d'abonnés, ses 3 chansons plus populaires et 3 chansons plus récentes, 
            son nombre de chansons dans le top 200 global de 2020
    """
    
    #Demander le nom d'artiste
    nom_artiste = input(str("Saisir le nom d'artiste: ")).lower()
    
    #Verifier si le nom d'artiste saisi existe dans artists_unique
    if nom_artiste not in artists_unique.values and nom_artiste not in tracks.values:
        print("Il y a aucune information de cet artiste")
    #Resultats
    else:
        #nombre d’abonnés
        print('Le nombre d’abonnés est', int(artists_unique.loc[artists_unique['name'] == nom_artiste, 'followers']))
        
        #3 chansons plus populaires
        top_chansons_populaires = tracks.loc[tracks['artists']== nom_artiste].sort_values('popularity',ascending = False)
        print('Les 3 chansons les plus populaires sont', top_chansons_populaires.iloc[0,1], ',', top_chansons_populaires.iloc[1,1], ',', top_chansons_populaires.iloc[2,1]) 
        
        #3 chansons plus récentes
        top_chansons_recentes = tracks.loc[tracks['artists']== nom_artiste].sort_values('release_date',ascending = False)
        print('Les 3 chansons les plus récentes sont', top_chansons_recentes.iloc[0,1], ',', top_chansons_recentes.iloc[1,1], ',', top_chansons_recentes.iloc[2,1])
        
        #Verifier si l'artiste a au moins 1 chanson dans le top 200 global de 2020
        if nom_artiste not in top200.values:
            print(nom_artiste.title(), 'n’a aucune chanson dans le top 200 global de 2020')
        else: 
            #si oui, nombre de chansons 
            artiste_top200 = top_artists.loc[top_artists['Artist'] == nom_artiste]
            print('Le nombre de chansons que',nom_artiste.title(), 'a dans le top 200 global de 2020 est', str(top_artists.iloc[0,1]))
        
Artiste_info()

"Question 2"
def song():
    
    """
    Cette fonction va demander au utilisateur un nom de chanson et enverra jusqu'à 20 résultats 
    selon la popularité
    output: 20 chansons ordonnées par popularité décroissante
    """
    
    #Demander le nom de chanson
    titre = input(str("Saisissez le titre d'une chanson : ")).lower()
    
    #verifier si la chanson existe 
    recherche=tracks.loc[tracks['name']==titre,['name','artists','popularity']]  
    if recherche.empty :
        print("Aucune chanson trouvée.")
    else :
        #20 chansons, si plusieurs fois la même alors afficher la plus populaire seulement
        chanson_unique = recherche.groupby(['name', 'artists']).agg({'popularity':'max'}).reset_index()
        print("Voici les chansons trouvées : ")
        print(chanson_unique.head(20).sort_values(by='popularity',ascending=False))
        
song()


"Question 3"
def Angenre():
    
    """
    Cette fonction va demander au utilisateur de saisir une année et un genre 
    et enverra tous les chansons correspondant ordonnées par popularité d'artistes
    output: chansons correspondant ordonnées par popularité d'artistes
            en cas où il y a plusieurs chansons pour un même artiste, 
            les ordonnées par popularité de chansons
    """
    
    #Demander l'année et le genre
    annee = float(input("Saisir une année : "))
    genre = input("Saisir un genre : ").lower()
    
    
    #Merge
    fusion = pd.merge(tracks, artists, left_on = "artists", right_on = "name", how = "inner" )
    #enlever doublons id titre
    fusion_unique = fusion.drop_duplicates(subset = ['id_x']) 
    
    #Verifier si l'l'année et le genre saisis existent

    if annee not in fusion_unique.values or genre not in fusion.values:
        print("Aucune chanson trouvée.")
    else :
        #resultat
        print("Voici les chansons trouvées : ")
        #filtre
        res = fusion_unique.loc[(fusion_unique['genres'].str.contains(genre)) & (fusion_unique['release_year'] == annee), ['name_x', 'artists', 'popularity_y', 'popularity_x']]
        print(res.sort_values(by=['popularity_y', 'popularity_x'],ascending=False))
        
Angenre()
