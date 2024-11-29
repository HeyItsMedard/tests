### Hibaelhárítás és vizsgálati lépések, ha az alkalmazás nem működik:

1. **Általános vizsgálatok a szerver oldalán**:
   - **Pingelés és hálózati elérhetőség**:
     - Teszteld, hogy a szerver válaszol-e:  
       ```bash
       ping <szerver_ip>
       ```
     - Ha a ping sikeres, a hálózat működik. Ellenkező esetben ellenőrizd a kapcsolatot (pl. router, DNS).
   - **SSH kapcsolat ellenőrzése**:
     - Próbálj belépni a szerverre:  
       ```bash
       ssh user@<szerver_ip>
       ```
     - Ha nem sikerül, ellenőrizd az SSH szolgáltatást:  
       ```bash
       systemctl status ssh
       ```

2. **Docker specifikus ellenőrzések**:
   - **Konténerek állapotának lekérdezése**:  
     ```bash
     docker ps -a
     ```
     - Ha a konténer nem fut, próbáld újraindítani:
       ```bash
       docker start <container_id>
       ```
     - Ellenőrizd a konténer logjait:
       ```bash
       docker logs <container_id>
       ```
     - Ha a logban "internal error" vagy más hibák szerepelnek, vizsgáld a konfigurációs fájlokat.
   - **Volume és network ellenőrzése**:
     - Nézd meg, hogy a szükséges volume-ok és network-ök megfelelően vannak-e csatolva:  
       ```bash
       docker inspect <container_id>
       ```

3. **Docker Compose hibák kezelése**:
   - **Függőségek és indítási sorrend**:
     - A `depends_on` nem garantálja, hogy a függőség teljesen készen áll. Használj egészségügyi ellenőrzést (`healthcheck`), például MySQL-re:
       ```yaml
       healthcheck:
         test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
         interval: 10s
         retries: 5
       ```
   - **Konfiguráció újragenerálása**:
     - Töröld és állítsd vissza a konténereket:  
       ```bash
       docker-compose down && docker-compose up -d
       ```

4. **NGINX hibák vizsgálata**:
   - **Konfigurációs fájl érvényessége**:  
     Ellenőrizd az NGINX konfigurációt:  
     ```bash
     nginx -t
     ```
   - **Port ütközés**:
     - Ellenőrizd, hogy másik szolgáltatás nem használja-e a szükséges portot:
       ```bash
       netstat -tuln | grep <port_number>
       ```

5. **Hálózati problémák feltárása**:
   - **DNS és domain ellenőrzése**:
     - Győződj meg arról, hogy a domain megfelelően oldódik fel:  
       ```bash
       nslookup <domain_name>
       ```
   - **Nginx Proxy Manager beállítások**:
     - Ellenőrizd, hogy a konténerek ugyanabban a hálózatban vannak-e:
       ```yaml
       networks:
         npm:
           external: true
       ```

6. **SSL hibák és HTTPS kapcsolatok**:
   - **SSL tanúsítvány ellenőrzése**:
     - Nézd meg a tanúsítvány érvényességét, például:  
       ```bash
       openssl s_client -connect <domain_name>:443
       ```
   - **Tanúsítvány újragenerálása**:  
     Ha a tanúsítvány lejárt, regeneráld Let's Encrypt vagy Nginx Proxy Manager segítségével.

7. **Erőforrás-problémák**:
   - Ellenőrizd a gép és a konténerek erőforrás-felhasználását:  
     ```bash
     docker stats
     ```
   - Ha a memória vagy CPU terhelés magas, próbálj skálázást vagy erőforrás-korlátozást beállítani:
     ```yaml
     deploy:
       resources:
         limits:
           memory: 512M
           cpus: "0.50"
     ```

8. **Környezeti változók és titkok**:
   - Győződj meg róla, hogy az alkalmazás által használt környezeti változók helyesen vannak megadva (pl. adatbázis-jelszó, API-kulcsok).  
     ```bash
     docker inspect <container_id> | grep Env
     ```

9. **Rendszeres hibák elemzése és naplózás**:
   - Vizsgáld a rendszer naplóit, például NGINX és Docker hibák esetében:
     - NGINX:  
       ```bash
       cat /var/log/nginx/error.log
       ```
     - Docker daemon log:  
       ```bash
       journalctl -u docker
       ```

10. **Utolsó lépések: frissítések és újratelepítés**:
    - **Docker image frissítése**:  
      Ha az alkalmazás régi verziót használ, próbálkozz a legújabb image-sel:  
      ```bash
      docker pull <image_name>:latest
      ```
    - **Újratelepítés**:  
      Ha minden más kudarcot vall, töröld és hozd létre újra az alkalmazást.

## Órai:

+1 compose és annak pullolása futtatása (kb. 5 sor a fájlban image-l) compose up -d
+1 hogyan lesz egy domain https saját gépen? dockerrel
   - 1. : portainer stack < file content
   - 2. : deploy stack
   - 3. : proxy manager login
   - 4. : szerzett domain.com pl. name.com-tól
   - 5. : ip: cica
   - 6. : 8080:80 8080 külső 80 belső dockeren belül fut a proxy manager, szóval 80
   - 7. : ssl certificate beszerzése
   - 8. : internal conflict error -> 
      - name
      - port
      - image neve
      - container fut-e
      - van e net?
      - ssh-t megtekinteni (fut-e a szerver)
      - nginx proxy managerben egy hálózaton kéne legyenek: nincsenek
         - meg kell adni composeban a networkot
            networks:
               npm:
                  external: true
   - 9. :
   - 10. :

