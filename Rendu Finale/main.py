#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname='ai23a002' user='me' host='tuxa.sme.utc' password='kZRpoz2T'")
cur = conn.cursor()


"""
sql = "SELECT num, nom, population FROM dpt2 ORDER BY num";
cur.execute(sql)
print ("\t[N°] Nom (Population)")
row = cur.fetchone()
while row:
  print("\t[%s] %s (%s)" % (row[0], row[1], row[2]))
  row = cur.fetchone()

print()

sql = "SELECT MAX(population) FROM dpt2";
cur.execute(sql)
row = cur.fetchone()
print("\n> Département le plus peuplé :", row[0]);

sql = "SELECT MIN(population) FROM dpt2";
cur.execute(sql)
row = cur.fetchone()
print("\n> Département le moins peuplé :", row[0]);
"""


def main():
    cont = 1
    while cont == 1:
        menu()
        cont = int(input("Continuer ? 1 si oui, 0 si non\n> "))
    conn.close()
    print(conn)
    return 0

def menu():
    print("\nListe requêtes :")
    print(" 1.   Liste des Parkings")
    print(" 2.   Liste des Utilisateurs")
    print(" 3.   Afficher toutes les Places Disponibles")
    print(" 4.   Afficher toutes les Places Disponibles Pour un Parking")
    print(" 5.   Ajouter un Utilisateurs")
    print(" 6.   Ajouter un Vehicule")
#    print(" 7.   Reserver une Place")
    print(" Autre.. TO DO")

    choice = int(input("Choix : "))

    if choice == 1:
        liste_parking()
    
    if choice == 2:
        liste_users()

    if choice == 3:
        places_dispo()
        
    if choice == 4:
        places_dispoP()

    if choice == 5:
        ajouterUtilisateur(user)

    if choice == 6:
        ajouterVehicule()

# Affiche les infos basiques de chaque parking
def liste_parking():
    sql = "SELECT Nom FROM Parking"
    cur.execute(sql)
    res = cur.fetchall()
    for raw in res:
        print (raw[0])


# Affiche les infos basiques de chaques users
def liste_users():
    sql = "SELECT Nom, Prenom FROM Utilisateur"
    cur.execute(sql)
    res = cur.fetchall()
    for raw in res:
        print (raw[0] raw[1])



# Récupère en temps réel le nombres de places dispo dans chaque parking (ex 80 places : 14 libres / 52 occupées / 14 réservées)
def places_dispo():
    sql = "SELECT Parking.Nom ,Parking.NbMaxPlaces, COUNT(Numplace) FROM Parking LEFT JOIN Place ON Place.Parking=Parking.idPark WHERE status='occupe' OR status='reserve' GROUP BY Parking.idPark "
    cur.execute(sql)
    res = cur.fetchall()
    for raw in res:
        print (raw[0] raw[1]-raw[2])


# Récupère en temps réel le nombres de places dispo un parking (ex 80 places : 14 libres / 52 occupées / 14 réservées)
def places_dispoP():
    name=input("Nom du parking : ")

    sql = "SELECT Parking.Nom ,Parking.NbMaxPlaces, COUNT(Numplace) FROM Parking LEFT JOIN Place ON Place.Parking=Parking.idPark WHERE (status='occupe' OR status='reserve') AND Parking.Nom = %s GROUP BY Parking.idPark " %name
    cur.execute(sql)
    res = cur.fetchall()
    for raw in res:
        print (raw[0] raw[1]-raw[2])


def ajouterUtilisateur():
    nom = input("Entrer son nom : ")
    prenom = input("Entrer son prenom : ")
    return ajoutUtilisateur(nom,prenom)



def ajoutUtilisateur(nom,prenom):

    id=recherche_utilisateur(nom, prenom)
    if id!="null":
        print("Cet utilisateur est déjà référencé.")
        return id

    sql = "INSERT INTO Utilisateur (nom, prenom);"
    cur.execute(sql)
    return recherche_utilisateur(nom, prenom)
        

def ajouterVehicule():
    imat = input("Entrer la plaque d'immatriculation : ")
    if len(cur.execute("SELECT imat FROM Vehicule WHERE imat ='%s'")%imat) == 0:
        print("Ce vehicule n'est pas encore référencé. Nous l'ajouterons à notre database après la saisie de vos informations...")
        id = ajouterUtilisateur()
        type = input("Entrer son type : ")
        while type not in {"deuxRoues","camion","simple"}:
            print("Vous devez choisir entre deuxRoues, camion et simple")
            type = input("Entrer son type : ")

        sql = "INSERT INTO Vehicule (IMAT, Utilisateur, Type) values (%s,%s,%s)" %(imat,id,type)
        cur.execute(sql)
    else 
        print("Ce vehicule est déjà référencé.")

def recherche_utilisateur(nom, prenom):
    if len(cur.execute("SELECT nom, prenom FROM Utilisateur WHERE nom ='%s' AND prenom = '%s'")%nom, %prenom) == 0:
        print("Cet utilisateur n'est pas encore référencé.")
        return "null"

    else
        sql= "SELECT idUser FROM Utilisateur WHERE nom ='%s' AND prenom = '%s'"%(nom,prenom)
        cur.execute(sql)
        res = cur.fetchone()
        for raw in res:
            return raw[0]

def afficher_voitures_utilisateur(User):
        utilisateur = User.utilsateur_text.displayText()
        try:
            sql = "SELECT  imat, Type FROM Vehicule WHERE utilisateur='%s'"%utilisateur
            User.cursor.execute(sql)
            results = User.cursor.fetchone()
        except:
            print('Couldnt connect to database')         
        if results:
            position = 0
            while results :
                print(results)
                results = User.cursor.fetchone()
                position+= 1
