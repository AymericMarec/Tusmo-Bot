# Tusmo-Bot

## Explication

Cette api lancé localement , permet de renvoyer le meilleur mot a ecrire pour jouer au motus, celon les lettres du joueur.  

Exemple de requete vers l'api :

```json
{
    "new":false, //si le mot est nouveau ou pas ( 1er guess ou pas)
    "guess":"DELABR_S", // le mot avec les tiret du bas pour les cases vides
    "yellowLetters":[], // les lettres qui sont dans le mot mais mal placés , en jaune dans le jeu
    "usedLetters":["T","I","N","O","C"] // les lettres utilisées qui ne sont pas dans le mot
}
```

Réponse :

```json
{
    "word": "DELABRES"
}
```

## Lancement

Pour lancer l'api , 2 solutions :

### Docker

**Requis** :
-   Docker 

```
docker compose up
```

Tout simplement , pas plus compliqué que ca

### Sans Docker

**Requis** :
-   Python

installez flask pour lancer le projet :

```
pip install flask
```

et lancez le fichier API.py

```
python API.py
```

## Extension : 

Pour l'extension qui permet d'utiliser cette API , voir le repo suivant :

https://github.com/AymericMarec/Tusmo-Bot-Extension

ou ceci pour le clone directement

```
git clone https://github.com/AymericMarec/Tusmo-Bot-Extension
```