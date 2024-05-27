# Curs_VCGJ_2024_fructe

Funda Gheorghe : caise.

## Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
2. [Pregatire mediu de lucru](#pregatire-mediu-de-lucru)
3. [Lintare & testare](#lintare--testare)
4. [Rulare aplicatie](#rulare-aplicatie)
5. [DevOps Continuous Integration](#continuous-integration)
6. [Flow Git](#flow-git)


## Descriere aplicatie

Aplicatia ofera informatii despre  fructul "caisa" intr-o pagina web. Aceasta poate fi rulata ori local, ori rulata folosind containere. A fost testata pe Ubuntu 22.04. Componenta WEB a aplicatiei se bazeaza pe framework-ul Flask. Aplicatia ofera informatii despre descrierea si istoria fructului cu ajutorul functiilor istorie_caisa() si descriere_caisa(). Informatiile sunt preluate din biblioteca aflata in folder-ul `lib` si sunt afisate folosind functiile Flask de tip view specifice fiecarei pagini, apoi returnate clientului WEB care apeleaza serverul.

Rutele paginii sunt:

- ruta standard '/' - URL : http://127.0.0.1:5000/
- rute in aplicatia WEB:
	- fruct: '/caisa'- URL: http://127.0.0.1:5000/caisa
	- istorie: '/caisa/istorie' - URL: http://127.0.0.1:5000/caisa/istorie
	- descriere: '/caisa/descriere' - URL: http://127.0.0.1:5000/caisa/descriere

Aplicatia include suport pentru containerizare in fisierul Dockerfile din directorul principal al aplicatiei.

Din punct de vedere al testarii, aceasta poate fi realizata fie prin utilizarea pytest, ori prin pipeline-ul Jenkins. Jenkins ne ofera o testare automatizata, aceasta cloneaza codul, creeaza mediul virtual si ruleaza unit-test-urile.

## Pregatire mediu de lucru

# Creare spatiu de lucru si clonare aplicatie:
mkdir proiect_final
cd proiect_final
git clone https://github.com/beluflorentina/Curs_VCGJ_2024_fructe.git

cd Curs_VCGJ_2024_fructe
git checkout devel_Funda_Geo

# Creare mediu virtual
python3 -m venv .venv
. .venv/bin/activate

# Instalare pachete
pip install flask
pip install pytest
pip install pylint

# Rulare locala a aplicatiei
cd app
flash --app 443_fructe.py run --debug

# Rulare folosind containere
cd ..
docker build -t imagine_caisa_final .
docker run -p 5000:5000 -- imagine_caisa_final

# Testare folosind pytest
cd app
pytest .

# Testare folosind jenkins
sudo systemctl start jenkins
accesare server si creeare pipeline



## Lintare & testare

Folosind pytest putem verifica functionalitatea codului prin niste test-case-uri. Ce se intampla este ca se apeleaza functia de testare si se verifica daca anumite fragmente din text-ul pentru caisa se afla in descriere sau istorie. Este o simpla functie ce returneaza True sau False. ex comanda: pytest . (in directorul unde se afla aplicatia)

Folosind pylint putem testa calitatea codului (spatii, nume de variabile, variabile neutilizate). In cadrul proiectului nu exista erori, ci doar avertismente privind spatierea si numele functiilor. ex comanda: pylint . (in directorul unde se afla aplicatia)


## Continuous Integration

Cand vorbim de CI, vorbim despre pipeline-ul Jenkins. Procesul este urmatorul
- build 
- lint 
- test
- deploy

Acest pipeline este definit de catre JenkinsFile-ul din proiect.
