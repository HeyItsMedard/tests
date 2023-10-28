

import os
from flask import Flask,request,url_for,redirect,render_template
from app import App
app= Flask(__name__)

APP=App()
if os.path.exists("felhasznalo.db"):
    APP.betoltes()
   


@app.route('/regisztracio',methods=["GET","POST"])
def regisztracio():
    uzenet=""
    if request.method == 'POST':
        felhasznalonev = request.form.get('felhasznalonev')
        jelszo = request.form.get('jelszo')
        
        hashed = APP.jelszo_atalakitas(jelszo)
        nev = request.form.get('nev') 
        if  not felhasznalonev.strip() or not jelszo.strip() or not nev.strip():
            # print("hiba")
            uzenet="Minden mezőt tölts ki"
        elif felhasznalonev in  APP.felhasznalok:
            uzenet = "Ez a felhasználónév már Foglalt"
        else:
            uzenet="Sikeres Regisztrácio"
            APP.felhasznalo_mentes(felhasznalonev, hashed, nev)
            # print(f"{felhasznalonev},{jelszo},{nev}")
    return  render_template("regisztracio.html", Uzenet=uzenet)
    

@app.route('/bejelentkezes',methods=["GET","POST"])
def bejelentkezes():
    uzenet=""
    if request.method == 'POST':
        felhasznalonev = request.form.get('felhasznalonev')
        jelszo = request.form.get('jelszo')
        helyes= APP.helyes(felhasznalonev,jelszo)
        if helyes :
            APP.aktualis_felhasznalo=felhasznalonev
            # print(f"sikeres belepes {APP.aktualis_felhasznalo}")
            return redirect(url_for("felhasznalo_menu"))
        else:
            uzenet="Hibás felhasználónév vagy jelszó"
    return  render_template("bejelentkezes.html",Uzenet=uzenet)
  

@app.route('/',methods=["GET","POST"])
def fo_oldal():
    APP.mentes()
    return  render_template("fooldal.html")


@app.route('/uj_uzenet',methods=["GET","POST"])
def uzenet_iras():
    uzenet=""
    if request.method == 'POST':
        cimzett= request.form.get('cimzett')
        uzenet_szoveg = request.form.get('szoveg')
        if cimzett==  APP.aktualis_felhasznalo or cimzett not in  APP.felhasznalok:
            uzenet="Hibás a cimzett"
            # print("hiba")
        else:
            uzenet="Elküldve"
            # print("elküldve")
            APP.id+=1
            APP.hozzaad(cimzett,uzenet_szoveg)
    return  render_template("uj_uzenet.html",Uzenet=uzenet)
    


@app.route('/uzenet_kiirasa',methods=["GET","POST"])
def uzenet_kiirasa():
    uzenetek=[]
    print( APP.felhasznalok[ APP.aktualis_felhasznalo].uzenetek)
    if len( APP.felhasznalok[ APP.aktualis_felhasznalo].uzenetek)==0:
        uzenetek.append("Nincs üzeneted")
    for uzenet in  APP.felhasznalok[ APP.aktualis_felhasznalo].uzenetek:
        if uzenet.olvasott==False:
            uzenet.olvasott=True
            uzenetek.append(f"{uzenet} (új)")
           
        else:
            uzenetek.append(uzenet)
        
    return  render_template("uzenetek_lista.html",Uzenetek=uzenetek)
        
    


@app.route('/felhasznalo_menu',methods=["GET","POST"])
def felhasznalo_menu():
    db=APP.uzenet_db()
    return  render_template("felhasznalo_menu.html",db=db)



if __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0',debug=True)
   