# Port részletekben

A Docker portleképezésének alapját az **`-p`** kapcsolóval megadott **`<host_port>:<container_port>`** formátum képezi, ahol két portot kapcsolunk össze:

- **Host port (bal oldal, `8080`)**: A gazdagép (azaz a fizikai vagy virtuális gép) portja, amelyen a szolgáltatás elérhetővé válik a külvilág számára.
- **Container port (jobb oldal, `80`)**: A konténeren belüli alkalmazás által használt port, amelyen az alkalmazás figyeli a bejövő forgalmat.

Ez a portleképezés lehetővé teszi, hogy a konténeren belüli alkalmazás szolgáltatásait elérjük a gazdagépen keresztül.

---

## **Hogyan működik?**

Amikor egy portleképezést adsz meg, például `-p 8080:80`, akkor a következők történnek:

1. **A konténer belsejében futó alkalmazás**:
   - Például egy Nginx vagy Vite alkalmazás a konténeren belül a 80-as porton hallgat.

2. **A Docker portleképezés**:
   - A Docker a gazdagép 8080-as portját összeköti a konténer 80-as portjával.

3. **A gazdagép külső forgalma**:
   - Ha valaki a böngészőjében beírja a `http://localhost:8080` címet, a kérés először a gazdagép 8080-as portjára érkezik.
   - A Docker automatikusan továbbítja a kérést a konténer 80-as portjára, ahol az alkalmazás válaszol.

4. **Az alkalmazás válasza**:
   - Az alkalmazás (például egy Nginx webkiszolgáló) válaszol a konténer 80-as portján keresztül.
   - A válasz visszakerül a gazdagép 8080-as portjára, majd a kliens böngészőjébe.

---

## **Gyakorlati példa: Nginx használata**

### Portleképezés parancs:
```bash
docker run -d -p 8080:80 nginx
```
Ahol nginx az image, nem a container. --name-mel containert is beállíthatunk (fennebb volt erre már példa)

1. **Konténer belső portja (80)**:
   - Az Nginx webkiszolgáló alapértelmezés szerint a konténer 80-as portján hallgat.

2. **Host portja (8080)**:
   - A gazdagép 8080-as portján fogadja a kéréseket, amelyeket továbbít a konténer 80-as portjára.

3. **Elérés a gazdagépen**:
   - Nyisd meg a böngészőt, és írd be a `http://localhost:8080` címet.
   - Az Nginx kezdőoldala jelenik meg, mert a 8080-as port leképezett a konténer 80-as portjára.

---

## **Fontos megjegyzések**

1. **Portok konfliktusa a gazdagépen**:
   - Ha egy másik alkalmazás már foglalja a gazdagép 8080-as portját, akkor hibaüzenetet kapsz.
   - Ilyenkor másik szabad portot kell választani, például: `-p 9090:80`.

2. **Belső port fix, külső port rugalmas**:
   - A konténeren belüli port (például 80) az alkalmazás konfigurációjától függ.
   - A gazdagép portját szabadon választhatod, például 3000, 5000 stb.

3. **Portleképezés hiánya**:
   - Ha nem adsz meg portleképezést, például így: `docker run -d nginx`, akkor az Nginx továbbra is figyelni fog a konténer 80-as portján, de a gazdagép felől nem lesz elérhető. Csak más konténerek érhetik el a belső Docker hálózaton keresztül.

---

## **Összegzés**

A `8080:80` portleképezés azt jelenti:
- A gazdagép 8080-as portján keresztül küldött forgalmat továbbítja a konténer 80-as portjára.
- Ez lehetővé teszi, hogy a konténerben futó alkalmazás elérhető legyen a gazdagépről vagy akár a hálózaton kívüli eszközökről is, ha a gazdagép megfelelő hálózati hozzáféréssel rendelkezik.

Kérdés: **Miért jó az, hogy 8080-on fogadjon a gazdagép forgalmat és nem közvetlen már a konténer portjára menjen adat?**

A portleképezés számos előnnyel jár, amelyek a **rugalmasság**, **biztonság**, és **szolgáltatások izolálása** köré épülnek. Nézzük meg részletesen, miért hasznos a gazdagép portján keresztül fogadni a forgalmat ahelyett, hogy közvetlenül a konténer belső portját tennénk elérhetővé:

---

