# DEVOPS

## Dockerfile és Build folyamat:

28. **Mi a `RUN` parancs szerepe egy Dockerfile-ban?**  
   - A `RUN` parancs lehetővé teszi, hogy parancsokat futtassunk a konténer létrehozásának során, például szoftverek telepítése, fájlok módosítása stb. Minden `RUN` lépés új réteget hoz létre az image-ban.

29. **Hogyan lehet a `npm` parancsot futtatni egy build során, majd a szükséges fájlokat bemásolni az Nginx könyvtárba?**  
   - A Dockerfile-ban a következő lépéseket tehetjük:
     ```Dockerfile
     # Build fázis
     FROM node:alpine AS builder
     WORKDIR /app
     COPY package*.json ./
     RUN npm install
     COPY . .
     RUN npm run build

     # Nginx fázis
     FROM nginx:alpine
     COPY --from=builder /app/dist /usr/share/nginx/html
     ```

30. **Miért nem elegendő egy alap Nginx Docker image a specifikus igények kielégítésére?**  
   - Az alap Nginx image csak az Nginx szerver alapvető funkcionalitását biztosítja. A személyre szabott konfigurációk, mint például a virtuális hosztok, SSL beállítások és más speciális igények nem érhetők el alapértelmezés szerint, ezeket külön kell konfigurálni.

31. **Mi a `COPY` parancs szerepe egy Dockerfile-ban?**  
   - A `COPY` parancs fájlokat vagy könyvtárakat másol a hostról a konténer fájlrendszerébe, ami lehetővé teszi a helyi forráskód vagy erőforrások integrálását az image-be.

32. **Hogyan lehet környezeti változókat definiálni egy Dockerfile-ban?**  
   - Környezeti változók definiálhatók az `ENV` paranccsal. Például:
     ```Dockerfile
     ENV NODE_ENV=production
     ```

33. **Milyen előnyökkel jár a multi-stage build használata Dockerfile-ban?**  
   - A multi-stage build lehetővé teszi, hogy több fázisban építkezzünk, így csökkentve a végső image méretét, mivel csak a szükséges fájlok kerülnek be a végső image-be, és elkerülhetjük a nem szükséges build eszközök beépítését. 

34. **Hogyan lehet megakadályozni, hogy a Docker cache-t használja a build során?**  
   - A `--no-cache` flag használatával lehet megakadályozni, hogy a Docker cache-t használjon a build során:
     ```bash
     docker build --no-cache -t my-image .
     ``` 

## Docker és konténerizáció alapjai:

1. **Mi a különbség egy Docker image és egy container között?**  
   - Az **image** egy statikus sablon, amely tartalmazza az alkalmazás futtatásához szükséges fájlokat és beállításokat. (az operációs rendszert, a szükséges könyvtárakat, függőségeket, valamint az alkalmazás kódját és konfigurációit tartalmazhatják)  
   - A **container** az image futó példánya, amely elkülönített környezetben végzi az alkalmazás működését. Egyetlen egységbe csomagolt környezet.

2. **Hogyan használhatóak a Docker volumes az adatok tárolására?**  
   - A Docker volumes segítségével tartósan tárolhatunk adatokat a konténerek számára, akár az alábbi módokon:  
     - **Bind mount**: Meghatározott helyi fájlrendszer felcsatolása.  
     - **Named volume**: Egy elkülönített tárolóhely, amelyet Docker kezel.  

3. **Mit jelent a `docker run` parancs különböző kapcsolókkal, például `-d` vagy `--rm`?**  
   - **`-d`**: A konténer **detached** módban (háttérben) fut.  
   - **`--rm`**: A konténer automatikusan törlődik a leállítása után.  

4. **Hogyan törölhető egy Docker container és image a terminál segítségével?**  
   - **Container törlése**:  
     ```
     docker stop <container_name>
     docker rm <container_name>
     ```  
   - **Image törlése**:  
     ```
     docker rmi <image_name>
     ```

5. **Mit kell tenni, ha egy image nem törölhető, mert egy container éppen fut rajta?**  
   - Először le kell állítani és törölni a futó containert:  
     ```
     docker stop <container_name>
     docker rm <container_name>
     ```  
   - Ezután törölhető lesz az image. 

