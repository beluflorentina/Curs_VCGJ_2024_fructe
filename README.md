# Curs_VCGJ_2024_fructe

# Utilizator DanSandu1609

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
1. [Configurare](#configurare)
1. [Testare cu pytest](#testare-cu-pytest)
1. [Verificare statica. pylint - calitate cod](#verificare-statica-cu-pylint)
1. [DevOps](#devops-ci)

   

# Descriere aplicatie

Aplicatia afiseaza informatii despre fructe intr-o pagina web. A fost testata pe Ubuntu 22.04.
Componenta WEB a aplicatiei se bazeaza pe framework-ul `Flask`.
Aplicatia este simpla, afiseaza informatii despre descrierea si culoarea fructului cu ajutoru functiilor culoare_banana() si descriere_banana().
Informatiile sunt preluate apoi in functiile de tip `view` specifice fiecarei pagini si returnate clientului WEB care apeleaza serverul.

Pentru o navigare mai usoara in browser, fiecare pagina contine link-uri catre celelalte pagini.

Rutele pentru pagini sunt:
 * ruta standard '/' - URL: http://127.0.0.1:5000
 * rute in aplicatia WEB pentru:
   * fruct:     '/banana' - URL: 'http://127.0.0.1:5000/banana',
   * culoare:   '/culoare' -                        .../banana/culoare
   * descriere: '/descriere' -                      .../banana/descriere

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
   git checkout devel_Sandu_Dan-Mihai
   
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
   git commit -m "Modificare"
   git push origin devel_Sandu_Dan-Mihai
   
   # Oferire drepturi Jenkins
   sudo groupadd docker
   sudo usermod -aG docker $USER
   sudo gpasswd -a $USER docker
   restart Ubuntu
   
   # Rulare Jenkins
   jenkins
   # Accesare server Jenkins din browser la 127.0.0.1:8080

```
# RULARE APLICATIE
![rulare](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/161347099/878c8cf7-c64b-4f85-9479-08824f069dc0)


# Testare cu pytest
[cuprins](#cuprins)

Functiile din biblioteca de functii a aplicatie au teste de tip 'unit - test' asociate - adica - este apelata functia si se asteapta o anumita valoare.
Testul compara valoarea obtinuta la apelul functie cu valoarea asteptata si returneaza True daca valoarea primita de la functie este cea asteptata si False in caz contrar.

Pentru testare s-a folosit pachetul **pytest** din python. 

![pytest](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/161347099/b76196f8-855d-4716-ad73-d82efea3b852)




# Verificare statica cu pylint
[cuprins](#cuprins)

- **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
- in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori

# Functionalitate aplicatie
![imagine2](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/161347099/7d939c45-a08e-476d-9ed5-95303a627fef)

![imagine1](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/161347099/ebf4cbf3-058b-4acb-8b10-98f47bfea079)


![DESCRIERE_BANANA](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/161347099/c6ce0d87-782e-42cc-a169-dfe2a26e5bd1)

![CULOARE_BANANA](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/161347099/211102ea-98f0-4859-9e3c-1e8f859fee12)


# Testare Jenkins

![Capture](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/161347099/1c641c65-6c24-4b7b-9300-561c0c274603)

![jenkins](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/161347099/901fdafb-49c1-42b9-91eb-a9aeda190bb8)


# Docker
![creare_docker](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/161347099/347b8227-c868-4d3a-9dec-0cb1f7ec2496)

![viz_docker](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/161347099/43720720-840d-4344-965b-8a721820556a)

![run_docker](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/161347099/ace97c7a-c8d3-45ef-8cdd-d67bc1272dec)


# DevOps CI
[cuprins](#cuprins)
- CI = Continuous Integration

Pipeline-ul Jenkins automatizeaza procesul de build, test si deploy pentru o aplicatie. Jenkinsfile este un script care defineste pipeline-ul Jenkins.

