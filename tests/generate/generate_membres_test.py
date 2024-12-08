import unittest
from src.scripts.generate.generate_membres import get_file_path, charger_membres

class TestGenerateMembres(unittest.TestCase):

    def test_get_file_path(self):
        # Teste si le chemin du fichier est correct
        self.assertEqual(get_file_path("membres-bureau-association.csv"), "./../../src/data/csv/membres-bureau-association.csv")

    def test_charger_membres_empty_file(self):
        # Teste le chargement d'un fichier CSV vide
        with open('./data/csv/empty.csv', 'w', encoding='utf-8') as f:
            pass  # Crée un fichier vide
        self.assertEqual(charger_membres('empty.csv'), [])

    def test_charger_membres_valid_file(self):
        # Teste le chargement d'un fichier CSV valide
        with open('./data/csv/valid.csv', 'w', encoding='utf-8') as f:
            f.write("prenom,nom,email,statut\n")
            f.write("Jean,Dupont,jean.dupont@example.com,membre\n")
        expected = [{"prenom": "Jean", "nom": "Dupont", "email": "jean.dupont@example.com", "statut": "membre"}]
        self.assertEqual(charger_membres('valid.csv'), expected)

    def test_charger_membres_incorrect_format(self):
        # Teste le chargement d'un fichier avec un format incorrect
        with open('./data/csv/invalid.csv', 'w', encoding='utf-8') as f:
            f.write("prenom,nom,email\n")
            f.write("Jean,Dupont,jean.dupont@example.com\n")
        with self.assertRaises(IndexError):
            charger_membres('invalid.csv')

    def test_get_file_path_invalid_name(self):
        # Teste le chemin du fichier avec un nom invalide
        self.assertEqual(get_file_path(""), ".csv")

if __name__ == '__main__':
    unittest.main()