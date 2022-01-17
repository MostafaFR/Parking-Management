#!/usr/bin/python3

import psycopg2

def MIdentificationUtilisateur(conn,cursor):
    print("\n\n_________________________________________________")
    print("\Bienvenue sur l'interface de gestion des parkings")
    print("_________________________________________________")
    print("Vous etes :")
    print("1\ Administrateur")
    print("2\ Utilisateur abonnee")
    print("3\ Utilisateur occasionnel")
    print("0\ Quitter")

    choix = int(input("Choix : "))
    
    if choix == 1:
        MAdmin(conn,cur)
    elif choix == 2:
        MAbonne(conn,cur)
    elif choix == 3:
        MOccasionnel(conn,cur)
    elif choix==0:
        exit()
    MIdentificationUtilisateur(conn,cur)

def MAdmin(conn,cur):
    print("\n\n_________________________________________________")
    print("Menu Administrateur")
    print("_________________________________________________")
    print("Liste requetes :")
    print("1\ Gestion des parkings")
    print("2\ Gestion des utilisateurs")
    print("3\ Gestion des reservation")
    print("0\ Menu Principal")

    choice = int(input("Choix : "))

    if choice == 1:
        gestion_parking(conn,cur)
    if choice == 2:
        gestion_users(conn,cur)
    if choice == 3:
        gestion_places(conn,cur)
    if choice == 0:
        MIdentificationUtilisateur(conn,cur)
    MAdmin(conn,cur)
    
def MOccasionnel(conn,cur, utilisateur=0):
    print("\n\n_________________________________________________")
    print("Menu Occasionnel")
    print("_________________________________________________")
    if utilisateur == 0:
        utilisateur = input("Identifiant : ")
    req = "SELECT * FROM Utilisateur WHERE idUser = '%s'" % (utilisateur)
    cur.execute(req)
    results = cur.fetchall()
    if len(results) == 0:
        print("Erreur mauvais identifiant")
        return 0
    else :
        print("\nListe requetes :")
        print("1\ Gerer vehicule")
        print("2\ Reserver une place")
        print("3\ Voir mes reservations")
        print("0\ Menu Principal")

        choice = int(input("Choix : "))

        if choice == 1:
            gererVehicule(conn,cur,utilisateur)
        elif choice == 2:
            FaireReservation(conn,cur,utilisateur)
        elif choice == 3:
            voirReservation(conn,cur,utilisateur)
        elif choice == 0:
            MIdentificationUtilisateur(conn,cur)
        else: MOccasionnel(conn,cur, utilisateur)
    

def MAbonne(conn,cur, login=0):
    try:
        if login == 0 :
            login = input("Login : ")
            mdp = input("Mot de passe : ")
            req = "SELECT * FROM UtilisateurAbonne WHERE login = '%s' AND Password='%s'" % (login, mdp)
        else:
            req = "SELECT * FROM UtilisateurAbonne WHERE login = '%s'" % (login)
    except:
        print("Erreur")

    cur.execute(req)
    results = cur.fetchall()
    if len(results) == 0:
        print("Erreur mauvaise combinaison")
        return 0
    else :
        print("\nListe requetes :")
        print("1\ Gerer compte")
        print("2\ Gerer vehicule")
        print("3\ Reserver une place")
        print("4\ Voir mes reservations")
        print("0\ Menu Principal")

        choice = int(input("Choix : "))

        if choice == 1:
            liste_parking(conn,cur)
        elif choice == 2:
            liste_users(conn,cur)
        elif choice == 3:
            places_dispo(conn,cur)
        elif choice == 0:
            MIdentificationUtilisateur(conn,cur)
        else : MAbonne(conn,cur, login)


# Affiche les infos basiques de chaque parking
def liste_parking(conn,cur):
    print()
    sql = "SELECT Nom FROM Parking"
    cur.execute(sql)
    res = cur.fetchall()
    for raw in res:
        print (raw[0])
    conn.commit()

# Affiche les infos basiques de chaques users
def liste_users(conn,cur):
    print()
    sql = "SELECT Nom, Prenom FROM Utilisateur"
    cur.execute(sql)
    res = cur.fetchall()
    for raw in res:
        print (raw[0],raw[1])
    conn.commit()

# Recupere en temps reel le nombres de places dispo dans chaque parking (ex 80 places : 14 libres / 52 occupees / 14 reservees)
def places_dispo(conn,cur):
    sql = "SELECT Parking.Nom ,Parking.NbMaxPlaces, COUNT(Numplace) FROM Parking LEFT JOIN Place ON Place.Parking=Parking.idPark WHERE status='occupe' OR status='reserve' GROUP BY Parking.idPark "
    cur.execute(sql)
    res = cur.fetchall()
    for raw in res:
        print (raw[0], raw[1]-raw[2])
    conn.commit()

