import unittest

def calculer_prix_nuit(prix_base, nb_nuits, frais_menage=50):
    """
    Calcule le prix total d'un sÃ©jour sur la plateforme Homey :
    - Un prix de base par nuit
    - Le nombre de nuits
    - Des frais de mÃ©nage (par dÃ©faut 50â‚¬)
    """
    return (prix_base * nb_nuits) + frais_menage    


class TestCalculPrixNuit(unittest.TestCase):
    """
    Tests unitaires pour la fonction calculer_prix_nuit.
    
    Cette classe dÃ©montre les concepts de base des tests unitaires :
    - Structure d'une classe de test avec unittest
    - MÃ©thodes de test commenÃ§ant par "test_"
    - Utilisation de assertEqual pour vÃ©rifier les rÃ©sultats
    - Test de diffÃ©rents scÃ©narios (cas normaux, valeurs par dÃ©faut, paramÃ¨tres personnalisÃ©s)
    """
    
    def test_prix_base_sans_frais_supplementaires(self):
        """
        Teste le calcul du prix avec les frais de mÃ©nage par dÃ©faut.
        
        Ce test vÃ©rifie que la fonction fonctionne correctement avec
        les paramÃ¨tres de base et la valeur par dÃ©faut pour frais_menage.
        """
        # Calcul : 100â‚¬/nuit Ã— 3 nuits + 50â‚¬ frais mÃ©nage = 350â‚¬
        resultat = calculer_prix_nuit(100, 3)
        self.assertEqual(resultat, 350, "3 nuits Ã  100â‚¬ + 50â‚¬ frais mÃ©nage = 350â‚¬")
    
    def test_prix_base_avec_frais_personnalises(self):
        """
        Teste le calcul du prix avec des frais de mÃ©nage personnalisÃ©s.
        
        Ce test vÃ©rifie que la fonction accepte un paramÃ¨tre personnalisÃ©
        pour les frais de mÃ©nage et l'utilise correctement dans le calcul.
        """
        # Calcul : 80â‚¬/nuit Ã— 2 nuits + 30â‚¬ frais mÃ©nage = 190â‚¬
        resultat = calculer_prix_nuit(80, 2, frais_menage=30)
        self.assertEqual(resultat, 190, "2 nuits Ã  80â‚¬ + 30â‚¬ frais mÃ©nage = 190â‚¬")
    
    def test_sejour_plusieurs_nuits(self):
        """
        Teste le calcul pour un sÃ©jour de plusieurs nuits.
        
        Ce test vÃ©rifie que la multiplication des nuits fonctionne
        correctement pour des sÃ©jours plus longs.
        """
        # Calcul : 120â‚¬/nuit Ã— 5 nuits + 50â‚¬ frais mÃ©nage = 650â‚¬
        resultat = calculer_prix_nuit(120, 5)
        self.assertEqual(resultat, 650, "5 nuits Ã  120â‚¬ + 50â‚¬ frais mÃ©nage = 650â‚¬")
    
    def test_sejour_une_nuit(self):
        """
        Teste le calcul pour un sÃ©jour d'une seule nuit.
        
        Ce test vÃ©rifie le cas limite d'un sÃ©jour minimal.
        """
        # Calcul : 90â‚¬/nuit Ã— 1 nuit + 50â‚¬ frais mÃ©nage = 140â‚¬
        resultat = calculer_prix_nuit(90, 1)
        self.assertEqual(resultat, 140, "1 nuit Ã  90â‚¬ + 50â‚¬ frais mÃ©nage = 140â‚¬")


if __name__ == "__main__":
    # ExÃ©cution des tests avec verbositÃ© pour voir tous les dÃ©tails
    unittest.main(verbosity=2) 