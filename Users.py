from data import utilisateurs

def filter_adults():
    """Retourner uniquement les utilisateurs de 18 ans ou plus"""
    return [u for u in utilisateurs if u[3] >= 18]

def modify_names():
    """Retourner la liste des prénoms en majuscules"""
    return [u[1].upper() for u in utilisateurs]

def afficher_utilisateurs():
    print("=== LISTE DES UTILISATEURS ===")
    for u in utilisateurs:
        print(f" - {u[1]} {u[2]}, {u[3]} ans")