# Recupere en temps reel le nombres de places dispo un parking (ex 80 places : 14 libres / 52 occupees / 14 reservees)
def places_dispoP(conn,cur):
    name=input("Nom du parking : ")

    sql = "SELECT Parking.Nom ,Parking.NbMaxPlaces, COUNT(Numplace) FROM Parking LEFT JOIN Place ON Place.Parking=Parking.idPark WHERE (status='occupe' OR status='reserve') AND Parking.Nom = %s GROUP BY Parking.idPark " %name
    cur.execute(sql)
    res = cur.fetchall()
    for raw in res:
        print (raw[0], raw[1]-raw[2])
    conn.commit()


def ajoutUtilisateur(conn, cur):

    nom = input("Entrer son nom : ")
    prenom = input("Entrer son prenom : ")
    id=recherche_utilisateur(nom, prenom)
    if id!="null":
        print("Cet utilisateur est deja reference.")
        return id

    sql = "INSERT INTO Utilisateur (nom, prenom);"
    cur.execute(sql)
    conn.commit()
    return recherche_utilisateur(nom, prenom)

def supprUtilisateur(conn, cur):
    try:
        sql = "SELECT  idUser FROM Utilisateur ;"
        cur.execute(sql)
        results = cur.fetchall()
    except:
        print('Couldnt connect to database')         
    if results:
        Users = []
        i = 0
        for res in results:
            Users.append(res)
            i+=1
            print(i)
        U = int(input("Veuillez selectionner le vehicule (chiffre) :"))
    else: print("Pas d'utilisateur")

    sql = "DELETE FROM Utilisateur WHERE idUser=%s"%U
    cur.execute(sql)
    conn.commit()
        
def ajouterVehicule(conn,cur, id=0):
    imat = input("Entrer la plaque d'immatriculation : ")
    if len(cur.execute("SELECT imat FROM Vehicule WHERE imat ='%s'")%imat) == 0:
        print("Ce vehicule n'est pas encore reference. Nous l'ajouterons a notre database apres la saisie de vos informations...")
        id = ajoutUtilisateur()
        type = input("Entrer son type : ")
        while type not in {"deuxRoues","camion","simple"}:
            print("Vous devez choisir entre deuxRoues, camion et simple")
            type = input("Entrer son type : ")

        sql = "INSERT INTO Vehicule (IMAT, Utilisateur, Type) values (%s,%s,%s)" %(imat,id,type)
        cur.execute(sql)
    else:
        print("Ce vehicule est deja reference.")
    return imat

def recherche_utilisateur(conn,cur, nom, prenom):
    if len(cur.execute("SELECT nom, prenom FROM Utilisateur WHERE nom ='%s' AND prenom = '%s'")%(nom,prenom)) == 0 :
        print("Cet utilisateur n'est pas encore reference.")
        return 0
    else:
        sql= "SELECT idUser FROM Utilisateur WHERE nom ='%s' AND prenom = '%s'"%(nom,prenom)
        cur.execute(sql)
        res = cur.fetchone()
    return res[0]

def recherche_utilisateur_abonne(conn,cur,id):
    if len(cur.execute("SELECT nom, prenom FROM Utilisateur WHERE idUser ='%s'")%(id)) == 0 :
        print("Cet utilisateur n'est pas abonne.")
        return 0
    else:
        sql= "SELECT idUser FROM Utilisateur WHERE idUser ='%s'"%(id)
        cur.execute(sql)
        res = cur.fetchone()
    return res[0]

# def afficher_voitures_utilisateur(conn,cur, User):
#         utilisateur = User.utilisateur_text.displayText()
#         try:
#             sql = "SELECT  imat, Type FROM Vehicule WHERE utilisateur='%s'" %utilisateur
#             User.cursor.execute(sql)
#             results = User.cursor.fetchone()
#         except:
#             print('Couldnt connect to database')         
#         if results:
#             position = 0
#             while results :
#                 print(results)
#                 results = User.cursor.fetchone()
#                 position+= 1


