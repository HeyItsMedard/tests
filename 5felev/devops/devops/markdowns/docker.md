## **Folyamat lépései**

### **1. Docker image letöltése**
Például az Nginx image-et fogjuk használni.

```bash
docker pull nginx:latest
```
Ez a parancs letölti az Nginx image legújabb verzióját.

---

### **2. Volume létrehozása**
A volume lehetővé teszi, hogy a konténer adatai tartósan tárolódjanak.

```bash
docker volume create my_nginx_data
```

Ezzel létrehoztunk egy `my_nginx_data` nevű volumet. Ez a volume a konténer fájlrendszerén kívül tárolja az adatokat.

---

### **3. Hálózat létrehozása**
A Dockerben külön hálózatot hozhatsz létre, hogy jobban elkülönítsd a konténereket.

```bash
docker network create my_custom_network
```

Ez a parancs létrehoz egy `my_custom_network` nevű bridge típusú hálózatot. Az alapértelmezett bridge hálózathoz képest ez testreszabottabb izolációt és kommunikációt biztosít a konténerek között.

---

### **4. Konténer létrehozása és indítása**
Hozzunk létre egy konténert az Nginx image alapján, és kapcsoljuk hozzá a korábban létrehozott volumet és hálózatot.

```bash
docker run -d \
  --name my_nginx \
  -p 8080:80 \
  --network my_custom_network \
  -v my_nginx_data:/usr/share/nginx/html \
  nginx:latest
```

**Parancsmagyarázat:**
- **`-d`**: A konténer háttérben futtatása.
- **`--name my_nginx`**: A konténer neve `my_nginx` lesz.
- **`-p 8080:80`**: A host gép 8080-as portját összekötjük a konténer 80-as portjával.
- **`--network my_custom_network`**: A konténert a `my_custom_network` nevű hálózathoz csatlakoztatjuk.
- **`-v my_nginx_data:/usr/share/nginx/html`**: A `my_nginx_data` volume csatolása a konténer `/usr/share/nginx/html` könyvtárához, ahol az Nginx alapértelmezett HTML fájljai találhatók.
- **`nginx:latest`**: Az image neve és verziója.

---

### **5. Tesztelés**
Nyisd meg a böngészőt, és írd be:
```
http://localhost:8080
```
Ekkor az Nginx alapértelmezett weboldalát kell látnod.

---

### **6. Ellenőrzés**
#### **Konténerek listázása**
```bash
docker ps
```

#### **Volume-ok listázása**
```bash
docker volume ls
```

#### **Hálózatok listázása**
```bash
docker network ls
```

#### **Hálózat információk ellenőrzése**
```bash
docker network inspect my_custom_network
```

Ez megmutatja a hálózaton lévő összes csatlakoztatott konténert (lehet több is).

---

### **7. Opciók a konténer leállítására és eltávolítására**

#### Konténer leállítása:
```bash
docker stop my_nginx
```

#### Konténer eltávolítása:
```bash
docker rm my_nginx
```

#### Volume eltávolítása:
```bash
docker volume rm my_nginx_data
```

#### Hálózat eltávolítása:
```bash
docker network rm my_custom_network
```

---

Ez a folyamat bemutatja, hogyan hozhatsz létre egy image-t, konténert, volumet és hálózatot helyben. Az ilyen struktúra ideális például webalkalmazások vagy tesztelési környezetek lokális futtatásához.