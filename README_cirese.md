 ```Curs_VCGJ_2024_fructe_cirese```

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
2. [Descriere versiune](#descriere-versiune)
3. [Setup si rulare aplicatie](#configurare)
   - [Rulare aplicatie prin Flask](#rulare-aplicatie-prin-flask)
   - [Rulare aplicatie prin Docker](#rulare-aplicatie-prin-docker)

# Descriere aplicatie

Aceasta aplicatie afiseaza informatii despre diverse fructe. Pe acest branch, sunt implementate functii care returneaza descrierea si culoare fructului de cires si fructului de acai.
Poate fi executata atat pe Linux cat si pe Windows. A fost dezvoltata si testata pe Ubuntu 22.04 dar functioneaza si pe Windows 11. Totusi, pentru Windows 11 inca nu se ofera suport si va trebui sa va configurati pe cont propriu environment-ul.

Componenta WEB a aplicatiei se bazeaza pe framework-ul `Flask`.
Ca si functionare, aplicatia are un fisier de library definit in app/lib/biblioteca_fructe.py unde se regasesc functiile ce intorc detaliile fructelor, functii mai apoi apelate in app/443_fructe.py.

Pagina principala afiseaza o lista de fructe, iar accesand unul din itemele listei se redirectioneaza catre pagina cu detalii despre fructul respectiv.

Aplicatia include suport pentru containerizare in fisierul `Dockerfile` din directorul principal al aplicatiei.

# Descriere versiune
 * ruta standard '/' - URL: http://127.0.0.1:5000 ; afiseaza lista de fructe
 * rute in aplicatia WEB pentru:
   * fruct acai:           '/acai' - URL: 'http://127.0.0.1:5000/acai',
   * culoare acai:         '/acai/culoare' -         .../acai/culoare
   * descriere acai:       '/acai/descriere' -       .../acai/descriere
   * fruct cireasa:        '/cirese' - URL: 'http://127.0.0.1:5000/cirese',
   * culoare cireasa:      '/cirese/culoare' -         .../acai/culoare
   * descriere cireasa:    '/cirese/descriere' -       .../acai/descriere

# Setup si rulare aplicatie

Se instaleaza toate dependintele necesare, daca nu sunt deja instalate:

```
NOTA: Daca nu aveti git instalat
sudo apt install git

sudo apt update
sudo apt upgrade -y
sudo apt install python3
sudo apt install python3-pip
sudo apt-get install python3-venv
```
Pentru instalare Docker Engine, se urmeaza instructiunile de la link-ul urmator:
https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

Se cloneaza aplicatia:

```
git clone https://github.com/beluflorentina/Curs_VCGJ_2024_fructe.git

cd Curs_VCGJ_2024_fructe
```
## Rulare aplicatie prin Flask

Se activeaza virtual environment-ul pentru a avea acces la Flask:

```
source .venv/bin/activate
```

Pentru rularea aplicatiei folosind Flask:
```
flask --app app/443_fructe.py run
```

Asa ar trebui sa arate rezultatul comenzii:
![Screenshot 2024-05-24 152449](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/132747703/fb98edfa-74d7-4cb6-9d0a-f3f2713791c0)

Accesand http://127.0.0.1:5000 in browser, ar trebui sa se incarce urmatoarea pagina:
![Screenshot 2024-05-24 152654](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/132747703/1de96d9c-73ca-4729-99ce-7297b55f1e5b)

## Rulare aplicatie prin Docker

Pentru rularea aplicatiei folosind Docker, se ruleaza urmatoarele comenzi:

```
sudo docker build -t <numecontainer> .
sudo docker run -dp 127.0.0.1:5000:5000 <numecontainer>
```

Pentru a lista containerele docker care ruleaza, se foloseste comanda
```
sudo docker ps
```
Exemplu pentru comenzile docker de mai sus:
![Screenshot 2024-05-24 153743](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/132747703/cd00d8b7-8050-4fce-88cf-4c2a9c512410)
![Screenshot 2024-05-24 153849](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/132747703/244a069f-db66-4a30-b8d6-011fb74f316d)

In continuare aplicatia va rula tot la 127.0.0.1:5000
```