### **1. Biztonság és hozzáférés kontrollálása**
- **Konténerek nem közvetlenül érhetők el** a gazdagép külső hálózatáról. Ez csökkenti a támadási felületet.
- A gazdagépen csak azokat a portokat kell megnyitnod, amelyek valóban szükségesek a külső hozzáféréshez.
  - Példa: Egy alkalmazás belső adminisztrációs felületét futtathatod egy másik porton, amelyet a külvilág nem érhet el.

### **2. Több konténer kezelése egy gazdagépen**
- Ha több konténert futtatsz, **ugyanazokat a belső portokat használhatják**:
  - Példa: Két különböző Nginx konténer is figyelhet a belső 80-as porton.
  - Ezt gazdagépi portleképezéssel különítheted el:
    ```bash
    docker run -d -p 8080:80 nginx # Az első konténer a gazdagép 8080-as portját használja
    docker run -d -p 8081:80 nginx # A második konténer a gazdagép 8081-es portját használja
    ```
- Így ugyanazon a gazdagépen több szolgáltatást is futtathatsz, amelyek egymástól teljesen függetlenek.
- Ez nem egy biztonságos gyakorlati példa (helyette érdemes proxy-t, load balancert, vagy Docker saját hálózatait használni).

### **3. Portok testreszabása és kompatibilitás**
- Lehet, hogy egy konténer belső portja (pl. 80) már foglalt a gazdagépen. Ekkor kiválaszthatsz egy másik szabad portot, például 8080-at vagy 5000-et.
- Az alkalmazások használata rugalmasabbá válik, mert nem kell aggódni, hogy ütközés lesz a gazdagépen futó többi szolgáltatással.

### **4. Lokális fejlesztés egyszerűbbé tétele**
- Fejlesztői környezetben gyakran előfordul, hogy több szolgáltatás ugyanazon a gépen fut. Például:
  - Egy API a 3000-es porton,
  - Egy frontend alkalmazás a 8080-as porton.
- A portleképezés lehetővé teszi, hogy a fejlesztési és tesztelési folyamat jól elkülönüljön.

### **5. Hálózatok izolálása**
- A Docker hálózatkezelése lehetővé teszi, hogy csak az a konténer legyen elérhető a külvilágból, amelyhez portleképezést állítottál be.
  - Példa: Egy adatbázis-konténer (`MySQL`) tipikusan nem kap külső portleképezést, mert azt csak más konténerek használják egy belső hálózaton keresztül.

### **6. Proxyk és load balancerek integrációja**
- Portleképezés használatával könnyebben kezelheted a konténerek elérhetőségét proxyk és load balancerek mögött.
  - Példa: Egy Nginx proxy leképezheti a gazdagép 80-as portját különböző konténerek portjaira.

### **7. Alacsony szintű hálózati problémák kezelése**
- A gazdagép portjain keresztül haladó forgalmat könnyebb monitorozni és hibakeresni szabványos hálózati eszközökkel.
  - Például használhatsz eszközöket, mint a **Wireshark** vagy a **netstat**, hogy ellenőrizd a gazdagép portjain folyó forgalmat.

---

### **Mi történne, ha közvetlenül a konténer portját használnád?**
1. **Korlátozott hozzáférés a külvilágból**:
   - A konténer alapértelmezés szerint csak a Docker belső hálózatában érhető el.
   - Ha közvetlen elérést szeretnél, minden egyes konténert manuálisan kellene elérhetővé tenni a gazdagép hálózatán kívülről.

2. **Konténerek ütközése**:
   - Ha több konténer használja ugyanazt a belső portot (például 80-at), akkor közvetlen elérés esetén ezek között konfliktus lépne fel.

3. **Rugalmasság hiánya**:
   - Nem tudnád szabadon megválasztani, hogy a gazdagép melyik portján érhetők el a különböző szolgáltatások.

---

### **Összegzés**
A portleképezés a gazdagép és a konténerek közötti kommunikáció **rugalmas, biztonságos és testreszabható** módját biztosítja. Ez lehetővé teszi:
- Több konténer egyszerű futtatását egy gépen,
- Portok konfliktusainak elkerülését,
- A szolgáltatások elérhetőségének pontos kontrollálását.

Ezért a gazdagép portjának használata gyakorlatilag egy interfész a konténerben futó alkalmazások és a külvilág között.