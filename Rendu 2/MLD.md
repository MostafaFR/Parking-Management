# __MLD__ <br/>
* Parking (#adresse : varchar, #nom : varchar, zone=>Zone)

* Zone (#nom : varchar, prix : integer)

* Place (#num : integer, parking=>Parking, emplacement : Type_emplacement, véhicule : Type_véhicule, status : Status)

* Utilisateur (#ID : integer, nom : varchar, prenom : varchar, num_abonne : integer, CB : string, prix_abo : integer, actif : bool, type : Type_utilisateur)

* Vehicule (#IMAT : varchar, utilisateur=>Utilisateur, Vehicule : Type_véhicule)

* Reservation (#ID : integer, véhicule=>Vehicule, prix : integer, début : date, fin : date)

* Transaction (#ID :integer, date : date, moyen_paiement : Moyen_payement, machine : Type_machine, heure_arrivee : time, imat=>Vehicule(IMAT), place=>Place(num), type : Type_transaction)  // contraintes en fct machine



# Types :
* Type_emplacement : enum {plein_air, couverte}

* Type_véhicule : enum {voiture, deux_roues, camion}

* Status : enum {libre, occupe, reserve}

* Moyen_payement : enum {CB, cash}

* Type_machine : enum {Automate, Guicher, En ligne}

* Type_utilisateur : enum { Abonné, Occasionnel }

* Type_transaction : enum { Occasionnel, Abonnement }


# Contraintes : 
* On supprime le ticket quand la voiture sort.

* Un utilisateur ne peut pas entrer dans le parking / prendre un ticket, si celui-ci est plein.

* Un ticket non payé ne permet pas à l'utilisateur de sortir.

* Un abonnement est limité à un unique véhicule.

* Une réservation est liée à un unique utilisateur.

* Paiement sur l'automate uniquement via CB (sinon CB et Cash sur les guichets)
