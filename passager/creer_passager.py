# creer passager
import copy


passager ={
    'id' : "id_unique",
    'nom' : 'name',
    'poids_bagage' : 0
}

liste_passager = []
liste_bus_passager =[]

def generate_passager(id, nom, poids):
    nouveau_passager = copy.deepcopy(passager)
    nouveau_passager['id'] = id
    nouveau_passager['nom'] = nom
    nouveau_passager['poids_bagage'] = poids
    liste_passager.append(nouveau_passager)
    print(f"le passager {nom} a bien été crée")
    return nouveau_passager

def verifie_Id_Passager(id):
    for passager in liste_passager:
        if passager['id'] == id:
            return True
    return False

def creer_Passager():
    poids = input("entrez le poids des bagages du passager : ")
    if poids.isdigit():
        poids = int(poids)
        id = input("entrez l'id du passager : ")
        id_correct = verifie_Id_Passager(id)
        if verifie_Id_Passager:
            while(id_correct):
                id = input("entrez l'id de l'utilisateur : ")
                id_correct = verifie_Id_Passager(id)
            nom = input("entrez le nom du passager : ")
        return generate_passager(id, nom, poids)
    else:
        return creer_Passager()



def supprimer_passager(liste_bus):
    id_passager = input("entrez l'id du passager : ")
    if verifie_Id_Passager(id_passager):
        for passager in liste_passager:
            if passager["id"] == id_passager:
                liste_passager.remove(passager)
                liste_bus_passager.append(liste_passager)
                for bus in liste_bus:
                    for passager in bus["passager"]:
                        if id_passager == passager["id"]:
                            bus["passager"].remove(passager)
                        else:
                            continue
                liste_bus_passager.append(liste_bus)
                return liste_bus_passager
            else:
                continue
    else:
        print("le passager n'existe pas ")
        return liste_passager


















