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
    

# Fonctions Ã  tester
def calculer_prix_base(nb_nuits, prix_par_nuit):
    """Calcule le prix de base d'un sÃ©jour."""
    return nb_nuits * prix_par_nuit


def appliquer_reduction(prix_base, nb_nuits):
    """
    Applique une rÃ©duction pour les sÃ©jours longs :
    - 7 nuits ou plus : 10% de rÃ©duction
    - Sinon : pas de rÃ©duction
    """
    if nb_nuits >= 7:
        return prix_base * 0.9  # 10% de rÃ©duction
    else:
        return prix_base
   