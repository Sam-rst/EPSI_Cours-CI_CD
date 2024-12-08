import os
import markdown
from jinja2 import Environment, FileSystemLoader


def lire_fichier_md(chemin):
    with open(chemin, 'r', encoding='utf-8') as f:
        return f.read()


def generer_html(nom_fichier, contenu_md, template):
    contenu_html = markdown.markdown(contenu_md)
    mots = os.path.splitext(nom_fichier)[0].split('-')
    if len(mots) > 1:
        imageFichier = '-'.join(mots[-2:]) + '.webp'
    else:
        imageFichier = os.path.splitext(nom_fichier)[0]

    actualite = {
        'titre': os.path.splitext(nom_fichier)[0],
        'imageFichier': imageFichier,
        'contenu': contenu_html
    }
    return template.render(actualite=actualite, file_depth="../")


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
                    contenu_md = lire_fichier_md(os.path.join('../data/md', filename))
                    output = generer_html(filename, contenu_md, template)

                    nom_fichier_html = os.path.splitext(filename)[0] + '.html'
                    file_path = f"../../public/actus/{nom_fichier_html}"
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(output)

                    print(f"Génération de la page {nom_fichier_html} réussie")

                except IOError as e:
                    print(f"Erreur lors de la lecture/écriture du \
                        fichier {filename} : {e}")
                except Exception as e:
                    print(f"Erreur lors du traitement du fichier \
                        {filename} : {e}")
    except Exception as e:
        print(f"Erreur lors du parcours des fichiers : {e}")


if __name__ == "__main__":
    try:
        generer_actualites()
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
