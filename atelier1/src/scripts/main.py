import os
import markdown
from jinja2 import Environment, FileSystemLoader

def generer_actualites():
    # Configurer Jinja2
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('actualite.html')

    # Parcourir les fichiers .md dans data/md
    for filename in os.listdir('data/md'):
        if filename.endswith('.md'):
            with open(os.path.join('data/md', filename), 'r') as f:
                contenu_md = f.read()
            
            # Convertir Markdown en HTML
            contenu_html = markdown.markdown(contenu_md)
            
            # Générer le HTML final avec le template
            output = template.render(contenu=contenu_html)
            
            # Écrire le fichier HTML
            nom_fichier_html = os.path.splitext(filename)[0] + '.html'
            with open(os.path.join('output', nom_fichier_html), 'w') as f:
                f.write(output)

    print("Génération des actualités terminée.")

if __name__ == "__main__":
    generer_actualites()