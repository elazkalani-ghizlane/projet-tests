import unittest
from exercice_homey_equipements import obtenir_equipements_propriete

class TestEquipementsPropriete(unittest.TestCase):
    """
    Tests unitaires pour la fonction obtenir_equipements_propriete avec assertIn et assertNotIn.
    
    Cette classe dÃ©montre l'utilisation des assertions pour tester la prÃ©sence
    ou l'absence d'Ã©lÃ©ments dans des collections.
    """
    
    def test_equipements_standard(self):
        """
        Teste qu'une propriÃ©tÃ© Standard contient les Ã©quipements de base.
        
        assertIn vÃ©rifie que les Ã©quipements sont prÃ©sents dans la liste.
        """
        equipements = obtenir_equipements_propriete("Standard")
        
        self.assertIn("WiFi", equipements, "WiFi devrait Ãªtre disponible en Standard")
        self.assertIn("Parking", equipements, "Parking devrait Ãªtre disponible en Standard")
        self.assertNotIn("Piscine", equipements, "Piscine ne devrait pas Ãªtre disponible en Standard")
    
    def test_equipements_premium(self):
        """
        Teste qu'une propriÃ©tÃ© Premium contient tous les Ã©quipements.
        
        assertIn vÃ©rifie que les Ã©quipements de base + premium sont prÃ©sents.
        """
        equipements = obtenir_equipements_propriete("Premium")
        
        self.assertIn("WiFi", equipements, "WiFi devrait Ãªtre disponible en Premium")
        self.assertIn("Parking", equipements, "Parking devrait Ãªtre disponible en Premium")
        self.assertIn("Piscine", equipements, "Piscine devrait Ãªtre disponible en Premium")


if __name__ == "__main__":
    unittest.main(verbosity=2) 