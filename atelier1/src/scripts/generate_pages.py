from generate.generate_actus import generer_actualites
from generate.generate_actus_home import generer_actualites_home

if __name__ == "__main__":
    try:
        generer_actualites()
        generer_actualites_home()
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