1. **Mit jelent a volume csatolása egy konténerhez, és miért van szükség rá?**  
   - A volume csatolása lehetővé teszi az adatok tartós tárolását a konténer újraindítása vagy törlése esetén is. Ez fontos, hogy megőrizzük az adatokat, például egy adatbázis esetén.
   - [Ez így történik meg a valóságban](#volume-csatolása).

2. **Hogyan lehet bind mount és volume között választani a fájlok tárolásakor?**  
   - **Bind mount**: A helyi fájlrendszer egy mellékhelyiséget csatolunk, közvetlenül a host fájlairól.   (magyarul: abszolút path)
   - **Volume**: Docker által kezelt, izolált tárolóhely, amely független a host fájlrendszerétől, ideális adatfelhasználásra és megosztásra. (magyarul: automatikus)

3. **Mit csinál a következő parancs: `docker-compose up`, ha egy konfigurációs fájl köt meg szolgáltatásokat?**  
   - A `docker-compose up` parancs létrehozza és elindítja a szolgáltatásokat a megadott konfigurációs fájl alapján,azaz a konténereket hálózati kapcsolatokkal és volume-okkal kezeli.

4. **Hogyan készíthető egy statikus weboldal Docker segítségével, Nginx-et hasznosítva?**  
   - Hozzon létre egy Dockerfile-t, ami Nginx-et telepít, és másolja a statikus fájlokat az Nginx html könyvtárába. Használja a `docker build` és `docker run` parancsokat a konténer létrehozásához és futtatásához. [Mindezt gyakorlatban itt találhatjátok](#statikus-weboldal-készítése-dockerrel-és-nginx-el).

5. **Hogyan biztosítható, hogy a fájlok elérhetők legyenek egy konténer számára helyi könyvtárból?**  
   - A helyi könyvtárat volume-ként vagy bind mount-ként felcsatlakoztathatjuk a konténerhez a `-v` vagy `--mount` flag segítségével a `docker run` parancsban.

6. **Mi történik, ha az index.html helyett egy másik fájl kerül felcsatolásra az Nginx konténerben?**  
   - Az Nginx az új fájlt fogja kiszolgálni a webes kérésekre, ami valószínűleg hibát vagy nem várt viselkedést okoz, ha a fájl nem érvényes HTML vagy más típusú tartalmat tartalmaz.

7. **Hogyan működik a `depends_on` kulcs a docker-compose fájlban?**  
   - A `depends_on` kulcs határozza meg a szolgáltatások indítási sorrendjét. Például ha a service A függ a service B-től, a Docker Compose először elindítja B-t, majd A-t. Azonban ez nem garantálja, hogy B készen is áll a kérések fogadására. 

- **+1.: Mi az a Docker Network, mit csinál?**
    - A Docker Network lehetővé teszi a konténerek közötti kommunikációt. Különböző hálózati drivereket használhatunk, mint például a bridge, host, és overlay, hogy meghatározzuk, hogyan kapcsolódnak egymáshoz a konténerek és a host rendszer.

    - bridge: Ez az alapértelmezett hálózati mód, amelyet a Docker használ, amikor egy konténert indít. A bridge hálózat egy virtuális hálózatot hoz létre a Docker host gépen belül, amely lehetővé teszi a konténerek közötti kommunikációt ugyanazon a host gépen. A bridge hálózat izolálja a konténereket a host gép hálózatától.

    - host: Ebben a módban a konténer közvetlenül a host gép hálózatát használja. Ez azt jelenti, hogy a konténer ugyanazokat az IP-címeket és portokat használja, mint a host gép. Ez a mód hasznos lehet, ha a konténernek közvetlen hozzáférésre van szüksége a host gép hálózatához, de csökkenti a konténerek izolációját.

    - overlay: Az overlay hálózat lehetővé teszi a konténerek közötti kommunikációt több Docker host gépen keresztül. Ez a mód különösen hasznos, ha több gépből álló Docker Swarm klasztert használunk. Az overlay hálózat egy virtuális hálózatot hoz létre, amely összekapcsolja a különböző host gépeken futó konténereket.

## Nginx és webes alkalmazások konténerizálása:

6. **Hogyan érhető el egy webkonténerből hostolt alkalmazás localhoston keresztül?**  
   - A konténert a host géphez kell kötni a `-p <host_port>:<container_port>` flaggel, például:  
     ```
     docker run -p 80:80 <image_name>
     ```
   - Ezután elérhető lesz a weboldal a `http://localhost` címen.

7. **Mit jelent a `-p 80:80` flag a `docker run` parancsnál?**  
   - A host gép **80-as portját** összeköti a konténer **80-as portjával**, így a kívülről érkező kérések eljutnak a konténerben futó alkalmazáshoz.

8. **Hogyan konfigurálható Nginx egyéni konfigurációs fájlokkal (pl. `default.conf`)?**  
   - A konfigurációs fájlt volume-ként fel lehet csatolni a konténerhez:
     ```
     docker run -v $(pwd)/default.conf:/etc/nginx/conf.d/default.conf nginx
     ```
   - Ez biztosítja, hogy a saját konfigurációt használja az Nginx.
   - +1.: **Mi az a volume?**
        - lehetővé teszi az adatok tartós tárolását és megosztását a konténerek között. A volume-ok segítségével a konténerek újraindítása vagy törlése esetén is megőrizhetők az adatok.

        - Például, ha egy adatbázis-konténerben tárolt adatokat szeretnél megőrizni, akkor egy volume-t csatolhatsz a konténerhez, amely a host gépen található fájlrendszert használja az adatok tárolására.   

9. **Hogyan kezelhetünk különböző portokat, ha több weboldalt szeretnénk kiszolgálni egy Nginx proxyval?**  
   - Az Nginx virtuális hostokra alapozva dolgozik. Különböző domain nevekhez és portokhoz külön konfigurációs fájlokat hozhatunk létre, például:  
     ```
     server {
       listen 81; # Első weboldal
       server_name site1.local;
       ...
     }
     server {
       listen 82; # Második weboldal
       server_name site2.local;
       ...
     }
     ```

10. **Mi az environment variable és hogyan adható meg például egy MySQL adatbázis jelszava?**  
   - Az **environment variable (környezeti változó)** a konfigurációs adatok tárolására használatos.  
     MySQL adatbázis jelszava megadható a `-e` flag segítségével:
     ```
     docker run -e MYSQL_ROOT_PASSWORD=my-secret-password mysql
     ``` 
     Megjegyzés: én .env-ben szoktam megadni ezeket, de ki ahol akarja

## IP, domain és DNS:
11. **Mi a különbség IP, domain, és subdomain között?**  
   - **IP**: Számokból álló cím, amely egy eszköz azonosítására szolgál a hálózaton.  
   - **Domain**: Ember számára érthető név, amely egy IP-címhez van társítva (pl. `example.com`).  
   - **Subdomain**: A domain része, amely általában egy aloldalra vagy külön szolgáltatásra utal (pl. `blog.example.com`).

12. **Hogyan működik a DNS cache és hogyan gyorsítja fel az elérést?**  
   - A DNS cache a korábban lekérdezett domain-IP párosokat tárolja helyileg. Ezáltal nem kell újra DNS-szervereken keresztül feloldani a címet, így gyorsabb az elérés.

13. **Hogyan konfigurálható egy domain Let's Encrypt tanúsítvány segítségével?**  
   - Használhatunk egy kliensprogramot (pl. Certbot), amely automatikusan generál és telepít tanúsítványt:
     ```
     sudo certbot --nginx -d example.com
     ```
   - Ezután az Nginx automatikusan HTTPS-t biztosít a domainhez.  
   - Mi az órán Nginx Proxy Managerben kértük le domainjeinkhez.  

14. **Miért fontos a Cloudflare DNS használata az anti-DDoS védelem érdekében?**  
   - A Cloudflare elosztott hálózatot és globális gyorsítótárat használ, valamint szűri a gyanús forgalmat. Ez csökkenti a DDoS támadások hatását és javítja az elérhetőséget.

15. **Mikor hasznosak a CNAME rekordok egy DNS rendszerben?**  
   - A CNAME rekordok akkor hasznosak, ha egy domain más domain névre mutat. Például egy subdomain (`www.example.com`) átirányítása az alap domainre (`example.com`). Ez csökkenti a karbantartás nehézségeit, ha az IP-cím változik. 

## Docker Swarm és Kubernetes:
16. **Mi a különbség a Docker Swarm és Kubernetes között?**  
   - **Docker Swarm**: Egyszerűbb, kevésbé komplex konténer-orchesztrációs eszköz, közvetlenül Dockerre épül.  
   - **Kubernetes**: Robusztusabb, több funkcióval rendelkező eszköz a skálázáshoz, automatikus helyreállításhoz és komplex munkafolyamatokhoz.

17. **Hogyan történik a szolgáltatások skálázása és monitorozása Kubernetes-ben?**  
   - **Skálázás**: A `kubectl scale` parancs segítségével állíthatjuk be a podok számát, vagy használhatunk automatikus skálázót (HPA - Horizontal Pod Autoscaler).  
   - **Monitorozás**: Beépített Kubernetes eszközök (pl. Metrics Server), illetve külső monitorozási eszközök, mint a Prometheus vagy Grafana.

18. **Mi az a "pod" Kubernetes-ben, és hogyan használható volumenekkel?**  
   - A pod a Kubernetes legkisebb egysége, amely egy vagy több konténert tartalmaz.  
   - Volumeneket a podhoz rendelhetünk adat persistálására:
     ```yaml
     volumes:
       - name: data-volume
         hostPath:
           path: /data
     ```

19. **Hogyan terheli szét egy Swarm Manager a feladatok végrehajtását több worker node között?**  
   - A Swarm manager automatikusan elosztja a feladatokat (tasks) a worker node-ok között a rendelkezésre álló erőforrások, prioritások és beállított replikációs szabályok alapján. 

## Portainer és Proxy Manager 
20. **Hogyan tárolható privát repository a Portainer stacken belül?**  
   - Privát repository-kat Github Token használatával lehet megadni.

21. **Milyen előnyei vannak a statikus weboldalak tárhely használatának?**  
   - Gyorsabb betöltési sebesség, egyszerűbb karbantartás és alacsonyabb erőforrás-felhasználás, mivel nincs dinamikus tartalomgenerálás.

22. **Mit jelent az, hogy autentikáció "access tokennel" történik?**  
   - Az **access token** egy titkosított azonosító, amelyet a felhasználók azonosítására használnak, biztosítva a jogosultságokat egy alkalmazáson belül.

23. **Hogyan kezelhetők a különböző szintű hozzáférések egy konténerizált környezetben?**  
   - Hozzáférések kezelhetők RBAC (Role-Based Access Control) segítségével, amely lehetővé teszi, hogy különböző felhasználók és csoportok eltérő jogosultságokkal rendelkezzenek a konténerek és erőforrások felett. 

## Folyamatadminisztráció és hibakezelés:
24. **Miért szükséges figyelni a futó konténerek erőforrás-használatát?**  
   - Az erőforrás-használat figyelése segít elkerülni a teljesítménybeli problémákat, biztosítja a stabil működést és optimalizálja az erőforrás-felhasználást, így költségeket is csökkenthet.

25. **Hogyan deríthetjük ki, ha egy adatbázis container erőforrás-problémái miatt áll le?**  
   - Ellenőrzés a konténer logjaiban (`docker logs <container_name>`), valamint a futó konténer erőforrás-használatának nyomon követése (`docker stats`). Ha a CPU vagy memória használat rendszeresen maxon pörög, akkor problémák lehetnek.

26. **Mikor kell Proxy managert használni egy infrastruktúra optimalizálásához?**  
   - Proxy managert akkor érdemes használni, ha több szolgáltatást szeretnénk egy domain alatt futtatni, illetve a forgalmat szét kívánjuk osztani, vagy HTTPS tanúsítványokat szeretnénk egyszerűen kezelni.

27. **Hogyan lehet egyszerű adblock-megoldásokkal minimalizálni a felesleges hálózati terhelést egy projektben?**  
   - Használhatunk tartalomblokkoló proxykat (pl. Pi-hole) vagy beállíthatunk a böngészőkben adblockert, hogy kiszűrjük a nem kívánt hirdetéseket és egyéb forgalmat, csökkentve ezzel a hálózati terhelést. 

## Docker Swarm és Kubernetes:

16. **Mi a különbség a Docker Swarm és Kubernetes között?**  
   - **Docker Swarm**: Egyszerűbb, könnyen használható, a Docker natív orchestration eszköze.  
   - **Kubernetes**: Komplexebb, sokkal robusztusabb, szélesebb körű funkcionalitást kínál, például automatikus skálázást és helyreállítást.

17. **Hogyan történik a szolgáltatások skálázása és monitorozása Kubernetes-ben?**  
   - **Skálázás**: A `kubectl scale` parancs, vagy automatikus horizontális skálázás (HPA) használatával végezhető.  
   - **Monitorozás**: Eszközök, mint a Prometheus és Grafana segítségével, amelyek metrikákat gyűjtenek a podokról és szolgáltatásokról.

18. **Mi az a "pod" Kubernetes-ben, és hogyan használható volumenekkel?**  
   - A pod a Kubernetes legkisebb végrehajtható egysége, amely egy vagy több konténert tartalmaz.  
   - Volumenek használatával adatok tárolhatók, például a pod definiálásakor:
     ```yaml
     volumes:
       - name: data-volume
         emptyDir: {}
     ```

19. **Hogyan terheli szét egy Swarm Manager a feladatok végrehajtását több worker node között?**  
   - A Swarm Manager figyeli a rendszer állapotát és a feladatokat a worker node-ok között osztja el az erőforrások és a szolgáltatások szükségletei alapján.

+1. **Nem indul el az oldal, miért?**  

SERVERHEZ HISTORY:
ssh medi@IP
history | less 
-> | multiple command (ennek a programnak a kimenetét | ennek a programnak a bemenete), görgethető
vagy more
tail -n 2 utolsó két sorrendjét
grep "ls" csak az ls-es listázásokat teszik ki
python main.py > print.log & cat print.log -> háttérben futó process
pkill 574073 process
python main.py > print.log && cat print.log
helyes print (vagy && helyett ;)
>> appendelelés (python main.py >> print.log && cat print.log)
hullámpötty (.~) - ssh kapcsolat megszakítása (pl ha elmenne a net és kilépnél ssh terminálból)
curl http... | sh 

# SOFTTEST

## CI/CD és állománykezelés:
- +1.: Mi az a CI/CD? 
    - CI/CD a folyamatos integráció (Continuous Integration) és folyamatos szállítás (Continuous Delivery) vagy folyamatos telepítés (Continuous Deployment) rövidítése. Ezek a DevOps gyakorlatok célja, hogy automatizálják és javítsák a szoftverfejlesztési folyamatokat.

    - Folyamatos integráció (CI): Ez a gyakorlat azt jelenti, hogy a fejlesztők gyakran, akár naponta többször is integrálják kódváltoztatásaikat a közös kódbázisba. Minden integráció után automatikus build és tesztelési folyamatok futnak, hogy biztosítsák a kód minőségét és a hibák korai felismerését.

    - Folyamatos szállítás (CD): Ez a gyakorlat azt jelenti, hogy a kódváltoztatások automatikusan kerülnek egy olyan állapotba, ahol készen állnak a kiadásra. Ez magában foglalja az automatikus tesztelést, buildelést és a release folyamatokat, de a tényleges telepítést manuálisan végzik.

    - Folyamatos telepítés (CD): Ez a gyakorlat egy lépéssel tovább megy a folyamatos szállításnál, és azt jelenti, hogy a kódváltoztatások automatikusan telepítésre kerülnek a termelési környezetbe, amint átmennek az összes teszten és ellenőrzésen.

    - A CI/CD célja, hogy gyorsabbá és megbízhatóbbá tegye a szoftverfejlesztési és kiadási folyamatokat, csökkentve a hibák számát és növelve a fejlesztési ciklusok hatékonyságát.  

17. **Mi a különbség a Continous Integration (CI) és a Continous Deployment (CD) folyamatai között?**  
   - **Continuous Integration (CI)**: A fejlesztők folyamatosan integrálják a kódot egy központi repository-ba, amit automatikus tesztelések követnek.  
   - **Continuous Deployment (CD)**: A CI folyamat kiterjesztése, ahol a kód automatikusan telepítésre kerül az éles környezetbe, miután a tesztek sikeresen lefutottak.

18. **Hogyan változik a tesztelés egy dev, test, beta és éles környezet között?**  
   - **Dev**: A kód működésének ellenőrzése, gyakran manuálisan.  
   - **Test**: Automatizált tesztelés (unit, integration), a funkciók megerősítése.  
   - **Beta**: Valós felhasználók által végzett tesztelés, hibák és visszajelzések gyűjtése.  
   - **Éles**: A végső, felhasználók számára elérhető verzió működésének figyelése.

19. **Mi történik, ha egy teszt során hibás kód kerül a repository-ba (pl. nincs CI/CD lánc)?**  
   - A hibás kód tovább súlyosbíthatja a problémákat, mivel nem levonhatóan tesztelték. Ez gyakori hibákat, funkcióvesztést és potenciális szolgáltatásleállásokat okozhat az éles környezetben.

20. **Hogyan oldható meg, hogy egy közvetlen példánnyal GUI teszteket futtassunk?**  
   - Használhatunk tesztautomatizáló eszközöket (pl. Selenium, Cypress), amelyek képesek közvetlenül a GUI-t tesztelni, illetve virtuális asztali környezetet (pl. VNC, Xvfb) hozhatunk létre a GUI-integrációs teszteléshez.

21. **Mi a különbség a white-box, black-box és gray-box tesztelés között?**  
   - **White-box tesztelés**: A tesztelő ismeri a kód belső működését, és a logikát, valamint az implementációt használja a tesztelés során.  
   - **Black-box tesztelés**: A tesztelő nem ismeri a kód belső működését, kizárólag a bemeneti és kimeneti funkciókat vizsgálja.  
   - **Gray-box tesztelés**: A tesztelő részben ismeri a belső működést, kombinálva a black-box és white-box megközelítést, hogy a tesztelés hatékonyabb legyen. 

## Tesztelési folyamatok és típusok (TDD):
8. **Mi a különbség a unit test, integration test, acceptance test és regression test között?**  
   - **Unit test**: Egyedi kódblokkok (funkciók, metódusok) tesztelése.  
   - **Integration test**: Különböző modulok együttműködésének tesztelése.  
   - **Acceptance test**: Az ügyfél igényeinek való megfelelés tesztelése, általában az end-user vagy stakeholder által végzett.  
   - **Regression test**: Ellenőrzi, hogy a korábbi funkciók még mindig működnek új kód vagy módosítások után.

9. **Milyen előnyökkel jár a Test Driven Development (TDD)?**  
   - Segít a kód minőségének javításában, csökkenti a hibák számát, elősegíti a könnyebb karbantartást, és biztosítja, hogy a kód megfeleljen a követelményeknek a fejlesztés minden lépésénél.

10. **Mikor használunk rendszer- (system) tesztelést, és hogyan figyeljük meg a teljesítményt különböző környezetekben?**  
   - Rendszertesztelést a teljes rendszer funkcionalitásának ellenőrzésére használunk. Teljesítményt különböző környezetekben monitorozhatjuk eszközökkel, mint például a JMeter vagy a LoadRunner, amelyek szimulálják a felhasználói forgalmat.

11. **Mi az a branch coverage és a code coverage, és miért fontosak ezek a tesztelés során?**  
   - **Branch coverage**: A kódbázisban található elágazások (if, switch) tesztelésének arányát méri.  
   - **Code coverage**: Az összes kódvonal hány százalékát tesztelik.  
   - Fontosak, mert segítenek azonosítani a tesztelés által lefedett kódot és a hiányosságokat, biztosítva a magasabb tesztelési minőséget.

12. **Miért nem elegendő egy statikus tesztelés (pl. Pylint), és miben különbözik a futó programok dinamikus tesztelésétől?**  
   - A statikus tesztelés a kód szintaxisának és stilisztikai problémáinak ellenőrzésére szolgál, de nem képes észlelni a futás közbeni hibákat.  
   - A dinamikus tesztelés során a kód valóban fut, lehetővé téve a funkcionális és logikai hibák azonosítását, amelyeket a statikus tesztelés nem tud észlelni. 

## Automatikus tesztelés eszközei:
#### Ezekhez jöhetnek jobb kérdések is

13. **Hogyan használható a Cypress, Playwright vagy Puppeteer a böngésző teszteléshez?**  
   - **Cypress**: Egyszerű és intuitív eszköz, amely lehetővé teszi az end-to-end tesztelést a böngészőben, valós időben.  
   - **Playwright**: Keresztplatformos megoldás, amely támogatja a Chrome, Firefox és Safari böngészőket, lehetővé téve a modern webalkalmazások automatizált tesztelését.  
   - **Puppeteer**: A Chrome vagy Chromium fejlesztéséhez használt könyvtár, amely lehetővé teszi a böngészőprogramozást és a tesztelést javascriptben.

14. **Mit csinál a `pytest.mark.parametrize` dekorátor, és miért hasznos?**  
   - A `pytest.mark.parametrize` lehetővé teszi, hogy egy tesztfüggvényt különböző bemeneti értékekkel futtassunk. Ezért hatékonyabb, mert csökkenti a kód duplikálását és egyszerűsíti a tesztelést különböző forgatókönyvek során.

15. **Hogyan lehet több szálon futtatni teszteket a Python-xdist használatával?**  
   - Az `xdist` telepítését követően a tesztek párhuzamos futtatásához a következő parancsot használhatjuk:  
     ```
     pytest -n <szálak_száma>
     ```

16. **Miért hasznos egy `pytest` esetén a `--junitxml` paraméter, és mire használható a generált fájl?**  
   - A `--junitxml` paraméter lehetővé teszi a teszteredmények JUnit formátumban történő exportálását. A generált fájl hasznos a CI/CD folyamatok integrálásához és a tesztelési eredmények könnyebb elemzéséhez különböző eszközökben. 

## Hibakezelés és debug:
22. **Mit jelent a ZeroDivisionError, és hogyan kezelhető a `pytest.raises` funkcióval?**  
   - A **ZeroDivisionError** egy hiba, ami akkor fordul elő, amikor egy számot nullával próbálunk osztani. A `pytest.raises` funkció segítségével tesztelhetjük, hogy a kód dob-e hibát olyan esetekben, amikor ezek a feltételek teljesülnek:
     ```python
     with pytest.raises(ZeroDivisionError):
         1 / 0
     ```

23. **Miért kell pontosan meghatározni, hogy milyen hibát várunk a tesztelés során?**  
   - A pontos hibakövetelmények meghatározása segít azonosítani, hogy a kód megfelel-e a várt működésnek. Ha a várt hiba nem történik meg, vagy más típusú hiba jelentkezik, a tesztelés nem hasznos, ezért a hibakezelés helyességének biztosítása kulcsfontosságú.

24. **Hogyan működnek a `try ... except ... finally` blokkok hibakezelésnél a Pythonban?**  
   - A `try` blokkban futó kódot ellenőrzik a hibákra. Ha hiba lép fel, az `except` blokk végrehajtódik, ahol a hiba kezelése történik. A `finally` blokk mindig végrehajtódik, függetlenül attól, hogy történt-e hiba, és jellemzően erőforrások felszabadítására használják.

## Tesztelés Python környezetben:

25. **Milyen szerepe van az `assert` állításnak egy unit tesztelés során?**  
   - Az `assert` állítás ellenőrzi, hogy egy kifejezés igaz-e. Ha hamis, a teszt meghiúsul, ami segít a várható és tényleges eredmények közötti eltérések azonosításában.

26. **Mi az `Arrange, Act, Assert` tesztelési minta, és hogyan alkalmazható?**  
   - Az `Arrange, Act, Assert` minta tesztelési struktúrája:
     - **Arrange**: Beállítjuk az előfeltételeket és az adatokat.
     - **Act**: Meghívjuk a tesztelni kívánt funkciót.
     - **Assert**: Ellenőrizzük az eredményeket.  
   - Ez a minta segít tisztán és érthetően strukturálni a teszteket.

27. **Hogyan használhatók az előre definiált pytest parancssori opciók, mint pl. `--maxfail` vagy `--quiet`?**  
   - A `--maxfail` paraméter korlátozza a futtatott tesztek számát, amely után a tesztelés leáll, ha a megadott számú teszt megbukik. A `--quiet` opció csökkenti a megjelenített információ mennyiségét, így a kimenet tömörebb lesz. Ezeket a parancssori opciókat tesztelés indításakor használjuk, például:
     ```
     pytest --maxfail=1 --quiet
     ``` 

## Extrák

### Volume csatolása

A volume csatolása egy konténerhez azt jelenti, hogy a konténer számára elérhetővé teszünk egy külső adattároló helyet (volumet), amely független a konténer életciklusától. Ez lehetővé teszi az adatok megőrzését akkor is, ha a konténer újraindul vagy törlésre kerül.  

#### **Hogyan csatolhatunk volumet egy konténerhez?**  
A `docker run` parancsban a `-v` vagy a `--mount` opció segítségével csatolhatunk volumet.

#### **Példa a volume használatára**  
1. **Hozzunk létre egy új volumet:**
   ```bash
   docker volume create my_volume
   ```

2. **Indítsunk egy konténert, amelyhez csatoljuk a volumet:**
   ```bash
   docker run -d --name my_container -v my_volume:/data nginx
   ```

   Ebben a példában:
   - **`-v my_volume:/data`**: A `my_volume` nevű volumet csatoljuk a konténer `/data` könyvtárához.
   - **`nginx`**: Egy alapértelmezett NGINX szervert futtatunk.

3. **Ellenőrizzük, hogy a volume csatolva lett:**
   ```bash
   docker inspect my_container
   ```
   Az eredményben a **Mounts** szekció mutatja, hogy a `my_volume` csatolva van a konténer `/data` útvonalához.

4. **Tartós adat mentése:**
   A konténerben a `/data` könyvtárban létrehozott vagy módosított fájlok a `my_volume`-be kerülnek. Ha a konténert újraindítjuk vagy töröljük, az adatok a volumeben megmaradnak, és egy új konténer is hozzáférhet ezekhez.

#### **Volume újrahasználata másik konténerrel**  
Egy másik konténer is használhatja a `my_volume` volumet:  
```bash
docker run -d --name another_container -v my_volume:/data nginx
```

Ebben az esetben az új konténer ugyanazokat az adatokat éri el, amelyek a volumeben tárolódnak. Ez ideális adatbázisokhoz, konfigurációs fájlokhoz vagy bármilyen állandó adattárolási szükséglethez.

### Statikus weboldal készítése Dockerrel és Nginx-el

A következőkben bemutatom, hogyan készíthetünk egy statikus weboldalt Docker segítségével, Nginx-et hasznosítva.

---

### **1. Hozzuk létre a szükséges fájlokat**
#### **Statikus tartalom létrehozása**
Hozzunk létre egy könyvtárat, például `static-website`, és tegyünk bele egy egyszerű statikus HTML fájlt.

```plaintext
static-website/
├── Dockerfile
├── index.html
```

#### **`index.html` tartalma:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Statikus Weboldal</title>
</head>
<body>
    <h1>Üdvözöllek a statikus weboldalamon!</h1>
    <p>Ez az oldal egy Docker konténerben fut Nginx segítségével.</p>
</body>
</html>
```

---

### **2. Dockerfile létrehozása**
A Dockerfile tartalmazza az utasításokat az Nginx és a statikus fájlok beállításához.

#### **`Dockerfile` tartalma:**
```dockerfile
# Alap Nginx image használata
FROM nginx:alpine

# Másoljuk a statikus fájlokat az Nginx alapértelmezett html könyvtárába
COPY index.html /usr/share/nginx/html/

# Nginx futtatása
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### **3. Konténer létrehozása és futtatása**

#### **1. Építsük meg az image-t:**
A `Dockerfile` alapján hozzuk létre az Nginx image-et:
```bash
docker build -t static-website .
```

Ebben:  
- **`-t static-website`**: Az új image neve.  
- A `.` jelzi, hogy a `Dockerfile` az aktuális könyvtárban található.

#### **2. Futtassuk a konténert:**
Indítsuk el a konténert az újonnan létrehozott image segítségével:
```bash
docker run -d -p 8080:80 --name my-static-site static-website
```

Ebben:  
- **`-d`**: A konténert háttérben futtatja.  
- **`-p 8080:80`**: A host gép 8080-as portját az Nginx konténer 80-as portjára irányítja.  
- **`--name my-static-site`**: A konténer neve.  
- **`static-website`**: A korábban létrehozott image neve.

---

### **4. Teszteljük a weboldalt**
Nyissuk meg a böngészőt, és írjuk be az alábbi URL-t:
```
http://localhost:8080
```

Meg kell jelenjen a weboldal az **"Üdvözöllek a statikus weboldalamon!"** szöveggel.

---

### **5. (Opcionális) A konténer leállítása és törlése**
#### Konténer leállítása:
```bash
docker stop my-static-site
```

#### Konténer törlése:
```bash
docker rm my-static-site
```

#### Image törlése:
```bash
docker rmi static-website
```

Ez a megközelítés gyors és egyszerű módja annak, hogy Docker segítségével statikus weboldalt futtassunk Nginx-en.