# __MLD__ <br/>
* Parking (#adresse : varchar, #nom : varchar, zone=>Zone)

* Zone (#nom : varchar, prix : integer)

* Place (#num : integer, #parking=>Parking, emplacement : Type_emplacement, véhicule : Type_véhicule, status : Status)

* Utilisateur (#ID : integer, nom : varchar, prenom : varchar, num_abonne : integer, CB : string, prix_abo : integer, actif : bool, type : Type_utilisateur)

* Vehicule (#IMAT : varchar, utilisateur=>Utilisateur, Vehicule : Type_véhicule)

* Reservation (#ID : integer, véhicule=>Vehicule, prix : integer, début : date, fin : date)

* Transaction (#ID :integer, date : date, moyen_paiement : Moyen_payement, machine : Type_machine, heure_arrivee : time, imat=>Vehicule(IMAT), place=>Place(num), type : Type_transaction)       // contraintes en fct machine



# Types :
* enum Type_emplacement {plein_air, couverte}

* enum Type_véhicule {voiture, deux_roues, camion}

* enum Status {libre, occupe, reserve}

* enum Moyen_payement {CB, cash}

* enum Type_machine {Automate, Guicher, En ligne}

* enum Type_utilisateur {Abonné, Occasionnel}

* enum Type_transaction {Occasionnel, Abonnement}


# Contraintes : 
* prix.Zone NOT NULL

* nom.Utilisateur & prenom.Utilisateur NOT NULL

* prix.Reservation NOT NULL


# Choix d'héritage
* 
