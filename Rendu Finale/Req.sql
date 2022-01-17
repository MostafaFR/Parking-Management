CREATE TYPE EEmplacement AS ENUM ('pleinAir', 'couvert');
CREATE TYPE EVehicule AS ENUM ('deuxRoues','camion','simple');
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
NbMaxPlaces INTEGER,
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
Carte BIGINT,
PtsdeFIdelite INTEGER,
Actif BOOLEAN,
PRIMARY KEY(idUser, NumeroAbonne)
);

CREATE TABLE Vehicule(
IMAT VARCHAR PRIMARY KEY, 
Utilisateur INTEGER, 
Type EVEHICULE,
FOREIGN KEY (Utilisateur) REFERENCES Utilisateur(idUser)
);

CREATE TABLE Reservation (
idResa SERIAL PRIMARY KEY, 
Vehicule VARCHAR, 
Prix FLOAT, 
Debut TIMESTAMP,
Fin TIMESTAMP,
Utilisateur INTEGER,
Place INTEGER,
Type EVEHICULE,
FOREIGN KEY (Utilisateur) REFERENCES Utilisateur(idUser),
FOREIGN KEY (Place) REFERENCES Place(NumPlace)
);

CREATE TABLE Transaction(
idTransac SERIAL PRIMARY KEY,
tdate TIMESTAMP,
moyenPaiement EPaiement,
machine EBorne,
heureArrivee TIMESTAMP,
heureSortie TIMESTAMP,
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

----------------- Initialisation ---------------------------------------------------

/* -------------------- Zones -------------------*/

INSERT into Zone values ('Periurbain',2.5);
INSERT into Zone values ('Centre',3);
INSERT into Zone values ('Commercial',2);

/* -------------------- Parkings -------------------*/

INSERT into Parking (Nom , Adresse , Zone, NbMaxPlaces) values ('Halles', '9 Rue St Jean' , 'Centre' , 120);
INSERT into Parking (Nom , Adresse , Zone, NbMaxPlaces) values ('Cordeliers', '1 Avenue Cordeliers', 'Centre', 70);
INSERT into Parking (Nom , Adresse , Zone, NbMaxPlaces) values ('Auchan', '3 Rue St Joseph','Commercial', 250);
INSERT into Parking (Nom , Adresse , Zone, NbMaxPlaces) values ('Jardiland', '12 Rue des Arbres','Periurbain', 400);


/* -------------------- Places -------------------*/

INSERT into Place (Parking , Emplacement , Vehicule, Status) values (1, 'couvert', 'simple', 'libre');
INSERT into Place (Parking , Emplacement , Vehicule, Status) values (1, 'couvert', 'simple', 'occupe');
INSERT into Place (Parking , Emplacement , Vehicule, Status) values (1, 'couvert', 'simple', 'reserve');

INSERT into Place (Parking , Emplacement , Vehicule, Status) values (3, 'pleinAir', 'simple', 'libre');
INSERT into Place (Parking , Emplacement , Vehicule, Status) values (3, 'pleinAir', 'simple', 'occupe');
INSERT into Place (Parking , Emplacement , Vehicule, Status) values (3, 'pleinAir', 'simple', 'libre');

INSERT into Place (Parking , Emplacement , Vehicule, Status) values (4, 'pleinAir', 'simple', 'libre');
INSERT into Place (Parking , Emplacement , Vehicule, Status) values (4, 'pleinAir', 'simple', 'occupe');
INSERT into Place (Parking , Emplacement , Vehicule, Status) values (4, 'pleinAir', 'simple', 'libre');


/* -------------------- Utilisateurs -------------------*/

INSERT into Utilisateur (Nom , Prenom, parking) 
VALUES ('Spencer', 'Judy', 1);
INSERT into Utilisateur (Nom , Prenom, parking) 
VALUES ('Judah', 'Patel', 3);
INSERT into Utilisateur (Nom , Prenom, parking) 
VALUES ('Leondra', 'Reid', 1);
INSERT into Utilisateur (Nom , Prenom, parking) 
VALUES ('Andrews', 'Simone', 2);
INSERT into Utilisateur (Nom , Prenom, parking) 
VALUES ('Ashley', 'Josephine', 3);


/* -------------------- Utilisateurs Abonnés -------------------*/

INSERT into UtilisateurAbonne (login, password, NumeroAbonne, carte, PtsdeFIdelite, Actif) 
VALUES ('jashley', 'FhpYfbEduRf8', 0654, 5480154835480135, 100, TRUE);

INSERT into UtilisateurAbonne (login, password, NumeroAbonne, carte, PtsdeFIdelite, Actif) 
VALUES ('sandrews', 'E4yVR7z7YA3i', 3618, 1548674735488874, 450, FALSE);

INSERT into UtilisateurAbonne (login, password, NumeroAbonne, carte, PtsdeFIdelite, Actif) 
VALUES ('jspencer', 'sEe5HfQRKq96', 4770, 1461457599867754, 1200, TRUE);


/* -------------------- Vehicule -------------------*/

INSERT into Vehicule (IMAT , Utilisateur , Type) 
VALUES ('DD451FR', 1, 'simple');
INSERT into Vehicule (IMAT , Utilisateur , Type) 
VALUES ('SF363DF', 1, 'deuxRoues');
INSERT into Vehicule (IMAT , Utilisateur , Type) 
VALUES ('GH811CX', 2, 'simple');
INSERT into Vehicule (IMAT , Utilisateur , Type) 
VALUES ('VJ982AZ', 3, 'simple');
INSERT into Vehicule (IMAT , Utilisateur , Type) 
VALUES ('VC874ZZ', 4, 'simple');
INSERT into Vehicule (IMAT , Utilisateur , Type) 
VALUES ('AA662VB', 5, 'simple');


/* -------------------- Reservation -------------------*/

INSERT into Reservation (Vehicule, Prix, Debut, Fin, Utilisateur, Place, Type) 
VALUES ('DD451FR', 3.50, '2022-01-22 14:05:00', '2022-01-22 17:45:00', 1, 4, 'simple');

INSERT into Reservation (Vehicule, Prix, Debut, Fin, Utilisateur, Place, Type) 
VALUES ('VJ982AZ', 13.50, '2022-02-04 10:24:00', '2022-02-08 06:45:00', 3, 1, 'simple');

/* -------------------- Transaction -------------------*/

INSERT into Transaction (tdate, moyenPaiement, machine, heureArrivee, heureSortie, imat, place, ETransaction) 
VALUES ('2022-01-28 18:05:00', 'Cartebleu', 'Guichet', '2022-01-02 10:24:00', '2022-02-04 13:48:00', 'AA662VB', 2, 'occasionnel');

