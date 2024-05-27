# Curs_VCGJ_2024_fructe

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
1. [Configurare](#configurare)
1. [Rularea aplicatiei prin flask](#Rularea-aplicatiei-prin-flask)
1. [Rularea aplicatiei prin docker](#Rularea-aplicatiei-prin-docker)


   

# Descriere aplicatie

Aplicatia afiseaza informatii despre fructe intr-o pagina web. A fost dezvoltata si testata pe Ubuntu 22.04
Componenta WEB a aplicatiei se bazeaza pe framework-ul `Flask`.
Aplicatia este simpla, afiseaza informatii despre descrierea si culoarea fructului cu ajutoru functiilor culoare_corcoduse() si descriere_corcoduse().
Informatiile sunt preluate apoi in functiile de tip `view` specifice fiecarei pagini si returnate clientului WEB care apeleaza serverul.
Aplicaia are un fisier de library definit in app/lib/biblioteca_fructe.py unde se gasesc functiile ce intorc detaliile fructelor.


Rutele pentru pagini sunt:
 * ruta standard '/' - URL: http://127.0.0.1:5000
 * rute in aplicatia WEB pentru:
   * fruct:     '/corcoduse' - URL: 'http://127.0.0.1:5000/corcoduse',
   * culoare:   '/culoare' -                        .../corcoduse/culoare
   * descriere: '/descriere' -                      .../corcoduse/descriere

Aplicatia include suport pentru containerizare in fisierul `Dockerfile` din directorul principal al aplicatiei.

Din punct de vedere al testarii, este inculs unit testing cu pytest, pentru functiile din biblioteca aplicatiei, aflate in directorul `app/lib`.

`DevOps CI`.
Pipeline-ul pentru Jenkins este definint in fisierul `Jenkinsfile`.
Pipeline-ul cloneaza codul, creeaza mediul de lucru virtual (venv-ul), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).


# Configurare
[cuprins](#cuprins)


```text 
   # Creare spatiu de lucru si clonare aplicatie:   
   mkdir fruct
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
   
   #NOTA: Daca nu aveti git instalat
   sudo apt install git

   sudo apt update
   sudo apt upgrade -y
   sudo apt install python3
   sudo apt install python3-pip
   sudo apt-get install python3-venv
   
```


# Rularea aplicatiei prin flask
[cuprins](#cuprins)

Se activeaza virtual environment-ul pentru a avea acces la Flask:


```
source .venv/bin/activate
```

Pentru rularea aplicatiei folosind Flask:
```
flask --app app/443_fructe.py run
``` 
Accesand http://127.0.0.1:5000 in browser, ar trebui sa se incarce pagina "Fructe"



#Rularea aplicatiei prin docker
[cuprins](#cuprins)

Pentru rularea aplicatiei folosind Docker, se ruleaza urmatoarele comenzi:

```
sudo docker build -t <numecontainer> .
sudo docker run -dp 127.0.0.1:5000:5000 <numecontainer>
```

Pentru a lista containerele docker care ruleaza, se foloseste comanda
```
sudo docker ps
```

In continuare aplicatia va rula tot la 127.0.0.1:5000
```


