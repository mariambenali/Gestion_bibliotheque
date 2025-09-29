# users.py
from data import utilisateurs, aime_livres

# 1. Filtrer les utilisateurs majeurs
majeurs = list(filter(lambda u: u[3] >= 18, utilisateurs))  # u[3] = âge
print("Étape 1 - Utilisateurs majeurs :", majeurs)

# 2. Formater les noms complets en majuscules
noms_complets = list(map(lambda u: f"{u[1].upper()} {u[2].upper()}", majeurs))
print("Étape 2 - Noms complets en majuscules :", noms_complets)

# 3. Créer un dictionnaire associant chaque utilisateur à ses livres aimés
user_likes = {}
for u in majeurs:
    user_id = u[0]
    livres_aimes = [titre for uid, titre in aime_livres if uid == user_id]
    user_likes[user_id] = livres_aimes
print("Étape 3 - Dictionnaire utilisateur → livres aimés :", user_likes)

# 4. Générer un résumé par utilisateur
print("Étape 4 - Résumé par utilisateur :")
for u in majeurs:
    user_id, prenom, nom, age = u
    livres_str = ", ".join(f"'{titre}'" for titre in user_likes[user_id])
    print(f"{prenom.upper()} {nom.upper()} ({age} ans) aime : {livres_str}")