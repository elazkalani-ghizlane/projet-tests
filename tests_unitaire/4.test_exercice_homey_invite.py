import unittest
from exercice_homey_invite import obtenir_responsable_proprietaire

class TestResponsablePropriete(unittest.TestCase):
    """
    Tests unitaires pour la fonction obtenir_responsable_proprietaire avec assertIsNone et assertIsNotNone.
    
    Cette classe dÃ©montre l'utilisation des assertions pour tester :
    - assertIsNone : quand on s'attend Ã  recevoir None
    - assertIsNotNone : quand on s'attend Ã  recevoir un objet
    """
    
    def test_propriete_avec_responsable(self):
        """
        Teste qu'une propriÃ©tÃ© avec responsable retourne un objet.
        
        assertIsNotNone est utilisÃ© car on s'attend Ã  recevoir un dictionnaire
        avec les informations du responsable.
        """
        resultat = obtenir_responsable_proprietaire(1)
        self.assertIsNotNone(resultat, "PropriÃ©tÃ© ID 1 devrait avoir un responsable")
        
        resultat = obtenir_responsable_proprietaire(2)
        self.assertIsNotNone(resultat, "PropriÃ©tÃ© ID 2 devrait avoir un responsable")
    
    def test_propriete_sans_responsable(self):
        """
        Teste qu'une propriÃ©tÃ© sans responsable retourne None.
        
        assertIsNone est utilisÃ© car on s'attend Ã  None pour les propriÃ©tÃ©s
        sans responsable assignÃ©.
        """
        resultat = obtenir_responsable_proprietaire(3)
        self.assertIsNone(resultat, "PropriÃ©tÃ© ID 3 ne devrait pas avoir de responsable")
        
        resultat = obtenir_responsable_proprietaire(99)
        self.assertIsNone(resultat, "PropriÃ©tÃ© ID 99 ne devrait pas avoir de responsable")


if __name__ == "__main__":
    unittest.main(verbosity=2) 