import os
import markdown
from jinja2 import Environment, FileSystemLoader

def generer_actualites_home():
    try:
        # Configurer Jinja2
        env = Environment(loader=FileSystemLoader('../templates'))
        template = env.get_template('home.html')
    except Exception as e:
        print(f"Erreur lors de la configuration de Jinja2 : {e}")
        return

    actualites = []  # Liste pour stocker les actualités

    try:
        # Parcourir les fichiers .md dans data/md
        for filename in os.listdir('../data/md'):
            if filename.endswith('.md'):
                try:
                    with open(os.path.join('../data/md', filename), 'r') as f:
                        contenu_md = f.read()
                    
                    # Convertir Markdown en HTML
                    contenu_html = markdown.markdown(contenu_md)
                    
                    # Écrire le fichier HTML
                    nom_fichier_html = os.path.splitext(filename)[0] + '.html'
                    mots = os.path.splitext(filename)[0].split('-')
                    imageFichier = '-'.join(mots[-2:]) + '.webp' if len(mots) > 1 else os.path.splitext(filename)[0]
                    imageFichier = f'assets/img/{imageFichier}'  # Chemin d'accès à l'image

                    # Ajouter l'actualité à la liste
                    actualites.append({
                        'titre': os.path.splitext(filename)[0],  # Titre basé sur le nom du fichier
                        'extrait': contenu_html[:100] + '...',  # Extrait des premiers 100 caractères
                        'lien': f'actus/{nom_fichier_html}',  # Lien vers l'article complet
                        'imageFichier': imageFichier
                    })

                except IOError as e:
                    print(f"Erreur lors de la lecture/écriture du fichier {filename} : {e}")
                except Exception as e:
                    print(f"Erreur lors du traitement du fichier {filename} : {e}")
    except Exception as e:
        print(f"Erreur lors du parcours des fichiers : {e}")
    else:
        # Générer le HTML final avec le template
        output = template.render(actualites=actualites)
        with open('../../public/index.html', 'w') as f:
            f.write(output)

    print("Génération des actualités terminée.")

if __name__ == "__main__":
    try:
        generer_actualites()
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
