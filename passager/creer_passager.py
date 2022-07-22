# creer passager
import copy


passager ={
    'id' : "id_unique",
    'nom' : 'name',
    'poids_bagage' : 0
}

liste_passager = []

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





















