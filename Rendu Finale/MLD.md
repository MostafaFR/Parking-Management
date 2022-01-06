# __MLD__ <br/>
* Parking (#idPark : serial, adresse : varchar, nom : varchar, zone=>Zone, nbPlacesMax : integer)

* Zone (#nom : varchar, prix : integer)

* Place (#num : serial, parking=>Parking, emplacement : Type_emplacement, véhicule : Type_véhicule, status : Status)

* Utilisateur (#idUser : serial, nom : varchar, prenom : varchar)

*UtilisateurAbonne(#idUser=>Utilisateur, login : string, password : string, num_abonne : serial,  CB : string, prix_abo : integer, actif : bool)

* Vehicule (#IMAT : varchar, utilisateur=>Utilisateur, Vehicule : Type_véhicule)

* Reservation (#idResa : serial, place=>Place, véhicule=>Vehicule, prix : integer, début : date, fin : date)

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

* adresse.Parking UNIQUE

* login.UtilisateurAbonne UNIQUE

* CB.UtilisateurAbonne UNIQUE

* prix.Zone NOT NULL

* nom.Utilisateur & prenom.Utilisateur NOT NULL

* prix.Reservation NOT NULL


# Choix d'héritage
* Utilisateur: On fait une spécialisation pour utilisateur abonné, il ne serait pas optimal de créer une table supplémentaire pour Utilisateuroccasionnel puisqu'elle ne comporterait pas plus d'attributs qu'Utilisateur.

* Transactions: 
