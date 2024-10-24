# Atelier 1 - Site Flat-File

## Introduction
Ce projet, développé par **Samuel R.** et **Hugo TD.**, vise à créer un site web dynamique généré à partir de fichiers Markdown (MD), d'images associées et de données au format CSV, en utilisant un système de gestion de contenu flat-file (Flat File CMS). L'objectif est de démontrer nos compétences en développement web, en intégration continue et en gestion de contenu. Ce site servira de plateforme pour l'association de quartier fictive "Vivre aux lilas", permettant d'afficher des actualités, des informations sur les membres et d'autres contenus pertinents. Ce projet sera également l'occasion d'appliquer des pratiques de développement modernes et de collaborer efficacement en équipe. Un système de linter de code python pour analyser le code 

## Table des matières
- [Prérequis](#prérequis)
- [Installation des packages Python](#installation-des-packages-python)
  - [Sous Windows](#sous-windows)
  - [Sous Linux](#sous-linux)
- [Lancement de l'application](#lancement-de-lapplication)
  - [Sous Windows](#sous-windows-1)
  - [Sous Linux](#sous-linux-1)
- [Lancement du serveur](#lancement-du-serveur)
  - [Sous Windows](#sous-windows-2)
  - [Sous Linux](#sous-linux-2)
- [Génération des pages HTML](#génération-des-pages-html)
  - [Sous Windows](#sous-windows-3)
  - [Sous Linux](#sous-linux-3)
- [Étapes du projet](#étapes-du-projet)
  - [Étape 1 - Maquette](#étape-1---maquette)
  - [Étape 2 - Génération](#étape-2---génération)
  - [Étape 3 - Documentation du build](#étape-3---documentation-du-build)

## Prérequis
Voici les prérequis : 
- python 3.x

## Installation des packages Python
Dans cette section, vous trouverez les instructions pour installer les dépendances nécessaires au projet. Les instructions sont fournies pour les utilisateurs de Windows et de Linux.

### Sous Windows
```bash
# Installation des modules Python
cd atelier1/
python -m venv env
env/Scripts/activate
pip install -r requirements.txt
```

### Sous Linux
```bash
# Installation des modules Python
cd atelier1/
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Lancement de l'application
Cette section explique comment démarrer l'application principale. Les instructions sont fournies pour les deux systèmes d'exploitation.

### Sous Windows
```bash
cd src/scripts/
python main.py
```

### Sous Linux
```bash
cd src/scripts/
python3 main.py
```

## Lancement du serveur
Ici, vous apprendrez comment démarrer le serveur local pour tester votre application. Les commandes sont spécifiques à chaque système d'exploitation.

### Sous Windows
```bash
python serveur_local.py
```

### Sous Linux
```bash
python3 serveur_local.py
```

## Génération des pages HTML
Cette section fournit les commandes nécessaires pour générer les pages HTML à partir des fichiers Markdown et CSV. Les instructions sont également séparées par système d'exploitation.

### Sous Windows
```bash
python generate_pages.py
```

### Sous Linux
```bash
python3 generate_pages.py
```

## Fonctionnement du linter flake8
Flake8 est un module python permettant de vérifier la qualité du code python de notre projet et de le corriger en conséquence.

### Sous Windows et Linux
```bash
flake8 ./<nom-du-fichier-ou-du-dossier>
```

# Étapes du projet
Dans cette section, vous trouverez un aperçu des différentes étapes à suivre pour réaliser le projet, y compris la création de maquettes, la génération de contenu et la documentation.

### Étape 1 - Maquette
Proposer une maquette pour l'association de quartier factice "Vivre aux lilas" contenant :
- Une page d'accueil capable d'afficher les actualités de l'association.
- Une page détail d'actualité.
- Une page membres du bureau.

**Note :** Les données de l'archive fournie devront pouvoir être affichées sur le site, mais la maquette ne reprend pas forcément leur contenu. Le site utilise SCSS pour ses feuilles de style ou un framework CSS personnalisable avec SCSS (et personnalisé selon vos codes couleur).

### Étape 2 - Génération
En privilégiant la convention plutôt que la configuration, écrire un ou plusieurs programmes ou scripts dans le langage de votre choix qui génère(nt) côté serveur les pages du site d'après les fichiers md et csv fournis en ligne de commande.

Ainsi, lors de sa consultation, aucun code serveur ne s'exécutera (pré). Du JavaScript élémentaire peut être envisagé côté client pour proposer des filtres, par exemple.

**Notes :**
- On suppose les fichiers déjà décompressés.
- Vous pouvez appuyer toute ou partie de votre génération sur l'appel à des applications tierces (Ex : pandoc pour convertir le markdown en html).
- Votre ou vos applications recevant les noms de fichiers à traiter en argument, vous n'avez pas d'exploration de répertoire à coder.

### Étape 3 - Documentation du build
Rédiger le README.md du projet en anglais ou français indiquant :
- Les prérequis systèmes pour un build et une génération du site.
- Leur installation sur un Linux (au choix).
- Les commandes du build de votre ou vos programmes.
- Les commandes et éventuelles options d'appel.
- Les membres du groupe Prénom + initiale du nom.
