from felhasznalok import Felhasznalo
from uzenetek import Üzenet
from datetime import datetime
import sqlite3
from flask_bcrypt import Bcrypt
from flask import Flask
app= Flask(__name__)
bcrypt = Bcrypt(app)
class App():

    def __init__(self) -> None:
        self.felhasznalok={}
        self.aktualis_felhasznalo=""
        self.id=0
    def jelszo_atalakitas(self,jelszo):
        return bcrypt.generate_password_hash(jelszo).decode('utf-8')


    def felhasznalo_mentes(self,felhasznalonev,jelszo,nev):
        self.felhasznalok[felhasznalonev]=Felhasznalo(felhasznalonev,jelszo, nev)
    def helyes(self, felhasznalonev,jelszo):
        if felhasznalonev in self.felhasznalok and bcrypt.check_password_hash(self.felhasznalok[felhasznalonev].jelszo, jelszo):
            return True
        return False
    
    def uzenet_db(self):
        db=0
        for uzenet in  self.felhasznalok[ self.aktualis_felhasznalo].uzenetek:
            if uzenet.olvasott==False:
                db+=1
        return db
    def hozzaad(self,cimzett,szöveg):
       
        self.felhasznalok[cimzett].uzenetek.append(Üzenet(self.id,szöveg,str(datetime.now().strftime("%Y-%m-%d %H:%M")),self.aktualis_felhasznalo,cimzett,False))


        
    def mentes(self):
    # Adatbázis kapcsolat létrehozása
        conn = sqlite3.connect('felhasznalo.db')
        c = conn.cursor()
        # c.execute("DROP TABLE IF EXISTS uzenet")
        c.execute('''CREATE TABLE IF NOT EXISTS felhasznalo
                     (felhasznalonev text PRIMARY KEY, jelszo text, nev text)''')
        c.execute('''CREATE TABLE IF NOT EXISTS uzenet
                     (id integer PRIMARY KEY, szoveg text, ido text, kuldo text, cimzett text, olvasott integer)''')
        
        for felhasznalonev, felhasznalo_adatok in self.felhasznalok.items():
            c.execute("INSERT OR REPLACE INTO  felhasznalo VALUES (?, ?, ?)",
                    (felhasznalonev, felhasznalo_adatok.jelszo, felhasznalo_adatok.nev))

            for uzenet in felhasznalo_adatok.uzenetek:
                c.execute("INSERT OR REPLACE INTO uzenet VALUES (?,?, ?, ?, ?, ?)",
                        (uzenet.id,uzenet.szoveg, uzenet.ido, uzenet.kuldo, uzenet.cimzett, int(uzenet.olvasott)))

        conn.commit()
        conn.close() 
    def betoltes(self):
        # Adatbázis kapcsolat létrehozása (ha még nem létezik az adatbázis, akkor létrehozza)
        conn = sqlite3.connect('felhasznalo.db')
        c = conn.cursor()

        # Felhasználók beolvasása
        for row in c.execute('SELECT * FROM felhasznalo'):
            felhasznalonev, jelszo, nev = row
            self.felhasznalok[felhasznalonev] = Felhasznalo(felhasznalonev, jelszo, nev)

        # Üzenetek beolvasása
        for row in c.execute('SELECT * FROM uzenet'):
            id,szoveg, ido, kuldo, cimzett, olvasott = row
            self.id=id
            uzenet = Üzenet(self.id,szoveg, ido, kuldo, cimzett, bool(olvasott))
            self.felhasznalok[cimzett].uzenetek.append(uzenet)

        # Kapcsolat bezárása
        conn.close()