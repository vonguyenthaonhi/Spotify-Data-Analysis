""" 

Ce script permet de faire tourner l'ensemble de notre code et donc notre interface.
Il importe les fonctions du module "Fonctions".

"""
from tkinter import * 
from tkinter import scrolledtext
from PIL import Image, ImageTk
import Fonctions as f


# Création de l'interface
fenetre = Tk()
fenetre.geometry("1000x500")
fenetre.resizable(width=False, height=False)
fenetre.title('Spotify Stats')
vert_spotify = '#348f43'

#mettre une photo en arrière plan

image_bg = Image.open("Images/spotify_background.png")
# Redimensionner l'image
image_bg = image_bg.resize((1000, 500))
#rendre l'image transparente
image_bg.putalpha(200)
# Convertir l'image retouchée en format Tkinter PhotoImage
image_bg = ImageTk.PhotoImage(image_bg)
# Création d'un Canvas avec les dimensions de l'image
canvas1 = Canvas(fenetre, width=1000, height=500)
canvas1.pack(fill="both", expand=True)
# Affichage de l'image redimensionnée
canvas1.create_image(0, 0, image=image_bg, anchor="nw")



# Titre
label_titre = Label(fenetre, text='Bienvenue sur Spotify stats!', font=("Montserrat",20, "italic bold underline"), fg='white', bg=vert_spotify)
label_titre.place(x=150,y=20)

# Bouton avec une image qui renvoit sur Spotify quand on clique dessus 
image = Image.open("Images/listenonspotifylogo.png")
image = image.resize((310, 55))  
photo = ImageTk.PhotoImage(image)
bouton_Spotify = Button(fenetre, image=photo,bg=vert_spotify, command=f.link_spotify)
bouton_Spotify.place(x=648, y=25)

#Definition des variables entrées par l'utilisateur 
artiste = StringVar()
chanson = StringVar()
annees = IntVar()
genres = StringVar()

annees.set("")


#boites de "recherhe"
#Les boites contiennent des labels, des entrées et des boutons 
#qui appellent des fonctions du script "Fonction" via des focntions anonymes

#boite1 pour rechercher l'artiste
boite1 = Frame(fenetre, bg=vert_spotify)
boite1.place(x=20, y=100)
label1 =Label(boite1, text="Artiste: ", bg=vert_spotify, font=("Montserrat", 10, "italic bold"))
label1.pack(side='left', padx= 5)
entree1=Entry(boite1, textvariable = artiste)
entree1.pack(side='left', padx= 5)
bouton1=Button(boite1, text="Valider", command= lambda: f.Artiste_info(artiste, resu1))
#résultat de la fonction apparait dans une listbox (cf ci-dessous)
bouton1.pack(side='left', padx= 5)

#boutons pour les liens wikipédia et spotify de l'artiste 
bouton_wiki = Button(boite1, text='Rechercher sur Wikipedia', command = lambda: f.lien_wikipedia(artiste))
bouton_wiki.pack(side='left')
bouton_lien_spotify = Button(boite1, text='Ouvrir sur Spotify', bg='white', command = lambda: f.lien_artiste_spotify(artiste))
bouton_lien_spotify.pack(side='left', padx=5)

#boite2 pour rechercher une chanson 
boite2 = Frame(fenetre, bg=vert_spotify)
boite2.place(x=20, y=140)
label2 =Label(boite2, text="Nom chanson: ", bg=vert_spotify, font=("Montserrat", 10, "italic bold"))
label2.pack(side='left', padx=5)
entree2=Entry(boite2, textvariable = chanson)
entree2.pack(side='left', padx=5)
bouton2=Button(boite2, text="Valider", command = lambda: f.song(chanson,resu2))
bouton2.pack(side='left')

#boite3 pour rechercher une année  
boite3 = Frame(fenetre, bg=vert_spotify)
boite3.place(x=20, y=180)
label3 =Label(boite3, text="Année: ", bg=vert_spotify, font=("Montserrat", 10, "italic bold"))
label3.pack(side='left', padx=5)
entree3=Entry(boite3, textvariable = annees)
entree3.pack(side='left', padx=5)

#boite4 pour rechercher un genre de musique (boite 3 et 4 sont associées à la même fonction et donc au même bouton)
boite4 = Frame(fenetre, bg=vert_spotify)
boite4.place(x=20, y=210)
label4 =Label(boite4, text="Et genre musical: ", bg=vert_spotify, font=("Montserrat", 10, "italic bold"))
label4.pack(side='left', padx=5)
entree4=Entry(boite4, textvariable = genres)
entree4.pack(side='left', padx=5)
bouton3=Button(boite4, text="Valider", command = lambda: f.Angenre(annees, genres, resu3))
bouton3.pack(side='left')


#Widget "resu1" pour afficher les résultats de la fonction "Artist_info"
resu1 = scrolledtext.ScrolledText(fenetre, width = 50, height = 11, bg='#7bef94', font=("Montserrat", 8, "italic bold"))
resu1.place(x=648, y=100)
resu1.insert('1.0', "Résultats quand vous saisissez  un nom d'artiste \n")

#Widget "resu2" pour afficher les résultats de la fonction "song"
resu2 = scrolledtext.ScrolledText(fenetre, width = 65, height = 12, bg='#7bef94', font=("Montserrat", 8, "italic bold"))
resu2.place(x=555, y = 300)
resu2.insert('1.0', "Résultats quand vous saisissez  un titre \n")

#Widget "resu3" pour afficher les résultats de la fonction "Angenre"
resu3 = scrolledtext.ScrolledText(fenetre, width = 80, height = 12, bg='#7bef94', font=("Montserrat", 8, "italic bold"))
resu3.place(x=20, y = 300)
resu3.insert('1.0', "Résultats quand vous saisissez une année et un genre \n")


fenetre.mainloop()

