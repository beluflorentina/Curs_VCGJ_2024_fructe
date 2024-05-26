# Curs_VCGJ_2024_fructe

# Cuprins
1. Descriere aplicatie
2. Configurare
3. Vizualizare aplicatie
4. Testare
   -Pytest
   -Jenkins
5. Containerizare 
   

# 1. Descriere aplicatie

Aplicatia afiseaza informatii despre fructe intr-o pagina web. A fost testata pe Ubuntu 22.04.
Componenta WEB a aplicatiei se bazeaza pe framework-ul `Flask`.
Aplicatia este simpla, afiseaza informatii despre descrierea si culoarea fructului cu ajutorul functiilor culoare_grapefruit() si descriere_grapefruit().
Informatiile sunt preluate apoi in functiile de tip `view` specifice fiecarei pagini si returnate clientului WEB care apeleaza serverul.

Pentru o navigare mai usoara in browser, fiecare pagina contine link-uri catre celelalte pagini.

Rutele pentru pagini sunt:
 * ruta standard '/' - URL: http://127.0.0.1:5000
 * rute in aplicatia WEB pentru:
   * fruct:     '/grapefruit' - URL: 'http://127.0.0.1:5000/grapefruit',
   * culoare:   '/culoare' -                        .../grapefruit/culoare
   * descriere: '/descriere' -                      .../grapefruit/descriere

Aplicatia include suport pentru containerizare in fisierul `Dockerfile` din directorul principal al aplicatiei.

Din punct de vedere al testarii, este inculs unit testing cu pytest, pentru functiile din biblioteca aplicatiei, aflate in directorul `app/lib`.

`DevOps CI`.
Pipeline-ul pentru Jenkins este definint in fisierul `Jenkinsfile`.
Pipeline-ul cloneaza codul, creeaza mediul de lucru virtual (venv-ul), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).


# 2. Configurare


``` 
   # Creare spatiu de lucru si clonare aplicatie:
   
   git clone https://github.com/beluflorentina/Curs_VCGJ_2024_fructe.git

   cd Curs_VCGJ_2024_fructe
   git checkout devel_Banica_Dragos
   
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
   docker build -t imagine_app .
   docker run -p 8080:5000 --name container imagine_app
   
   # Testare
   cd app/test/
   pytest .
   
   # Staging, inregistrare modificari si sincronizare local cu remote
   git add
   git commit -m "modificare1"
   git push origin devel_Banica_Dragos
   
   # Oferire drepturi Jenkins
   sudo groupadd docker
   sudo usermod -aG docker $USER
   sudo gpasswd -a $USER docker
   reboot
   
   # Rulare Jenkins
   jenkins
   # Accesare server Jenkins din browser la 127.0.0.1:8080
```
   # 3. Vizualizare aplicatie
   
   ![Screenshot_1](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/145229192/f53b048d-8bd0-498b-8528-61dde2a7a626)
   ![image](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/145229192/b0625d9d-616a-43f2-a1ae-89ec68125a46)

   # 4. Testare
   -pytest
   ![image](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/145229192/1552bfb1-be91-421e-bb40-4c762b15431b)

   -jenkins
   ![image](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/145229192/c7a651be-f23b-4191-91b5-d178ffed8a96)

   Vizualizare cu Blue Ocean
   ![image](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/145229192/a4bb7551-33aa-4eda-a445-448fd9ad7050)

   #  5. Containerizare

   ![image](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/145229192/deda587d-0baf-4283-814e-1480d1a12d0b)


   





   
