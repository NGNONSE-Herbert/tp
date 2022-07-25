
import creer_bus
import creer_passager
import gerer_passager_bus

def menu():
    print("Bienvenue sur la Platforme \n" )
    print("1 : créer un bus ")
    print("2 : créer un passager ")
    print("3 : ajouter un passager à un bus ")
    print("4 : connaitre le nombre place disponible dans un bus ")
    print("5 : connaitre le nombre de kg reservé pour un bus ")
    print("6 : retirer un passager d'un bus ")
    print("7 : savoir si un bus peut accueillir les passagers provenant d'un autre bus ")
    print("8 : afficher la liste des passagers d'un bus ")
    print("9 : afficher l'ensemble des passagers de ma flotte de bus ")
    print("10 : savoir si un passager est enregistré sur un bus de ma flotte ")
    print("11 : supprimer un bus ")
    print("12 : supprimer un passager ")
    print("q : quitter \n")
    

    
liste_bus =[]
liste_passager = []
valeur=""
while valeur.lower() != "q":
    print("")
    menu()
    valeur = input("Entrez votre choix : ")
    print("")
    if valeur == "1":
        bus = creer_bus.creer_bus()
        liste_bus.append(bus)
            
    elif valeur == "2":
        passager = creer_passager.creer_Passager()
        liste_passager.append(passager)
    elif valeur == "3":
        liste_bus= gerer_passager_bus.ajouter_Passager_Au_bus(liste_bus, liste_passager)
    elif valeur == "4":
        place = creer_bus.nombre_de_place(liste_bus)
    elif valeur == "5":
        poids = creer_bus.nombre_kg_bus()
    elif valeur == "6":
        liste_bus = gerer_passager_bus.delete_passager(liste_bus)
    elif valeur == "7":
        gerer_passager_bus.acceuil_passager_bus(liste_bus)
    elif valeur == "8":
        gerer_passager_bus.afficher_liste_passager_bus(liste_bus)
    elif valeur == "9":
        gerer_passager_bus.liste_passager_flotte(liste_passager)
    elif valeur == "10":
        gerer_passager_bus.passager_flotte_bus(liste_bus)
    elif valeur == "11":
        liste_bus = creer_bus.delete_bus()
    elif valeur == "12":
        delete = creer_passager.supprimer_passager(liste_bus)
        liste_passager = delete[0]
        liste_bus = delete[1]
    elif valeur == "q":
        break

    
        





   




























