from generate_pages import generer_pages
from serveur_local import lancer_serveur_local

if __name__ == "__main__":
    try:
        generer_pages()
        lancer_serveur_local()
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

