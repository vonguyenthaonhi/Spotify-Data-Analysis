""" 

Ce script introduit les fonctions nécéssaires à l'utilisation de l'interface Tkinter. 
Les fonctions créées ici seront alors appelées dans le script Main (interface).

"""


import pandas as pd 
from tkinter import *
from tkinter import ttk
import webbrowser
from traitement_data import artists_unique, tracks, top200, top_artists, artists, df_artists


def Artiste_info(name,afficher_resultat):
    
    """
    La fonction Artiste_info prend en argument un nom d'artiste, et 
    un widget où apparaît l'output.
    
    Elle renvoie:
        son nombre d'abonnés, 
        ses 3 chansons les plus appréciées, 
        ses 3 chansons les plus récentes,
        le nombre de chansons qu'il possède dans le top 200 global de 2020.
    """
    
    #On récupère le nom d'artiste saisi
    nom_artiste = name.get().lower()
    
    #Verifier si le nom d'artiste saisi existe dans artists_unique
    if (nom_artiste not in artists_unique.values and nom_artiste not in tracks.values) or (nom_artiste==""):
        afficher_resultat.delete("2.0", END)
        afficher_resultat.insert(END,"\n Il n'y a pas d'informations pour ce nom d'artiste. \n")
        
    #Resultats
    else:
        #nombre d’abonnés
        nombre_abonnes = artists.loc[artists['name'] == nom_artiste, 'followers']
        #convertir en string
        nombre_abonnes = nombre_abonnes.to_string(index = False)
        afficher_resultat.delete("2.0", END)
        afficher_resultat.insert(END, f'\n Le nombre d’abonnés est {nombre_abonnes} \n')
        
        #Les 3 chansons les plus populaires
        top_chansons_populaires = tracks.loc[tracks['artists']== nom_artiste].sort_values('popularity',ascending = False)
        afficher_resultat.insert(END, f'Ses 3 chansons les plus populaires sont :\n {top_chansons_populaires.iloc[0,1].title()}, {top_chansons_populaires.iloc[1,1].title()}, {top_chansons_populaires.iloc[2,1].title()} \n')
      
        #Les 3 chansons les plus récentes
        top_chansons_recentes = tracks.loc[tracks['artists']== nom_artiste].sort_values('release_date',ascending = False)
        afficher_resultat.insert(END, f'Ses 3 chansons les plus populaires sont :\n {top_chansons_recentes.iloc[0,1].title()}, {top_chansons_recentes.iloc[1,1].title()}, {top_chansons_recentes.iloc[2,1].title()} \n')
    
              
        #Verifier si l'artiste a au moins 1 chanson dans le top 200 global de 2020
        if nom_artiste not in top200.values:
            afficher_resultat.insert(END,str(nom_artiste.title()) + 
                       ' n’a aucune chanson dans le top 200 global de 2020.\n')
        else:
            #si oui, nombre de chansons 
            artiste_top200 = top_artists.loc[top_artists['Artist'] == nom_artiste]
            afficher_resultat.insert(END,str(nom_artiste.title()) + ' a ' + str(artiste_top200.iloc[0,1]) + ' chanson(s) dans le top 200 de 2020. \n')
                      

def song(song_name, afficher_resultat):
    
    """
    La fonction song prend en argument un nom de chanson, et un widget 
    où apparaît l'output.
    
    Elle renvoie:
        la ou les chansons possédant ce nom.
    """
    
    #On récupère le nom de chanson saisi
    nom_chanson = song_name.get().lower()
    
    #Vérifier si la chanson existe 
    tracks['name'] = tracks['name'].str.lower()
    recherche=tracks.loc[tracks['name'] == nom_chanson,['name','artists','popularity']]  
    if recherche.empty :
        afficher_resultat.delete("2.0", END)
        afficher_resultat.insert(END, "\n Aucune chanson trouvée.\n")
    else :
        #filtre
        chanson_unique = recherche.groupby(['name', 'artists']).agg({'popularity':'max'}).reset_index()
        resultat = chanson_unique.head(20).sort_values(by='popularity',ascending=False)
        #afficher que titre et nom d'artiste
        resultat = resultat[['name','artists']]
        #changer le nom de colonnes
        resultat.columns = ['Titre', 'Artistes']
        #resultat
        afficher_resultat.delete("2.0", END)
        afficher_resultat.insert(END,  f"\n Voici les chansons trouvées qui correspondent à {nom_chanson.title()}: \n")
        afficher_resultat.insert(END, resultat.to_string(index=False,col_space = 35, justify = 'center'),'\n')
       
        

def Angenre(date,style, afficher_resultat):
    
    """
    La fonction Angenre prend en argument une année, un genre musical, 
    et un widget où apparaît l'output.
    
    Elle renvoie:
        les chansons correspondant au genre et à l'année saisie,
        ordonnées par popularité d'artiste.
    """
    
    #On récupère l'année et le genre saisis
    annee = date.get()
    genre = style.get().lower()
    
    #Merge
    fusion = pd.merge(tracks, artists, left_on = "artists", right_on = "name", how = "inner" )
    #enlever doublons id titre
    fusion_unique = fusion.drop_duplicates(subset = ['id_x']) 
    
    
    #Verifier si l'l'année et le genre saisis existent
    if annee not in fusion_unique.values or genre not in fusion.values:
        afficher_resultat.delete("2.0", END)
        afficher_resultat.insert(END, "\n Aucune chanson trouvée.\n")
    else :
        #filtre
        res = fusion_unique.loc[(fusion_unique['genres'].str.contains(genre)) & (fusion_unique['release_year'] == annee), ['name_x', 'artists', 'popularity_y', 'popularity_x']]
        res_trier = res.sort_values(by=['popularity_y', 'popularity_x'],ascending=False)
        #afficher que titre et nom d'artiste
        res_trier = res_trier[['name_x', 'artists']]
        #changer le nom de colonnes
        res_trier.columns = ['Titre','Artistes']
        #resultat
        afficher_resultat.delete("2.0", END)
        afficher_resultat.insert(END,  "\n Voici les chansons trouvées: \n")
        afficher_resultat.insert(END, res_trier.to_string(index=False, justify = ['left', 'right'], max_colwidth = 25, col_space = 40),'\n')


def lien_wikipedia (name):
    
    """ 
    
    fonction qui permet d'afficher la page wikipedia 
    de l'artiste saisi dans l'interface (boite 1)
    
    """
    #On récupère le nom d'artiste saisi
    nom_artiste = name.get()
    
    df_artists['name'] = df_artists['name'].str.lower()
    nom_artiste_maj = nom_artiste.strip().title()
    url_wiki = "https://fr.wikipedia.org/wiki/{}"
    
    if nom_artiste_maj.lower() in df_artists['name'].values : 
        webbrowser.open(url_wiki.format(nom_artiste_maj.replace(" ", "_")))
    
        
  
# Afficher le lien de la page spotify de l'artiste saisi
def lien_artiste_spotify (name):
    
    """ 
    
    fonction qui permet d'afficher la page spotify 
    de l'artiste saisi dans l'interface (boite 1)
    
    """
    
    nom_artiste = name.get().lower() 
    id_artiste = df_artists.loc[df_artists['name']==nom_artiste,'id'].iloc[0]
    url_spotify = "https://open.spotify.com/intl-fr/artist/{}"
    webbrowser.open(url_spotify.format(id_artiste))
    


def link_spotify():
    
    """ 
    fonction qui permet d'ouvrir la page d'accueil de Spotify
    
    """
    
    url = "https://open.spotify.com/intl-fr"
    webbrowser.open(url)










