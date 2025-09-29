from Users import filter_adults, modify_names, afficher_utilisateurs
from books import afficher_livres
from data import livres, aime_livres, utilisateurs

# --- FONCTIONS BONUS ---

def rechercher_utilisateur(nom):
    """Recherche par prénom ou nom"""
    for u in utilisateurs:
        if nom.lower() in (u[1] + " " + u[2]).lower():
            return f"Utilisateur trouvé : {u[1]} {u[2]} ({u[3]} ans)"
    return " Utilisateur introuvable."

def rechercher_livre(titre):
    """Recherche par titre"""
    for l in livres:
        if titre.lower() in l["titre"].lower():
            return f" Livre trouvé : {l['titre']} ({l['année']})"
    return " Livre introuvable."

def liste_utilisateurs_triee():
    """Créer une liste (Nom complet, âge) triée par âge"""
    noms = [f"{u[1]} {u[2]}" for u in utilisateurs]
    ages = [u[3] for u in utilisateurs]
    liste = list(zip(noms, ages))
    return sorted(liste, key=lambda x: x[1])  # tri par âge

# --- PROGRAMME PRINCIPAL ---
if __name__ == "__main__":
    print("=== RÉCAPITULATIF ===\n")
    afficher_utilisateurs()
    print()
    afficher_livres(livres)

    print("\n=== RECHERCHE ===")
    print(rechercher_utilisateur("Alice"))
    print(rechercher_livre("Harry"))

    print("\n=== UTILISATEURS TRIÉS PAR ÂGE ===")
    for nom, age in liste_utilisateurs_triee():
        print(f" - {nom}, {age} ans")