def gererVehicule(conn,cur,utilisateur): 
    print("1\ Voir vos véhicules")
    print("2\ Ajouter un véhicule")
    print("3\ Supprimer un véhicule")
    print("0\ Menu Principal")

    choice = int(input("Choix : "))

    if choice == 1:
        sql = "SELECT imat, Type FROM Vehicule WHERE utilisateur = '%s'" %utilisateur
        utilisateur.cursor.execute(sql)
        results = utilisateur.cursor.fetchone()
        if results:
            position = 0
            while results :
                print(results)
                results = utilisateur.cursor.fetchone()
                position+= 1

    elif choice == 2:
        imat = input("Donner l'IMAT : ")
        try:
            type = input("Donner le type ? {voiture, deux_roues, camion} :")
            sql = "INSERT INTO Vehicule (IMAT, Utilisateur, Type) values (%s,%s,%s)" %(imat,utilisateur,type)
            utilisateur.cursor.execute(sql)
        except:
            print("Problème Survenu")

    elif choice == 3:
        print()
        try:
            sql = "SELECT imat, Type FROM Vehicule WHERE utilisateur = '%s'" %utilisateur
            utilisateur.cursor.execute(sql)
            results = utilisateur.cursor.fetchone()
        except:
            print("Problème Survenu")
        if results:
            position = 0
            while results :
                print(results)
                results = utilisateur.cursor.fetchone()
                position+= 1
        imatToDelete = input("Entrez l'IMAT du véhicule à supprimer :")
        try:
            sql = "DELETE FROM Vehicule WHERE imat=%s)" %imatToDelete
        except:
            print("impossible de supprimer le véhicule")
        print("Véhicule Supprimé")
        
    elif choice == 0:  
        gererVehicule(conn,cur,utilisateur)

    return gererVehicule(conn,cur,utilisateur)


def FaireReservation(conn,cur,utilisateur):

     
    try:
        # demander parking
        parking = input("Donner le parking : ")

        #verfifier qu'il n'est pas plein
        sql = "SELECT Parking.NbMaxPlaces, COUNT(Numplace) FROM Parking LEFT JOIN Place ON Place.Parking=Parking.idPark WHERE status='occupe' OR status='reserve' GROUP BY Parking.idPark "
        cur.execute(sql)
        park=cur.fetchone()
        if (park[0]<=park[1]):
            print("Mes excuses mon seigneur il n'y a plus une place dans ce parking")
            return

        # regarder les places vides et en recuperer le prix
        sql="SELECT NumPlace,prix from place inner join parking inner join zone on Zone.nom=Parking.zone on Parking.idPark=Place.Parking where parking.nom = %s and place.status='libre'"%parking
        cur.execute(sql)
        park=cur.fetchone()
    except:
        print('Erreur') 

    try:

        id = recherche_utilisateur_abonne(utilisateur)
        if id == 0:
            prix=park[1]
        else:
            #recuperer reduction abonne 
            sql="SELECT PtsdeFIdelite from UtilisateurAbonne where id = %s" %id
            cur.execute(sql)
            res3=cur.fetchone()
            prix=park[1] - (res3[0]*park[1])/100
    except:
        print('Erreur') 

    try:
        sql = "SELECT  imat, Type FROM Vehicule WHERE utilisateur='%s'" %utilisateur
        cur.execute(sql)
        results = cur.fetchall()
    except:
        print('Couldnt connect to database')         
    if results:
        Veh = []
        i = 0
        for res in results:
            Veh.append(res)
            i+=1
            print(i)
        Vehicule = int(input("Veuillez selectionner le vehicule (chiffre) :"))
    else: Vehicule=ajouterVehicule(conn,cur, utilisateur)

    try:
        sql="SELECT Type FROM vehicule where imat=%s"%Vehicule
        cur.execute(sql)
        res=cur.fetchone()
        Typevehicule=res[0]
    except:
        print('Erreur') 

    emplacement=input("'couvert' ou 'pleinAir' ?")


    if not park :

        try:    
            sql = "INSERT INTO Place (parking, emplacement, Vehicule, Status) values (%s,%s,%s,'libre')" %(parking, emplacement, Typevehicule)
            cur.execute(sql)

            sql="SELECT NumPlace,prix from place inner join parking inner join zone on Zone.nom=Parking.zone on Parking.idPark=Place.Parking where parking.nom = %s and place.status='libre'"%parking
            cur.execute(sql)
            park=cur.fetchone()
        except:
            print("ERREUR")
   
    try:
        #recuperer dates
        debut = input("Veuillez selectionner la date de debut (AAAA-MM-JJ hh:mm:ss) :")
        fin = input("Veuillez selectionner la date de fin (AAAA-MM-JJ hh:mm:ss) :")
        
        sql= "INSERT into Reservation (Vehicule, Prix, Debut, Fin, Utilisateur, Place, Type) VALUES (%s,%s,%s,%s,%s,%s,%s)"%(Vehicule, prix, debut, fin, utilisateur, park[0], Typevehicule)
        cur.execute(sql)
    except:
        print('Erreur') 


