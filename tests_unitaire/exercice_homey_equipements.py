# Fonction Ã  tester
def obtenir_equipements_propriete(standing):
    """
    Retourne les Ã©quipements selon le standing de la propriÃ©tÃ© Homey.
    - Standard : ["WiFi", "Parking"]
    - Premium : ["WiFi", "Parking", "Piscine"]
    
    Args:
        standing (str): Standing de la propriÃ©tÃ© ("Standard" ou "Premium")
    
    Returns:
        list: Liste des Ã©quipements disponibles
    """
    equipements = ["WiFi", "Parking"]
    
    if standing == "Premium":
        equipements.append("Piscine")
    
    return equipements 

import unittest
from exercice_homey_equipements import obtenir_equipements_propriete

class TestEquipementsPropriete(unittest.TestCase):
    # TODO : Ã‰crire une classe de tests unitaires avec unittest
    # 1. Tester qu'une propriÃ©tÃ© Standard contient "WiFi" (assertIn).
    # 2. Tester qu'une propriÃ©tÃ© Standard ne contient pas "Piscine" (assertNotIn).
    # 3. Tester qu'une propriÃ©tÃ© Premium contient "Piscine" (assertIn).
    # 4. Tester qu'une propriÃ©tÃ© Premium contient "WiFi" (assertIn).
    
    pass

if __name__ == "__main__":
    unittest.main() 