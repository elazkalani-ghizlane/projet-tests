# Fonction Ã  tester
def calculer_prix_total(nb_nuits, prix_par_nuit):
    """
    Calcule le prix total d'un sÃ©jour sur la plateforme Homey.
    - Si nb_nuits est nÃ©gatif, lÃ¨ve ValueError
    - Si prix_par_nuit est nÃ©gatif ou nul, lÃ¨ve ValueError
    
    Args:
        nb_nuits (int): Nombre de nuits du sÃ©jour
        prix_par_nuit (float): Prix par nuit de la propriÃ©tÃ©
    
    Returns:
        float: Prix total du sÃ©jour
    """
    if nb_nuits < 0:
        raise ValueError("Le nombre de nuits ne peut pas Ãªtre nÃ©gatif")
    
    if prix_par_nuit <= 0:
        raise ValueError("Le prix par nuit doit Ãªtre positif")
    
    return nb_nuits * prix_par_nuit 

import unittest
from exercice_homey_reservation_validation import calculer_prix_total

# Classe de tests unitaires (Ã  complÃ©ter)
class TestCalculPrix(unittest.TestCase):
    # TODO : Ajouter les tests unitaires ici
    # 1. Tester un calcul normal : 5 nuits Ã  80â‚¬ (assertEqual).
    # 2. Tester avec nombre de nuits nÃ©gatif (assertRaises ValueError).
    # 3. Tester avec prix par nuit nÃ©gatif (assertRaises ValueError).
    # 4. Tester avec prix par nuit zÃ©ro (assertRaises ValueError).
    
    pass

if __name__ == "__main__":
    unittest.main() 