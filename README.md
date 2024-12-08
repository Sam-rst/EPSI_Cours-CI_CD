# Atelier 1 - Vivre aux lilas

## Introduction
Ce projet, conçu par **Samuel R.** et **Hugo TD.**, a pour objectif de développer un site web dynamique généré à partir de fichiers Markdown (MD), d’images et de données au format CSV, utilisant un système de gestion de contenu flat-file (Flat File CMS). Ce site web est destiné à l'association de quartier fictive "Vivre aux Lilas" et présente des actualités, des informations sur les membres, ainsi que d'autres contenus pertinents. Le projet permet d’explorer des pratiques modernes en développement web, gestion de contenu, intégration continue, et collaboration d’équipe.

## MEP du projet
Voici le lien de l'application mise en production durant ce cours : [Vivre aux lilas](https://sam-rst.github.io/EPSI_Cours-CI_CD/)

## Prérequis
Avant de commencer, assurez-vous que votre environnement répond aux exigences suivantes :
- **Python 3.x**

## Maquettage
Les maquettes du site ont été créées avec **Figma** pour visualiser les pages générées via le code HTML produit par nos scripts Python :

- [Maquette fonctionnelle](https://www.figma.com/proto/A7XB9N5xIFljSMUCcSJmdS/Vivre-aux-lilas?node-id=0-1&t=ffc2pUzq8Q6EPEvB-1)
- [Maquette technique](https://www.figma.com/design/A7XB9N5xIFljSMUCcSJmdS/Vivre-aux-lilas?node-id=0-1&m=dev&t=ffc2pUzq8Q6EPEvB-1)

## Installation des dépendances
Installez les modules Python nécessaires à l’aide du fichier `requirements.txt`. Suivez les instructions ci-dessous selon votre système d’exploitation. Assurez-vous de bien être dans le dossier `atelier1/`.

### Sous Windows
```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

### Sous Linux
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Démarrage de l'application
Pour exécuter l'application principale, utilisez la commande appropriée à votre système d'exploitation.

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

## Lancement des scripts spécifiques
Si vous souhaitez lancer indépendemment les 2 scripts : 
- `serveur_local.py` : lance le serveur en localhost
- `generate_pages.py` : génère les différentes pages html venant des fichiers md pour les actualités, du fichier csv pour les membres et des autres templates de `src/templates`

### Serveur local
```bash
# Windows
python serveur_local.py

# Linux
python3 serveur_local.py
```

### Génération des pages HTML
```bash
# Windows
python generate_pages.py

# Linux
python3 generate_pages.py
```

## Linter du code avec Flake8
**Flake8** est utilisé pour assurer la qualité du code Python. Exécutez Flake8 comme suit :

```bash
flake8 ./<nom-du-fichier-ou-du-dossier>
```

## Étapes du projet
Voici les différentes étapes suivies dans ce projet :

### Étape 1 - Création de la maquette
Proposition de maquettes pour le site "Vivre aux Lilas" contenant :
- Une page d'accueil pour les actualités de l'association.
- Une page détaillant chaque actualité.
- Une page pour les membres du bureau.

**Remarque** : Les données fournies devront pouvoir être affichées sur le site. Le style utilise SCSS ou un framework CSS personnalisable avec SCSS adapté aux couleurs choisies.

### Étape 2 - Génération des pages
En suivant les conventions, des scripts Python génèrent les pages HTML depuis les fichiers MD et CSV. Le rendu final ne nécessite pas d'exécution de code côté serveur, sauf JavaScript pour des filtres côté client.

**Notes** :
- Les fichiers à traiter sont fournis décompressés.
- Utilisation possible d’outils externes comme *pandoc* pour la conversion Markdown en HTML.
- Les noms de fichiers sont passés en arguments, donc pas besoin de parcourir les répertoires.

### Étape 3 - Documentation du build
Ce fichier README fournit toutes les informations nécessaires :
- Prérequis système pour le build et la génération.
- Instructions d'installation sur Linux.
- Commandes pour générer le site et options disponibles.
- Membres de l'équipe : Samuel R., Hugo TD.

---

Cela offre une structure claire et une présentation professionnelle de votre projet !