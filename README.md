**ANALYSE DE DONNÉES SPOTIFY**

Pour ce projet final, le sujet qui nous a le plus inspiré est celui portant sur Spotify. Nous avons utilisé les données provenant de Kaggle que nous analyserons en détail dans la première partie. En ce qui concerne les données Top200, nous n’aurons besoin que du fichier spotify_top200_global et non ceux des pays séparément.
Notre projet se décompose en un dossier pour chacune des trois parties à traiter dans le cadre de ce projet, un dossier contenant les données et le rapport que vous êtes en train de lire 🙂. 

Source 1 : https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks

Source 2 : Top 200 most streamed songs on spotify 2020 (kaggle.com)

![unnamed](https://github.com/Thaonheyy/Spotify-Data-Analysis/assets/139818124/1cb5960a-a0f8-4ff8-8f9d-89a2ab20b2fc)

**PARTIE 1: ANALYSE DESCRIPTIVE DES BASES ET VISUALISATION** : Au sein du dossier 1 vous trouverez un notebook contenant le code que nous avons réalisé pour la partie 1 du projet.

**PARTIE 2 : RECHERCHE DE CONTENU** : Au sein du dossier 2, vous trouverez un fichier (.py) contenant le code que nous avons réalisé pour la partie 2 du projet.

La première fonction Artiste_info() demande à l’utilisateur de saisir un nom d’artiste et retourne son nombre d’abonnés, les trois chansons les plus populaires, les trois chansons les plus récentes et le nombre de chansons qu’il a dans le top 200 global de 2020. Le résultat devait retourner toutes les chansons qui y correspondent, et n’afficher que les 20 premières s’il y en avait plus que cela. 

La deuxième fonction song() est pour rechercher un titre de chanson.

La troisième fonction Angenre() renverra toutes les chansons qui correspondent à deux critères simultanément : l’année de sortie et le genre de musique. Le résultat devra afficher les chansons ordonnées par popularité d’artiste décroissante, puis s’il y a plusieurs chansons pour un même artiste, elles devront également être ordonnées par ordre de leur popularité décroissante. 

**PARTIE 3 : INTERFACE GRAPHIQUE** : Le dossier 3 se décompose en 3 fichiers PY (“Main”, “Fonctions” et “traitement_data”) et un sous-dossier contenant deux images. Le script “Main” est le code permettant de faire fonctionner l’interface. Ce script fait appel aux images présentes dans le sous-dossier “Images” et aux fonctions du module “Fonctions”. Le module “Fonctions” appelle lui-même des objets du script “traitement_data”. Ce dernier importe les données présentes dans le dossier  “Data” avant d’en faire un traitement préliminaire. 

![unnamed (1)](https://github.com/Thaonheyy/Spotify-Data-Analysis/assets/139818124/6b930dac-e148-4e92-be1c-bb5f170f665a)

 Cette interface comporte les éléments suivants:
- Possibilité pour l’utilisateur de saisir les différents critères (selon ce qui sera fait à la partie 2)
- Affichage des résultats selon ce qui a été demandé dans la partie 2
- Insertion des liens vers les pages Wikipedia et Spotify des artistes ainsi que le main page de Spotify

