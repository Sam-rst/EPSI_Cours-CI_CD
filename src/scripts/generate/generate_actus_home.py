import os
import markdown
from jinja2 import Environment, FileSystemLoader


def lire_fichier_md(filename):
    """Lire le contenu d'un fichier Markdown et le convertir en HTML."""
    with open(os.path.join('../data/md', filename), 'r', encoding='utf-8') as f:
        contenu_md = f.read()
    return markdown.markdown(contenu_md)


def construire_actualite(filename, contenu_html):
    """Construire un dictionnaire d'actualité à partir du nom de fichier et du contenu HTML."""
    nom_fichier_html = os.path.splitext(filename)[0] + '.html'
    mots = os.path.splitext(filename)[0].split('-')
    if len(mots) > 1:
        imageFichier = '-'.join(mots[-2:]) + '.webp'
    else:
        imageFichier = os.path.splitext(filename)[0] + '.webp'

    imageFichier = f'assets/img/{imageFichier}'

    return {
        'titre': os.path.splitext(filename)[0],
        'extrait': contenu_html[:100] + '...',
        'lien': f'actus/{nom_fichier_html}',
        'imageFichier': imageFichier
    }


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
                    contenu_html = lire_fichier_md(filename)
                    actualites.append(construire_actualite(filename, contenu_html))
                except IOError as e:
                    print(f"Erreur lors de la lecture/écriture du fichier {filename} : {e}")
                except Exception as e:
                    print(f"Erreur lors du traitement du fichier {filename} : {e}")
    except Exception as e:
        print(f"Erreur lors du parcours des fichiers : {e}")
    else:
        # Générer le HTML final avec le template
        output = template.render(actualites=actualites, file_depth="")
        with open('../../public/index.html', 'w', encoding='utf-8') as f:
            f.write(output)

    print("Génération des actualités terminée.")


if __name__ == "__main__":
    try:
        generer_actualites_home()
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
