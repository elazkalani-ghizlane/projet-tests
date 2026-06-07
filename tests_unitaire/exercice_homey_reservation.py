# Fonction Ã  tester
def propriete_disponible(nb_nuits):
    """
    VÃ©rifie si une propriÃ©tÃ© est disponible selon la durÃ©e du sÃ©jour.
    - SÃ©jours de 7 nuits ou plus : disponible (True)
    - SÃ©jours plus courts : non disponible (False)
    
    Args:
        nb_nuits (int): Nombre de nuits demandÃ©es
    
    Returns:
        bool: True si disponible, False sinon
    """
    if nb_nuits >= 7:
        return True
    else:
        return False 
    
import unittest
from exercice_homey_reservation import propriete_disponible

class TestDisponibilitePropriete(unittest.TestCase):
    # TODO : Ã‰crire une classe de tests unitaires avec unittest
    # 1. Tester un sÃ©jour de 7 nuits (assertTrue).
    # 2. Tester un sÃ©jour de 10 nuits (assertTrue).
    # 3. Tester un sÃ©jour de 3 nuits (assertFalse).
    # 4. Tester un sÃ©jour de 6 nuits (assertFalse).
    
    pass

if __name__ == "__main__":
    unittest.main()     