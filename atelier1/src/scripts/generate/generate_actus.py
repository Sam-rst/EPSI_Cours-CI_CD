import os
import markdown
from jinja2 import Environment, FileSystemLoader

def generer_actualites():
    try:
        # Configurer Jinja2
        env = Environment(loader=FileSystemLoader('../templates'))
        template = env.get_template('actualite.html')
    except Exception as e:
        print(f"Erreur lors de la configuration de Jinja2 : {e}")
        return

    try:
        # Génération du dossier actus si il n'existe pas déjà
        os.makedirs('../../public/actus', exist_ok=True)
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

                    actualite = {
                        'titre': os.path.splitext(filename)[0],  # Titre basé sur le nom du fichier
                        'imageFichier': imageFichier,
                        'contenu': contenu_html
                    }
                    # Générer le HTML final avec le template
                    output = template.render(actualite=actualite)
                    with open(f"../../public/actus/{nom_fichier_html}", 'w') as file:
                        file.write(output)

                    print(f"Génération de la page {nom_fichier_html} réussie")

                except IOError as e:
                    print(f"Erreur lors de la lecture/écriture du fichier {filename} : {e}")
                except Exception as e:
                    print(f"Erreur lors du traitement du fichier {filename} : {e}")
    except Exception as e:
        print(f"Erreur lors du parcours des fichiers : {e}")

if __name__ == "__main__":
    try:
        generer_actualites()
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
