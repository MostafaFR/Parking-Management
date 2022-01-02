CREATE TYPE EEmplacement AS ENUM ('Plein_Air', 'couvert');
CREATE TYPE EVehicule AS ENUM ('deux_roues','camion','simple');
CREATE TYPE EPaiement AS ENUM ('Espece','Cartebleu');
CREATE TYPE EBorne AS ENUM ('Guichet','Automate');
CREATE TYPE EStatus AS ENUM ('libre','occupe','reserve');
CREATE TYPE ETransaction AS ENUM ('occasionnel','abonnement');

CREATE TABLE Zone(
Nom VARCHAR PRIMARY KEY,
Prix INTEGER
);

CREATE TABLE Parking(
idPark SERIAL PRIMARY KEY,
Nom VARCHAR,
Adresse VARCHAR UNIQUE,
Zone VARCHAR, 
FOREIGN KEY (Zone) REFERENCES Zone(Nom)
);

CREATE TABLE Place(
NumPlace SERIAL UNIQUE,
Parking INTEGER,
FOREIGN KEY (Parking) REFERENCES Parking(idPark),
Emplacement EEmplacement,
Vehicule EVehicule,
Status EStatus,
PRIMARY KEY (NumPlace, Parking)
);

CREATE TABLE Utilisateur(
idUser SERIAL PRIMARY KEY,
Nom VARCHAR,
Prenom VARCHAR,
parking INTEGER,
FOREIGN KEY (parking) REFERENCES Parking(idPark)
);

CREATE TABLE UtilisateurAbonne(
idUser SERIAL ,
login VARCHAR,
Password VARCHAR,
FOREIGN KEY (idUser) REFERENCES Utilisateur(idUser),
NumeroAbonne INTEGER,
Carte INTEGER,
PtsdeFIdelite INTEGER,
Actif BOOLEAN,
PRIMARY KEY(idUser, NumeroAbonne)
);

CREATE TABLE Vehicule(
IMAT VARCHAR PRIMARY KEY, 
Utilisateur INTEGER UNIQUE, 
Type EVEHICULE,
FOREIGN KEY (Utilisateur) REFERENCES Utilisateur(idUser)
);

CREATE TABLE Reservation (
idResa SERIAL PRIMARY KEY, 
Vehicule VARCHAR, 
Prix FLOAT, 
Debut DATE,
Fin DATE,
Utilisateur INTEGER,
Place INTEGER,
Type EVEHICULE,
FOREIGN KEY (Utilisateur) REFERENCES Utilisateur(idUser),
FOREIGN KEY (Place) REFERENCES Place(NumPlace)
);

CREATE TABLE Transaction(
idTransac SERIAL PRIMARY KEY,
tdate DATE,
moyenPaiement EPaiement,
machine EBorne,
heureArrivee DATE,
heureSortie DATE,
imat VARCHAR,
place INTEGER,
type ETransaction,
FOREIGN KEY (IMAT) REFERENCES Vehicule(IMAT),
FOREIGN KEY (place) REFERENCES Place(NumPlace),
  CHECK (
    (machine='Automate' AND moyenPaiement='Cartebleu')
    OR
    (machine='Automate' AND (moyenPaiement='Cartebleu' OR moyenPaiement='Espece'))
    )
);


INSERT into Zone values (%s,%s);
INSERT into Parking (idPark, Nom , Adresse , Zone) values (%s,%s,%s);
INSERT into Place (NumPlace, Parking , Emplacement , Vehicule, Status  ) values (%s,%s,%s,%s);
INSERT into Utilisateur (idUser, Nom, Prenom, parking) values (%s,%s,%s,%s);
INSERT into UtilisateurAbonne (idUser, login, Password, NumeroAbonne, Carte, PtsdeFIdelite, Actif) values (%s,%s,%s,%s,%s,%s,%s);
INSERT into Vehicule (IMAT, Utilisateur, Type) values (%s,%s,%s);
INSERT into Reservation (idResa, Vehicule, Prix, Debut, Fin, Utilisateur, Place) values (%s,%s,%s,%s,%s,%s,%s);
INSERT into Transaction (idTransac, tdate, moyenPaiement, machine, heureArrivee, heureSortie, imat, place, ETransaction) values (%s,%s,%s,%s,%s,%s,%s,%s,%s);


DROP TABLE Transaction;
DROP TABLE Reservation;
DROP TABLE Vehicule;
DROP TABLE UtilisateurAbonne;
DROP TABLE Utilisateur;
DROP TABLE Place;
DROP TABLE Parking;
DROP TABLE Zone;