import copy

bus = {
    'id' : '',
    'poids_bagage_bus' : 1500,
    'place' : 0,
    'passager' : []
}

liste_bus = []
liste_id = []

def generer_bus(id, place):
    nouveau_bus = copy.deepcopy(bus)
    nouveau_bus['id'] = id
    nouveau_bus['place'] = place
    liste_bus.append(nouveau_bus)
    print(f"le bus {id} a bien été crée")
    return nouveau_bus

def verifier_id(id):
    for bus in liste_bus:
        if bus['id'] == id:
            return True
    return False

     


def creer_bus():
    place = input("entrer le nombre de place : ")
    if place.isdigit():    #isdigit permet de verifier qu'une variable contient un chiffre
        place = int(place)
        id = input("Entrer l'id du bus : ")
        id_correct = verifier_id(id)
        if verifier_id:
       
            while(id_correct):
                id = input("Entrer l'id du bus : ")
                id_correct = verifier_id(id)
       
        return generer_bus(id, place)
    else:
        return creer_bus()

            
def nombre_de_place(liste_bus):
    id_bus = input("entrez l'id du bus : ")
    if verifier_id(id_bus):
        for bus in liste_bus:
            if id_bus == bus["id"]:
                nombre_de_place = bus["place"] - len(bus["passager"])
                print(f"le nombre de place disponible est de {nombre_de_place}")
                break
            else:
                continue
    else:
        pass

def calculate_nombre_place(bus1):
    nombre_de_place = bus1["place"] - len(bus1["passager"])
    return nombre_de_place



def nombre_kg_bus():
    id_bus = input("entrez l'id du bus : ")
    if verifier_id(id_bus):
        for bus in liste_bus:
            if id_bus == bus["id"]:
                nombre_kg_bus = bus['poids_bagage_bus']
                poid = 0
                for passager in bus["passager"]:
                    poid = poid + int(passager["poids_bagage"])
                poids_restant = nombre_kg_bus - poid
                print(f"ce bus supporte {nombre_kg_bus} kg")
                print(f"le poids disponible pour ce bus est de {poids_restant} kg")
                break
            else:
                continue
    else:
        pass
        
def calculate_poids_restant(bus1):
    nombre_kg_bus = bus1['poids_bagage_bus']
    poid = 0
    for passager in bus1["passager"]:
        poid = poid + int(passager["poids_bagage"])
    poids_restant = nombre_kg_bus - poid
    return poids_restant


def delete_bus():
    id_bus = input("entrez l'id du bus : ")
    if verifier_id(id_bus):
        for bus in liste_bus:
            if bus["id"] == id_bus:
                liste_bus.remove(bus)
                return liste_bus
            else:
                continue
    else:
        print("ce bus n'existe pas ")
        return liste_bus

























