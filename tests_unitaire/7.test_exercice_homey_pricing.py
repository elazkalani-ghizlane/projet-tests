import unittest
from exercice_homey_pricing import calculer_prix_base , appliquer_reduction

class TestPrixSejour(unittest.TestCase):
  

    def setUp(self):
        # Variables communes utilisÃ©es dans plusieurs tests
        self.prix_nuit = 100.0
        self.nb_nuits_court = 3    # Pas de rÃ©duction
        self.nb_nuits_long = 7     # Avec rÃ©duction

    def test_calcul_prix_base(self):
        prix = calculer_prix_base(self.nb_nuits_court, self.prix_nuit)
        self.assertEqual(prix, 300.0, "3 nuits Ã  100â‚¬ = 300â‚¬")

    def test_pas_de_reduction_sejour_court(self):
        
        prix_base = calculer_prix_base(self.nb_nuits_court, self.prix_nuit)
        prix_final = appliquer_reduction(prix_base, self.nb_nuits_court)
        self.assertEqual(prix_final, prix_base, "Pas de rÃ©duction pour sÃ©jour court")

    def test_reduction_sejour_long(self):
        
        prix_base = calculer_prix_base(self.nb_nuits_long, self.prix_nuit)
        prix_final = appliquer_reduction(prix_base, self.nb_nuits_long)
        prix_attendu = prix_base * 0.9  # 10% de rÃ©duction
        self.assertEqual(prix_final, prix_attendu, "10% de rÃ©duction pour 7+ nuits")


if __name__ == "__main__":
    unittest.main(verbosity=2) 
    