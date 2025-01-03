from generate.generate_actus import generer_actualites
from generate.generate_actus_home import generer_actualites_home
from generate.generate_membres import generer_membres


def generer_pages():
    generer_actualites()
    generer_actualites_home()
    generer_membres("membres-bureau-association.csv")


if __name__ == "__main__":
    try:
        generer_pages()
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
