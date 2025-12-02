# Dictionnaire pour stocker la bibliothèque
bibliotheque = {}

def ajouter_livre():
    """Fonction pour ajouter un nouveau livre"""
    titre = input("Entrez le titre du livre : ")
    auteur = input("Entrez le nom de l'auteur : ")
    annee = int(input("Entrez l'année de publication : "))
    genre = input("Entrez le genre du livre : ")
    
    # Création d'un dictionnaire pour chaque livre
    livre = {
        "auteur": auteur,
        "annee": annee,
        "genre": genre,
        "lu": False
    }
    
    # Ajout du livre dans la bibliothèque
    bibliotheque[titre] = livre
    print(f"Le livre '{titre}' a été ajouté avec succès !")

def afficher_bibliotheque():
    """Fonction pour afficher tous les livres"""
    if not bibliotheque:
        print("Votre bibliothèque est vide.")
        return
    
    for titre, infos in bibliotheque.items():
        statut = "Lu" if infos["lu"] else "Non lu"
        print(f"Titre: {titre}")
        print(f"Auteur: {infos['auteur']}")
        print(f"Année: {infos['annee']}")
        print(f"Genre: {infos['genre']}")
        print(f"Statut: {statut}")
        print("-" * 30)

def marquer_comme_lu():
    """Fonction pour marquer un livre comme lu"""
    titre = input("Entrez le titre du livre à marquer : ")
    
    # Condition pour vérifier si le livre existe
    if titre in bibliotheque:
        bibliotheque[titre]["lu"] = True
        print(f"Le livre '{titre}' a été marqué comme lu.")
    else:
        print("Ce livre n'est pas dans votre bibliothèque.")

def rechercher_par_genre():
    """Fonction pour rechercher des livres par genre"""
    genre_recherche = input("Entrez le genre à rechercher : ")
    
    # Boucle pour trouver les livres correspondants
    livres_trouves = []
    for titre, infos in bibliotheque.items():
        if infos["genre"].lower() == genre_recherche.lower():
            livres_trouves.append(titre)
    
    # Condition pour afficher les résultats
    if livres_trouves:
        print(f"Livres du genre '{genre_recherche}' :")
        for livre in livres_trouves:
            print(livre)
    else:
        print(f"Aucun livre trouvé dans le genre '{genre_recherche}'.")

def menu_principal():
    """Menu principal avec boucle d'interaction"""
    while True:
        print("\n--- Gestionnaire de Bibliothèque ---")
        print("1. Ajouter un livre")
        print("2. Afficher la bibliothèque")
        print("3. Marquer un livre comme lu")
        print("4. Rechercher par genre")
        print("5. Quitter")
        
        choix = input("Entrez votre choix (1-5) : ")
        
        # Structure de conditions pour le menu
        if choix == '1':
            ajouter_livre()
        elif choix == '2':
            afficher_bibliotheque()
        elif choix == '3':
            marquer_comme_lu()
        elif choix == '4':
            rechercher_par_genre()
        elif choix == '5':
            print("Merci d'avoir utilisé le Gestionnaire de Bibliothèque !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Lancement du programme
menu_principal()

