# Curs_VCGJ_2024_fructe

## Cuprins
1. [Descriere aplicatie](#descriere-aplicatie)
2. [Configurare](#configurare)
3. [Testare](#testare)
   - [Testare manuala](#testare-manuala)
   - [Testare automata cu Jenkins](#testare-automata-cu-jenkins)
4. [Verificare statica](#verificare-statica)
5. [DevOps CI](#devops-ci)

## Descriere aplicatie
Aplicatia 443_fructe afiseaza informatii despre fructe intr-o pagina web. A fost testata pe Ubuntu 22.04. Componenta WEB a aplicatiei se bazeaza pe framework-ul Flask. Aplicatia este simpla, afiseaza informatii despre descrierea si culoarea fructului cu ajutorul functiilor `culoare_guava()` si `descriere_guava()`. Informatiile sunt preluate apoi in functiile de tip view specifice fiecarei pagini si returnate clientului WEB care apeleaza serverul.

Pentru o navigare mai usoara in browser, pagina fructului contine link-uri catre paginile culoare si descriere, iar aceste pagini contin link-uri catre pagina initiala (ruta standard) si una catre cealalta.

Rutele pentru pagini sunt:
- ruta standard '/' - URL: `http://127.0.0.1:5000`
- rute in aplicatia WEB pentru:
  - fruct: '/guava' - URL: `http://127.0.0.1:5000/guava`
  - culoare: '/culoare' - URL: `http://127.0.0.1:5000/guava/culoare`
  - descriere: '/descriere' - URL: `http://127.0.0.1:5000/guava/descriere`

Aplicatia include suport pentru containerizare in fisierul Dockerfile din directorul principal al aplicatiei.

## Configurare

### Creare spatiu de lucru si clonare aplicatie
```bash
mkdir Proiect_SCC_433D_fructe
cd fructe
git clone https://github.com/beluflorentina/Curs_VCGJ_2024_fructe.git

sudo apt upgrade
sudo apt install git

cd Curs_VCGJ_2024_fructe
git checkout devel-Marin-Jan223
```
   
### Creare mediu virtual si activare
```bash
   python3 -m venv .venv
   . .venv/bin/activate
```
   
### Instalare pachete
```bash
   pip install flask
   pip install pytest
   pip install pylint
```
   
### Rulare aplicatie
Crearea componentei web aplicatiei pe baza fremework-ului flask functioneaza doar dupa activarea venv
```bash 
   flask --app 443_fructe.py run --debug
```
### Creare si rulare container
```bash
   cd <director-dockerfile>
   docker build -t <nume-imagine>
   docker run -p 8080:5000 --name <nume-container> <nume-imagine>
```

### Incarcare imagine pe Docker Hub
```bash
   docker login
   docker tag <nume-imagine> jan/<nume-imagine>:latest
   docker push 	jan/<nume-imagine>:latest
```
### Staging, inregistrare modificari si sincronizare local cu remote
```bash
git add <fisier_modificat>
git commit -m "Mesaj logging modificari"
git push origin devel-Marin-Jan223
```

## Testare

### Testare manuala
Functiile din biblioteca de functii a aplicatiei au teste de tip 'unit-test' asociate - se verifica ca functiile de biblioteca sa returneze anumite valori pre-definite. Testul compara valoarea obtinuta la apelul functiei cu valoarea asteptata si returneaza True daca valoarea primita de la functie este cea asteptata si False in caz contrar.

Pentru testare s-a folosit pachetul pytest din Python.
```bash
cd app/test
pytest .
```
### Testare automata cu Jenkins
Pipeline-ul pentru Jenkins este definit in fisierul Jenkinsfile in care avem definite stagiile urmatoare:
- **Build:** Creeaza environment-ul de testare prin activarea mediului venv si instalarea bibliotecilor necesare prin executarea de comenzi.
- **pylint - calitate cod:** Este un stagiu in care este verificata calitatea codului dar si verifica daca venv a fost activat.
- **Unit testing:** Este stagiul in care testam functiile din biblioteca_fructe cu ajutorul fisierului `test_lib.py` si comenzilor folosite.
- **Deploy:** Este stagiul care testeaza containerizarea aplicatiei prin crearea unei imagini docker si crearea containerului respectiv.

#### Oferire drepturi Jenkins
Pentru ca serverul Jenkins sa poata crea container:
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
sudo gpasswd -a $USER docker
sudo reboot
```
#### Rulare Jenkins
Serverul Jenkins este accesat din browser la 127.0.0.1:8080 sau la localhost:8080
```bash
jenkins
```

## Verificare statica
pylint - pachet Python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.). In cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori.

## DevOps CI
CI = Continuous Integration. Pipeline-ul Jenkins automatizeaza procesul de build, test si deploy pentru o aplicatie. Jenkinsfile este un script care defineste pipeline-ul Jenkins.

