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
Aplicatia este simpla, afiseaza informatii despre descrierea si culoarea fructului cu ajutoru functiilor culoare_acai() si descriere_acai().
Informatiile sunt preluate apoi in functiile de tip `view` specifice fiecarei pagini si returnate clientului WEB care apeleaza serverul.

Pentru o navigare mai usoara in browser, fiecare pagina contine link-uri catre celelalte pagini.

Rutele pentru pagini sunt:
 * ruta standard '/' - URL: http://127.0.0.1:5000
 * rute in aplicatia WEB pentru:
   * fruct:     '/acai' - URL: 'http://127.0.0.1:5000/acai',
   * culoare:   '/culoare' -                        .../acai/culoare
   * descriere: '/descriere' -                      .../acai/descriere

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
   git checkout devel_Belu_Florentina
   
   # Creare mediu virtual si activare
   python3 -m venv .venv
   . .venv/bin/activate
   
   # Instalare pachete
   pip install flask
   pip install pytest
   pip install pylint
   
   # Rulare aplicatie
   cd app
   flask --app 443_fructe.py run --debug

   # Creare si rulare container
   cd ..
   docker build -t imagine-aplicatie
   docker run -p 8080:500 --name container-aplicatie imagine-aplicatie
   
   # Incarcare imagine pe Docker Hub
   docker login
   docker tag imagine-aplicatie beluflorentina/imagine_aplicatie:latest
   docker push beluflorentina/imagine_aplicatie:latest
   
   # Testare
   cd app/test
   pytest .
   
   # Staging, inregistrare modificari si sincronizare local cu remote
   git add
   git commit -m "versiunea 1"
   git push origin devel_Belu_Florentina
   
   # Oferire drepturi Jenkins
   sudo groupadd docker
   sudo usermod -aG docker $USER
   sudo gpasswd -a $USER docker
   restart Ubuntu
   
   # Rulare Jenkins
   jenkins
   # Accesare server Jenkins din browser la 127.0.0.1:8080
   
```


# Testare cu pytest
[cuprins](#cuprins)

Functiile din biblioteca de functii a aplicatie au teste de tip 'unit - test' asociate - adica - este apelata functia si se asteapta o anumita valoare.
Testul compara valoarea obtinuta la apelul functie cu valoarea asteptata si returneaza True daca valoarea primita de la functie este cea asteptata si False in caz contrar.

Pentru testare s-a folosit pachetul **pytest** din python. 



# Verificare statica cu pylint
[cuprins](#cuprins)

- **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
- in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori



# DevOps CI
[cuprins](#cuprins)
- CI = Continuous Integration

Pipeline-ul Jenkins automatizeaza procesyl de build, test si deploy pentru o aplicatie. Jenkinsfile este un script care defineste pipeline-ul Jenkins.
