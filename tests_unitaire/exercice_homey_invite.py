# Fonction Ã  tester
def obtenir_responsable_proprietaire(id_propriete):
    """
    Retourne le responsable d'une propriÃ©tÃ© selon son ID.
    - ID 1 ou 2 : retourne un responsable (dict)
    - Autres ID : pas de responsable assignÃ© (None)
    
    Args:
        id_propriete (int): Identifiant de la propriÃ©tÃ©
    
    Returns:
        dict ou None: Informations du responsable ou None
    """
    if id_propriete in [1, 2]:
        return {"nom": "Jean Dupont", "telephone": "0123456789"}
    else:
        return None 
    
import unittest
from exercice_homey_invite import obtenir_responsable_proprietaire

# Classe de tests unitaires (Ã  complÃ©ter)
class TestResponsablePropriete(unittest.TestCase):
    # TODO : Ajouter les tests unitaires ici
    # 1. Tester propriÃ©tÃ© ID 1 (assertIsNotNone).
    # 2. Tester propriÃ©tÃ© ID 3 (assertIsNone).
    # 3. Tester propriÃ©tÃ© ID 2 (assertIsNotNone).
    
    pass

if __name__ == "__main__":
    unittest.main()     