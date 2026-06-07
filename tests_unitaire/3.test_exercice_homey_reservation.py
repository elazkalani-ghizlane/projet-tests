import unittest
from exercice_homey_reservation import propriete_disponible

class TestDisponibilitePropriete(unittest.TestCase):
    """
    Tests unitaires pour la fonction propriete_disponible avec assertTrue et assertFalse.
    
    Cette classe dÃ©montre l'utilisation des assertions assertTrue et assertFalse
    pour valider des fonctions qui retournent des valeurs boolÃ©ennes.
    """
    
    def test_sejour_long_disponible(self):
        """
        Teste qu'un sÃ©jour long est disponible.
        
        assertTrue est utilisÃ© car on s'attend Ã  True pour les sÃ©jours >= 7 nuits.
        """
        resultat = propriete_disponible(7)
        self.assertTrue(resultat, "Un sÃ©jour de 7 nuits devrait Ãªtre disponible")
        
        resultat = propriete_disponible(10)
        self.assertTrue(resultat, "Un sÃ©jour de 10 nuits devrait Ãªtre disponible")
    
    def test_sejour_court_non_disponible(self):
        """
        Teste qu'un sÃ©jour court n'est pas disponible.
        
        assertFalse est utilisÃ© car on s'attend Ã  False pour les sÃ©jours < 7 nuits.
        """
        resultat = propriete_disponible(3)
        self.assertFalse(resultat, "Un sÃ©jour de 3 nuits ne devrait pas Ãªtre disponible")
        
        resultat = propriete_disponible(6)
        self.assertFalse(resultat, "Un sÃ©jour de 6 nuits ne devrait pas Ãªtre disponible")


if __name__ == "__main__":
    unittest.main(verbosity=2) 