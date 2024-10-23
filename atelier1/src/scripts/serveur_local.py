import os
import http.server
import socketserver
import time

def lancer_serveur_local(port=8000, max_tentatives=5):
    tentatives = 0
    while tentatives < max_tentatives:
        try:
            handler = http.server.SimpleHTTPRequestHandler

            try:
                os.chdir("../../public")
            except OSError as e:
                print(f"Erreur lors du changement de répertoire : {e}")
                return

            try:
                with socketserver.TCPServer(("", port), handler) as httpd:
                    print(f"Serveur lancé sur le port {port}")
                    print(f"Ouvrez votre navigateur et allez à http://localhost:{port}")
                    httpd.serve_forever()
            except PermissionError:
                print(f"Erreur : Permission refusée pour le port {port}. Essayez un port supérieur à 1024 ou exécutez le script avec des privilèges administrateur.")
                return
            except OSError as e:
                if e.errno == 98:
                    print(f"Erreur : Le port {port} est déjà utilisé. Tentative de redémarrage dans 5 secondes...")
                    time.sleep(5)
                    tentatives += 1
                else:
                    print(f"Erreur lors du lancement du serveur : {e}")
                    return
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")
            return

    print(f"Impossible de lancer le serveur après {max_tentatives} tentatives.")

if __name__ == "__main__":
    try:
        lancer_serveur_local()
    except KeyboardInterrupt:
        print("\nServeur arrêté par l'utilisateur.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite lors du lancement du serveur : {e}")
