# Curs_VCGJ_2024_fructe

# Cuprins

   

# Descriere aplicatie

Aplicatia afiseaza informatii despre fructe intr-o pagina web. A fost testata pe Ubuntu 22.04.
Componenta WEB a aplicatiei se bazeaza pe framework-ul `Flask`.
Aplicatia este simpla, afiseaza informatii despre descrierea si culoarea fructului cu ajutoru functiilor culoare_grapefruit() si descriere_grapefruit().
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


# Configurare


```text 
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
   docker build -t imagine_aplicatie
   docker run -p 8080:5000 --name container imagine_aplicatie
   
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

   # Vizualizare aplicatie
   
   ![Screenshot_1](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/145229192/f596efe8-3eec-4f92-8c13-54df7feb367c)

   
