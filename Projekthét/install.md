Codespacesben a megfelelő branch (indev) megnyitásával főoldalon:

Python extension letöltése, majd Flask telepítése

```console
$ pip3 install flask
```
Indítás:
```console
$ python3 -m marrakech
```
és a kiírt porton megnyitni, ami valahogy így néz ki:
```console
 * Running on http://127.0.0.1:5000
```
Cntrl+Click a portra.

Megnyitás saját gépről, Visual Studio Codeban:  
Python extension és telepítés weboldalról.  
Flask telepítése:
```console
$ py -m pip install flask
```
Megnyitás:
```console
$ py -m marrakech
```
Játékon kívüli third-party extensionök telepítés:
Telepíteni kell a felhasznált 3rd-party csomagokat:
```console
pip install -r requirements.txt
```