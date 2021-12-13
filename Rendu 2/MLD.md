# __MLD__ <br/>
Parking (#adresse : varchar, #nom : varchar, zone=>Zone)
<br/>
Zone (#nom : varchar, prix : integer)
<br/>
Place (#num : integer, parking=>Parking, emplacement : Type_emplacement, véhicule : Type_véhicule, status : Status)
<br/>
Utilisateur (#ID : integer, nom : varchar, prenom : varchar, num_abonne : integer, CB : string, prix_abo : integer, actif : bool, type : Type_utilisateur)
<br/>
Vehicule (#IMAT : varchar, utilisateur=>Utilisateur, Vehicule : Type_véhicule)
<br/>
Reservation (#ID : integer, véhicule=>Vehicule, prix : integer, début : date, fin : date)
<br/>
Transaction (#ID :integer, date : date, moyen_paiement : Moyen_payement, machine : Type_machine, heure_arrivee : time, imat=>Vehicule(IMAT), place=>Place(num), type : Type_transaction) //contraintes en fct machine
<br/>


# Types :
Type_emplacement : enum {plein_air, couverte}
<br/>
Type_véhicule : enum {voiture, deux_roues, camion}
<br/>
Status : enum {libre, occupe, reserve}
<br/>
Moyen_payement : enum {CB, cash}
<br/>
Type_machine : enum {Automate, Guicher, En ligne}
<br/>
Type_utilisateur : enum { Abonné, Occasionnel }
<br/>
Type_transaction : enum { Occasionnel, Abonnement }


# Contraintes : 
On supprime le ticket quand la voiture sort
<br/>

