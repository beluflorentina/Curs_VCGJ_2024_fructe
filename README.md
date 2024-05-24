# Curs_VCGJ_2024_fructe

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
1. [Configurare](#configurare)
1. [Testare cu pytest](#testare-cu-pytest)
1. [Verificare statica. pylint - calitate cod](#verificare-statica-cu-pylint)
1. [DevOps](#devops-ci)

   

# Descriere aplicatie

Aplicatia afiseaza informatii despre fructe intr-o pagina web. A fost testata pe Ubuntu 22.04.
Componenta WEB a aplicatiei se bazeaza pe framework-ul `Flask`.
Aplicatia este simpla, afiseaza informatii despre descrierea si culoarea fructului cu ajutorul functiilor culoare_guava() si descriere_guava().
Informatiile sunt preluate apoi in functiile de tip `view` specifice fiecarei pagini si returnate clientului WEB care apeleaza serverul.

Pentru o navigare mai usoara in browser, pagina fructului contine link-uri catre paginile culoare si descriere, iar aceste pagini contin link-uri catre pagina initiala (ruta standard) si una catre cealalta.

Rutele pentru pagini sunt:
 * ruta standard '/' - URL: http://127.0.0.1:5000
 * rute in aplicatia WEB pentru:
   * fruct:     '/guava' - URL: 'http://127.0.0.1:5000/guava',
   * culoare:   '/culoare' -                        .../guava/culoare
   * descriere: '/descriere' -                      .../guava/descriere

Aplicatia include suport pentru containerizare in fisierul `Dockerfile` din directorul principal al aplicatiei.

Din punct de vedere al testarii, este inculs unit testing cu pytest, pentru functiile din biblioteca aplicatiei, aflate in directorul `app/lib`.

`DevOps CI`.
Pipeline-ul pentru Jenkins este definint in fisierul `Jenkinsfile`.
Pipeline-ul cloneaza codul, creeaza mediul de lucru virtual (venv-ul), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).


# Configurare
[cuprins](#cuprins)


```text 
   # Creare spatiu de lucru si clonare aplicatie:   
   mkdir fructe
   cd fructe
   git clone https://github.com/beluflorentina/Curs_VCGJ_2024_fructe.git

   sudo apt upgrade
   sudo apt install git

   cd Curs_VCGJ_2024_fructe
   git checkout devel-Marin-Jan223
   
   # Creare mediu virtual si activare
   python3 -m venv .venv
   . .venv/bin/activate
   
   # Instalare pachete
   pip install flask
   pip install pytest
   pip install pylint
   
   # Rulare aplicatie // Creare componenta web aplicatie pe baza fremework-ului flask
   flask --app 443_fructe.py run --debug

   # Creare si rulare container
   cd <director-dockerfile>
   docker build -t <nume-imagine>
   docker run -p 8080:5000 --name <nume-container> <nume-imagine>
   
   # Incarcare imagine pe Docker Hub
   docker login
   docker tag <nume-imagine> jan/<nume-imagine>:latest
   docker push 	jan/<nume-imagine>:latest
   
   # Testare // Rulare fisier de testare a functiilor de biblioteca
   cd app/test
   pytest .
   
   # Staging, inregistrare modificari si sincronizare local cu remote
   git add <fisier_modificat>
   git commit -m "Mesaj logging modificari"
   git push origin devel-Marin-Jan223
   
   # Oferire drepturi Jenkins // Pentru ca serverul jenkins sa poate crea container
   sudo groupadd docker
   sudo usermod -aG docker $USER
   sudo gpasswd -a $USER docker
   restart Ubuntu
   
   # Rulare Jenkins
   jenkins
   # Accesare server Jenkins din browser la 127.0.0.1:8080 sau localhost:8080
   
```


# Testare cu pytest
[cuprins](#cuprins)

Functiile din biblioteca de functii a aplicatie au teste de tip 'unit - test' asociate - se verifica ca functiile de biblioteca sa returneze anumite valori pre-definite.
Testul compara valoarea obtinuta la apelul functiei cu valoarea asteptata si returneaza True daca valoarea primita de la functie este cea asteptata si False in caz contrar.

Pentru testare s-a folosit pachetul **pytest** din python. 



# Verificare statica cu pylint
[cuprins](#cuprins)

- **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
- in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori



# DevOps CI
[cuprins](#cuprins)
- CI = Continuous Integration

Pipeline-ul Jenkins automatizeaza procesyl de build, test si deploy pentru o aplicatie. Jenkinsfile este un script care defineste pipeline-ul Jenkins.
