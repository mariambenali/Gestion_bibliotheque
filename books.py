from data import livres, aime_livres, utilisateurs


# 1. Trier les livres
livres_tries = sorted(livres, key=lambda x: x["année"])
print("Livres triés :", [l["titre"] for l in livres_tries])

# 2. Plus ancien / Plus récent
print("Plus ancien :", livres_tries[0]["titre"])
print("Plus récent :", livres_tries[-1]["titre"])

# 3. Dictionnaire des préférences
compte = {}
for _, titre in aime_livres:
    compte[titre] = compte.get(titre, 0) + 1
print("Compteur :", compte)

# 4. Pagination utilisateurs (2 par 2)
i = 0
while i < len(utilisateurs):
    print(utilisateurs[i:i+2])
    i += 2


    # afficher_livres
    def afficher_livres(livres):
     for livre in livres:
        print(f"{livre['titre']} - {livre['auteur']} ({livre['année']})")
