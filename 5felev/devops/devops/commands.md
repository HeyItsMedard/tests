Az általad megadott parancsokat elemezve a szerveren különböző típusú tevékenységeket hajtottak végre, beleértve rendszergazdai hozzáférés beállítását, tűzfal konfigurálását, Docker telepítését, valamint SSH- és fájlkezelési műveleteket. Íme a részletes elemzés:

---

### **Rendszergazdai jogosultságok és általános parancsok**
1. `su root`: Átváltás root (rendszergazdai) felhasználóra.
2. `exit`: Kilépés az aktuális terminálból vagy root mód elhagyása.
3. `sudo yum install htop`: A **htop** rendszerfigyelő eszköz telepítése.
4. `ls -lka`: A fájlrendszer listázása bővített információkkal.
5. `cd`: Könyvtárváltás a felhasználó alapértelmezett könyvtárába.
6. `mkdir .ssh`: Létrehoz egy **.ssh** könyvtárat a felhasználó könyvtárában.
7. `touch .ssh/authorized_keys`: Létrehoz egy **authorized_keys** fájlt az SSH kulcsok tárolására.
8. `ls -la .ssh/`: A **.ssh** könyvtár tartalmának listázása részletes nézettel.
9. `chmod -R go= .ssh/`: A **.ssh** könyvtár és fájljainak jogosultságainak korlátozása, hogy csak a tulajdonos érhesse el.
10. `vim .ssh/authorized_keys` / `nano .ssh/authorized_keys`: Az **authorized_keys** fájl szerkesztése az SSH kulcsok hozzáadásához.

---

### **SSH konfiguráció**
12. `ssh medi@47.250.87.83`: Kapcsolódás SSH-n keresztül a megadott szerverhez.
49. `sudo nano /etc/ssh/sshd_config`: Az SSH daemon konfigurációs fájljának szerkesztése.
50. `sudo systemctl restart sshd.service`: Az SSH szolgáltatás újraindítása a konfigurációs módosítások alkalmazásához.

---

### **Tűzfalkezelés**
16. `yum install firewalld`: A Firewalld telepítése (nem rendszergazdaként próbálkozva).
17. `yum install firewalld -y`: Telepítés automatikus jóváhagyással.
18. `sudo yum install firewalld -y`: Firewalld telepítése rendszergazdaként.
19. `sudo systemctl status firewalld`: Firewalld státuszának lekérdezése.
20. `sudo systemctl start firewalld`: Firewalld szolgáltatás elindítása.
21. `sudo systemctl status firewalld`: Ismételt státuszlekérdezés.
22. `sudo firewall-cmd --permanent --list-all`: A tűzfal jelenlegi szabályainak listázása.
23. `sudo firewall-cmd --get-services`: Elérhető tűzfal-szolgáltatások listázása.
24. `sudo firewall-cmd --permanent --add-service=http`: HTTP-szolgáltatás engedélyezése a tűzfalon.
25. `sudo firewall-cmd --permanent --add-service=https`: HTTPS-szolgáltatás engedélyezése a tűzfalon.
26. `sudo firewall-cmd --reload`: Tűzfal újratöltése a szabályok alkalmazásához.
27. `sudo firewall-cmd --permanent --list-all`: Az aktuális tűzfal-szabályok ismételt listázása.
28. `sudo systemctl enable firewalld`: A Firewalld automatikus indításának engedélyezése a rendszer indításakor.
53. `sudo firewall-cmd --zone=public --permanent --add-port=81/tcp`: TCP port 81 engedélyezése a nyilvános zónában.
54. `sudo firewall-cmd --reload`: Tűzfal szabályainak újratöltése.
55. `sudo firewall-cmd --zone=public --list-ports`: Nyitott portok listázása a tűzfalon.

---

### **Szoftvertelepítés és frissítés**
29. `sudo yum install epel-release`: EPEL tároló hozzáadása a további csomagok telepítéséhez.
30. `sudo yum update`: A rendszer összes csomagjának frissítése.
31. `sudo yum remove epel-release`: Az EPEL tároló eltávolítása.
32. `sudo yum install htop`: **htop** újratelepítése.
33. `sudo yum update`: Újabb frissítési próbálkozás.
34. `sudo yum install htop`: **htop** ismételt telepítése.

---

### **Docker telepítése és konfiguráció**
36. `curl -fsSL https://get.docker.com/ | sh`: A Docker telepítése a hivatalos Docker script segítségével.
37. `sudo systemctl status docker`: Docker állapotának ellenőrzése.
38. `sudo systemctl start docker`: Docker szolgáltatás elindítása.
39. `sudo systemctl status docker`: Ismételt állapotlekérdezés.
40. `sudo systemctl enable docker`: Docker automatikus indításának engedélyezése a rendszer indításakor.
42. `docker ps`: Docker futó konténerek listázása (engedély nélkül próbálkozva).
43. `sudo docker ps`: Docker futó konténerek listázása rendszergazdaként.
44. `groups`: Jelenlegi felhasználó csoportjainak listázása.
45. `sudo usermod -aG docker $(whoami)`: A jelenlegi felhasználó hozzáadása a Docker csoporthoz.
46. `whoami`: Az aktuális felhasználónév lekérdezése.
47. `groups`: Csoporttagság ellenőrzése a Docker csoport hozzáadása után.

---

### **Egyéb**
35. `tmux`: Tmux session indítása (terminál multiplexer használata).
51. `tmux`: Ismételt tmux indítás.
48. `exit`: Kilépés a terminálból.

---

### **Összegzés**
A parancsok nagy részét rendszergazdai jogosultságokkal futtatták, amelyek a következőkre terjedtek ki:
- **SSH konfiguráció**: Kapcsolatok biztosítása.
- **Tűzfal szabályozása**: HTTP/HTTPS és egyedi portok megnyitása.
- **Docker telepítése**: Konténerizációs környezet kialakítása.
- **Rendszerfigyelő eszközök telepítése**: Htop.
- **Szoftverfrissítések és új csomagok kezelése**: YUM és EPEL.

Ez a sorozat jól mutatja a szerver előkészítését különféle szolgáltatások futtatására és biztosítására.