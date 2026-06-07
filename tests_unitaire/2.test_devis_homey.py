import unittest
from devis_homey import devis_par_nuit

class TestDevisHomey(unittest.TestCase):

  def test_cas_Tousfalse(self):
     self.assertEqual(devis_par_nuit(100.0, week_end=False, long_sejour=False),100.0)

  def test_cas_True_False(self):
     self.assertEqual(devis_par_nuit(100.0 , week_end=True , long_sejour=False),115.0)


  def test_cas_False_True(self):
     self.assertEqual(devis_par_nuit(100.0 , week_end=False, long_sejour=True),90.0)

  def test_cas_simple(self):
     self.assertEqual(devis_par_nuit(100.0 , week_end=True , long_sejour=True),105.0)


if __name__ == "__main__":
    unittest.main()