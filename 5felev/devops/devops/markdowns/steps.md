A megadott parancsok egy logikus sorrendben mutatják be, hogyan készült elő a szerver egy működőképes és biztonságos környezet megteremtésére, miközben alapvető eszközöket telepítettek és beállítottak. Az alábbiakban részletezem a parancsok sorrendjét és a mögöttük húzódó logikát:

---

### **1. Kezdeti rendszergazdai hozzáférés és alapbeállítások**
- **1. `su root`**: A rendszergazdai jogosultság megszerzése. Ez az első lépés, mert sok művelethez adminisztrátori jogosultság kell.
- **2. `exit`**: Visszalépés normál felhasználói módba. Valószínűleg csak tesztelték a hozzáférést.

---

### **2. Alap szoftvertelepítés és rendszerfigyelés**
- **3. `sudo yum install htop`**: Az **htop** rendszerfigyelő eszköz telepítése, hogy könnyebben nyomon követhessék a szerver erőforrásait.
- **4. `ls -lka`**: A fájlrendszer ellenőrzése.
- **5-9. Könyvtár és jogosultság beállítása az SSH számára**:  
   - **6. `mkdir .ssh`**: Az SSH kulcsok tárolásához szükséges könyvtár létrehozása.  
   - **7-9**: Az SSH-kulcsok kezeléséhez szükséges fájlok létrehozása és biztonsági beállítások (pl. csak a tulajdonos férhet hozzá).

---

### **3. SSH hozzáférés konfigurálása**
- **10-11**: Az SSH-kulcsokat a **vim** vagy **nano** használatával hozzáadták az **authorized_keys** fájlhoz.
- **12. `ssh medi@47.250.87.83`**: SSH kapcsolódás tesztelése a megadott szerverhez.
- **49-50**: Az **/etc/ssh/sshd_config** fájl módosítása az SSH további konfigurációjához (pl. portok, protokollok, vagy biztonsági beállítások finomhangolása).

---

### **4. Tűzfal beállítása**
- **16-21**: A **firewalld** telepítése és indítása:
  - Az első próbálkozás során root jog nélkül futtatták, ezért sikertelen lehetett (parancs ismétlése sudo-val).
  - Státuszellenőrzések biztosítják, hogy a szolgáltatás fut-e.
- **22-28**: A tűzfal konfigurációja:
  - A HTTP/HTTPS szolgáltatások, valamint egyedi portok (pl. 81) engedélyezése történt.
  - A szabályok tartós érvényesítése a **--permanent** kapcsolóval.
  - Az új szabályok alkalmazása a tűzfal újratöltésével (**reload**).
- **53-55**: Egy adott port (81/tcp) megnyitása és az aktív portok ellenőrzése.

---

### **5. Szoftverfrissítések és csomagkezelés**
- **29-34**: Az EPEL tároló hozzáadása és a rendszer frissítése:
  - EPEL (Extra Packages for Enterprise Linux) tároló telepítése olyan csomagokhoz, amelyek alapértelmezés szerint nem érhetők el.
  - A rendszer és az egyes szoftverek (pl. htop) frissítése.
  - Az EPEL eltávolítása, ha már nem szükséges.

---

### **6. Docker telepítése és beállítása**
- **36-40**: A Docker telepítése és konfigurációja:
  - A Docker telepítése a hivatalos script segítségével történt.
  - A szolgáltatás indítása és automatikus indításának engedélyezése a rendszerindításkor.
- **42-47**: A Docker-csoport kezelése:
  - A felhasználót hozzáadták a Docker csoporthoz, hogy rendszergazdai jogosultságok nélkül is futtathasson konténereket.

---

### **7. Egyéb tevékenységek**
- **35, 51. `tmux`**: A Tmux (terminál multiplexer) indítása, amely lehetővé teszi több terminál szekció futtatását és kezelhetőségét.
- **48. `exit`**: Terminálból való kilépés.

---

### **Logikai sorrend és folyamat**
1. **Kezdeti hozzáférés ellenőrzése**: Rendszergazdai jogok, SSH alapok létrehozása.
2. **Alap szoftverek telepítése és ellenőrzése**: A rendszerfigyeléshez és csomagkezeléshez szükséges eszközök telepítése.
3. **Biztonságos távoli elérés kialakítása**: SSH beállítás és kulcskezelés.
4. **Hálózati és biztonsági szabályok konfigurálása**: Tűzfal beállítása.
5. **Fejlett eszközök és konténerizáció telepítése**: Docker, Tmux.
6. **Tesztelések és végső ellenőrzések**: A konfigurált szolgáltatások állapotának ellenőrzése.

Ez a sorrend a szerver alapvető konfigurációjától a biztonsági szabályok és fejlett eszközök telepítéséig ível.