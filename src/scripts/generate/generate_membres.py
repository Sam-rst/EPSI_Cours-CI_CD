import csv
from jinja2 import Environment, FileSystemLoader

def get_file_path(csv_file_name) -> str:
    return f"./../data/csv/{csv_file_name}"

def charger_membres(file_path: str) -> list:
    membres = []
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
    return membres

def generer_membres(csv_file_name: str):
    try:
        # Configurer Jinja2
        env = Environment(loader=FileSystemLoader('./../templates'))
        template = env.get_template('membres.html')
    except Exception as e:
        print(f"Erreur lors de la configuration de Jinja2 : {e}")
        return

    membres = charger_membres(get_file_path(csv_file_name))
    output = template.render(membres=membres, file_depth="")
    with open('./../../public/membres.html', 'w', encoding='utf-8') as f:
        f.write(output)

    print("Génération des membres terminée.")


if __name__ == "__main__":
    try:
        generer_membres("membres-bureau-association.csv")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
