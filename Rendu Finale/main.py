#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname='ai23a002' user='me' host='tuxa.sme.utc' password='kZRpoz2T'")
cur = conn.cursor()

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


def afficher_voitures_utilsateur(User):
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
