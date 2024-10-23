# Atelier 1 - Site Flat-File
Seul-e ou en binôme, vous proposez un site généré à partir de fichiers (aka Flat File CMS) en .md, d'images
associées et de données en .csv qui fera l'objet d'intégration continue sur les ateliers suivants.

## Etape 1 - Maquette
Proposer une maquette pour l'association de quartier factice "Vivre aux lilas" contenant :
- une page d'accueil capable d'afficher les actualités de l'association,
- une page détail d'actualité,
- une page membres du bureau

Note : Les données de l'archive fournie devront pouvoir être affichées sur le site, mais la maquette ne reprend
pas forcément leur contenu.

Le site utilise SCSS pour ses feuilles de style ou un framework CSS personnalisable avec SCSS (et personnalisé
selon vos codes couleur).

## Etape 2 - Génération
En privilégiant la convention plutôt que la configuration, écrire un ou plusieurs programmes ou scripts dans le
langage de votre choix qui génère(nt) côté serveur les pages du site d'après les fichiers md et csv fournis en
ligne de commande.

Ainsi, lors de sa consultation, aucun code serveur ne s'exécutera (pré). Du javascript élémentaire peut être
envisagé côté client pour proposer des filtres, par exemple.

Notes :
- On suppose les fichiers déjà décompressés,
- Vous pouvez appuyer toute ou partie de votre génération sur l'appel à des applications tierces (Ex :
pandoc pour convertir le markdown en html),
- Votre ou vos applications recevant les noms de fichiers à traiter en argument, vous n'avez pas
d'exploration de répertoire à coder.

## Etape 3 - Documentation du build
Rédiger le readme.md du projet en anglais ou français indiquant :
- les prérequis systèmes pour un build et une génération du site,
- leur installation sur un linux (au choix),
- les commandes du build de votre ou vos programmes,
- les commandes et éventuelles options d'appel
- les membres du groupe Prénom + initiale du nom


## Requirements

## Installation des packages python

### Sous Linux
```bash
python venv -m env
env/Scripts/activate
pip install -r requirements.txt
```

### Sous Windows
```bash
python venv -m env
env/Scripts/activate
pip install -r requirements.txt
```