def voirReservation(conn,cur,utilisateur):
    print()
    sql = " SELECT Place,Vehicule,EVEHICULE,Prix,Debut,Fin from Reservation join utilisateur on Utilisateur.idUser=Reservation.Utilisateur where utilisateur.idUser= '%s'" %utilisateur
    utilisateur.cursor.execute(sql)
    results = utilisateur.cursor.fetchall()
    for raw in results:
        print("Num de place: %s, imat: %s, Type de vehicule: %s, prix: %s, de %s jusque %s") %(raw[0],raw[1],raw[2],raw[3],raw[4],raw[5])


def gestion_parking(conn,cur):
    print("\n1\ Afficher tous les Parkings")
    print("2\ Ajouter un Parking")
    print("3\ Supprimer un Parking")
    print("0\ Menu Principal")

    choice = int(input("Choix : "))

    if choice == 1:
        sql = "SELECT nom FROM Parking"
        cur.execute(sql)
        results = cur.fetchone()
        if results:
            position = 0
            print()
            while results :
                print(results[0])
                results = cur.fetchone()
                position+= 1

    elif choice == 2:
        nom = input("Nom du parking à ajouter : ")
        adr = input("Adresse du parking à ajouter : ")
        nbPl = input("Nombre Places du parking à ajouter : ")
        zone = input("Num ID de la zone : ")
        try:
            sql = "INSERT INTO Parking (adresse, nom, zone, nbPlacesMax) values (%s,%s,%s,%s)" %(adr,nom, zone, nbPl)
            cur.execute(sql)
        except:
            print("Problème Survenu")

    elif choice == 3:
        print()
        try:
            nom = input("Nom du parking à supprimer : ")
            sql = "DELETE FROM Parking WHERE nom=%s)" %nom
            cur.execute(sql)
        except:
            print("Problème Survenu")
        print("Parking Supprimé")
        
    elif choice == 0:  
        MAdmin(conn,cur)
    
    gestion_parking(conn, cur)

def gestion_places(conn,cur):
    print("1\ Afficher tous les places")
    print("2\ Ajouter une place")
    print("3\ Supprimer une place")
    print("0\ Menu Principal")

    choice = int(input("Choix : "))

    if choice == 1:
        sql = "SELECT numPlace FROM Place"
        cur.execute(sql)
        results = cur.fetchone()
        if results:
            position = 0
            while results :
                print(results)
                results = cur.fetchone()
                position+= 1

    elif choice == 2:
        parking = input("Nom du parking à ajouter : ")
        emplacement = input("Adresse du parking à ajouter ('pleinAir', 'couvert') : ")
        vehicule = input("Nombre Places du parking à ajouter ('deuxRoues','camion','simple') :")
        status = input("Num ID de la zone ('libre','occupe','reserve') : ")
        try:
            sql = "INSERT INTO Place (parking, emplacement, Vehicule, Status) values (%s,%s,%s,%s)" %(parking,emplacement, vehicule, status)
            cur.execute(sql)
        except:
            print("Problème Survenu")

    elif choice == 3:
        print()
        try:
            num = input("Numero de la place a supprimer : ")
            sql = "DELETE FROM Place WHERE NumPlace=%s)" %num
            cur.execute(sql)
        except:
            print("Problème Survenu")
        print("Parking Supprimé")
        
    elif choice == 0:  
        MAdmin(conn,cur)
    
    gestion_parking(conn, cur)


def gestion_users(conn,cur):
    print("\n\n_________________________________________________")
    print("Gestion Utilisateur")
    print("_________________________________________________")
    print("Liste requetes :")
    print("1\ Creer un utilisateur")
    print("2\ Supprimer un utilisateur")
    print("3\ Afficher les utilisateurs")
    print("0\ Menu Principal")

    choice = int(input("Choix : "))

    if choice == 1:
        ajoutUtilisateur(conn, cur)
    if choice == 2:
        supprUtilisateur(conn, cur)
    if choice == 3:
        liste_users(conn,cur)
    if choice == 0:
        MAdmin(conn,cur)
    gestion_users(conn,cur)
    
if __name__=="__main__":
    HOST = "tuxa.sme.utc"
    USER = "ai23a002"

    PASSWORD = "kZRpoz2T"
    DATABASE = "dbai23a002"
    try:
        conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
        cur = conn.cursor()
    except:
        print("Erreur lors de la connexion")
    MIdentificationUtilisateur(conn, cur)
