# __MLD__ <br/>
Parking (#adresse : varchar, nom : varchar, zone=>Zone)
<br/>
Zone (#nom : varchar, prix : integer)
<br/>
Place (#num : integer, parking=>Parking, emplacement : Type_emplacement, véhicule : Type_véhicule, status : Status)
<br/>
Utilisateur (#ID : integer, nom : varchar, prenom : varchar)
<br/>
Vehicule (#IMAT : varchar, utilisateur=>Utilisateur, Vehicule : Type_véhicule)
<br/>
Reservation (#ID : integer, véhicule=>Vehicule, prix : integer, début : date, fin : date)
<br/>
Transaction (#ID :integer, date : date, moyen_paiement : Moyen_payement, machine : Type_machine) //contraintes en fct machine
<br/>
Ticket (#heure_arrivee : time, imat=>Vehicule(IMAT), place=>Place(num))
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

# Contraintes : 
On supprime le ticket quand la voiture sort
<br/>

