# Contexte : Homey calcule un prix par nuit pour une rÃ©servation.
# RÃ¨gles simplifiÃ©es :
# - week_end : +15 % (vendredi/samedi/dimanche)
# - long_sejour : -10 % (sÃ©jour >= 7 nuits)
# NB : pas de "else" -> chaque if a 2 issues (Vrai/Faux)

def devis_par_nuit(tarif_base: float, week_end: bool, long_sejour: bool) -> float:
    total = tarif_base
    if week_end:        # DÃ©cision 1 (Vrai / Faux)
        total += tarif_base * 0.15
    if long_sejour:     # DÃ©cision 2 (Vrai / Faux)
        total -= tarif_base * 0.10
    # Arrondi commercial faÃ§on Homey (2 dÃ©cimales)
    return round(total, 2)

