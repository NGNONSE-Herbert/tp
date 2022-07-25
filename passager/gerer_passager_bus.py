

from creer_bus import calculate_nombre_place, calculate_poids_restant, nombre_de_place, verifier_id
import creer_passager 



def ajouter_Passager_Au_bus(liste_bus, liste_passager):    
    true = True
    while true:   
        id_bus = input("entrez l'id du bus : ")
        if verifier_id(id_bus):
            position_bus = 0
            for bus in liste_bus:
                if id_bus == bus['id']:
                    break
                else:
                    position_bus += 1
            t = True
            while t:
                id_passager = input("entrez l'id du passager : ")

                if creer_passager.verifie_Id_Passager(id_passager):
                        for passager in liste_bus[position_bus]['passager']:
                            if id_passager == passager["id"]:
                                print("le passager existe deja dans ce bus")
                                t = True
                                return liste_bus
                            else:
                                continue
                        for passager in liste_passager:
                            if id_passager == passager['id']:
                                bus1 = liste_bus[position_bus]
                                nombre_de_place = calculate_nombre_place(bus1)
                                poid_restant = calculate_poids_restant(bus1)
                                poid_restant = poid_restant - passager["poids_bagage"]
                                if nombre_de_place > 0 and poid_restant > 0:

                                    liste_bus[position_bus]["passager"].append(passager)
                                    nom = passager["nom"]
                                    print(f"le passager {nom} a été bien ajouté au bus {id_bus} ")
                                    return liste_bus
                                elif nombre_de_place <= 0:
                                    print("il n'y a plus de place disponible")
                                    return liste_bus
                                else:
                                    print("le passager ne peut etre ajoute au bus a cause du poids de ces bagages")
                                    return liste_bus
                            else:
                                continue
                else:
                    continue
               
        else:
            continue
        

def delete_passager(liste_bus):
    id_bus = input("entrez l'id du bus : ")
    if verifier_id(id_bus):
        id_passager = input("entrez l'id du passager : ")
        if creer_passager.verifie_Id_Passager(id_passager):
            for bus in liste_bus:
                if id_bus == bus["id"]:
                    for passager in bus["passager"]:
                        if id_passager == passager["id"]:
                            nom = passager["nom"]
                            bus["passager"].remove(passager)
                            print(f"le passager {nom} a été retiré avec succes du bus {id_bus}")
                            return liste_bus
                        else:
                            continue
                else:
                    continue
        else:
            print("l'id du passager est incorrect")
            return liste_bus
    else:
        print("l'id du bus est incorrecte")
        return liste_bus




def acceuil_passager_bus(liste_bus):
    nombre_de_place = 0
    nombre_de_place1 = 0
    id_bus = input("Entrez l'id du bus vers lequel on veut transferer les passagers : ")
    if verifier_id(id_bus):
        for bus in liste_bus:
            if id_bus == bus["id"]:
                nombre_de_place = int(bus["place"]) - len(bus["passager"])
                break
            else:
                continue
        id_bus1 = input("Entrez l'id du bus vers lequel on veut prendre les passagers ")
        if verifier_id(id_bus1):
            for bus in liste_bus:
                if id_bus1 == bus["id"]:
                    nombre_de_place1 = len(bus["passager"])
                    break
                else:
                    continue
            if nombre_de_place >= nombre_de_place1:
                print(f"le bus {id_bus} peut recevoir les passagers du bus {id_bus1}")
            elif nombre_de_place < nombre_de_place1:
                print(f"le bus {id_bus} ne peut pas recevoir les passagers du bus {id_bus1}")
            else:
                print(f"le bus {id_bus} ne peut pas recevoir les passagers du bus {id_bus1}")
        else:
            print("ce bus n'existe pas")
    else:
        print("ce bus n'existe pas")

def afficher_liste_passager_bus(liste_bus):
    id_bus = input("entrez l'id du bus : ")
    if verifier_id(id_bus):
        for bus in liste_bus:
            if id_bus == bus["id"]:
                if len(bus["passager"]) > 0:
                    print("la liste des passagers est : ")
                    for passager in bus["passager"]:
                        id = passager["id"]
                        nom = passager["nom"]
                        print(f" {id} : {nom}")
                else:
                    print(f"le bus {id_bus} n'a pas encore de passager")
            else:
                continue
    else:
        print(f"le bus {id_bus} n'existe pas ")

def liste_passager_flotte(liste_passager):
    if len(liste_passager) > 0:
        print("la liste des passagers de ma flotte est : ")
        for passager in liste_passager:
            id = passager["id"]
            nom = passager["nom"]
            print(f" {id} : {nom}")
    else:
        print("ma flotte ne contient aucun passager")

    
def passager_flotte_bus(liste_bus):
    id_passager = input("entrez l'id du passager : ")
    if creer_passager.verifie_Id_Passager(id_passager):
        valeur = 0
        for bus in liste_bus:
            for passager in bus["passager"]:
                if id_passager == passager["id"]:
                    id = bus["id"]
                    place_max = bus["place"]
                    place_occupe = len(bus["passager"])
                    print(f" le passager {id_passager} est present dans le bus : \n {id} : place max : {place_max} place occupe : {place_occupe}")
                    valeur += 1
                else:
                    continue
        if valeur == 0:
            print("le passager n'est present dans aucun bus ")
            
    else:
        print(f"le passager {id_passager} n'existe pas ")



    


                    
                    
                
                


        
        
























