import csv
from jinja2 import Environment, FileSystemLoader


def generer_membres():
    try:
        # Configurer Jinja2
        env = Environment(loader=FileSystemLoader('../templates'))
        template = env.get_template('membres.html')
    except Exception as e:
        print(f"Erreur lors de la configuration de Jinja2 : {e}")
        return

    membres = []
    file_path = '../data/csv/membres-bureau-association.csv'
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row

        for row in csv_reader:
            membres.append({
                "prenom": row[0],
                "nom": row[1],
                "email": row[2],
                "statut": row[3],
            })
        output = template.render(membres=membres)
        with open('../../public/membres.html', 'w') as f:
            f.write(output)

        print("Génération des membres terminée.")


if __name__ == "__main__":
    try:
        generer_membres()
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
