`Curs_VCGJ_2024_fructe`
=======================

# Identificator utilizator Borge201

# Cuprins
1. [Descriere aplicatie](#descriere-aplicatie)
1. [Configurare](#configurare)
1. [Vizualiare aplicatie](#vizualizare aplicatie)
1. [Verificare](#verificare)
   1. [Teste manuale](#teste-manuale)
   1. [Teste Jenkins](#teste-jenkins)
   1. [Teste pylint](#teste-pylint)
1. [Containerizare](#containerizare)
1. [DevOps CI](#devops_ci)
1. [Bibliografie](#bibliografie)

# Descriere aplicatie
[cuprins](#cuprins)
Aplicatia reprezinta un site web care se bazeaza pe frameworkul Flask.
Aplicatia afiseaza detalii despre fructe, detalii cum ar fi culoarea si descrierea fructului.
Aplicatia este simpla, afiseaza informatii despre descrierea si culoarea fructului ackee cu ajutoru functiilor culoare_ackee() si descriere_ackee().
Informatiile sunt preluate in functiile de tip `view` specifice fiecarei pagini si returnate clientului care apeleaza serverul.
Paginile fructului (culoare, descriere) sunt definite in functiile din interiorul fisierului app/lib/biblioteca_fructe.py

Aplicatia include suport pentru containerizare in fisierul Dockerfile din directorul principal al aplicatiei.
Pipeline-ul pentru Jenkins este definit in fisierul Jenkinsfile.

Rutele pentru pagini sunt:
 * ruta standard '/' - URL http://127.0.01:5000
 * rute in aplicatia WEB pentru:
   * fruct: '/ackee' - URL: 'http://127.0.0.1/ackee';
   * culoare: '/culoare' - '.../ackee/culoare';
   * descriere: '/descriere' - '.../ackee/descriere'.

# Configurare
[cuprins](#cuprins)
```text
	# Creare spatiu de lucru si clonare:
	mkdir app_fructe
	cd app_fructe
	git clone https://github.com/beluflorentina/Curs_VCGJ_2024_fructe.git
	
	sudo apt upgrade
	sudo apt install git
	
	cd Curs_Vcgj_2024_fructe
	git checkout devel_Burlacel_George
	
	# Creare mediu virtual si activarea acestuia
	python3 -m venv .venv
	. .venv/bin/activate
	
	#Instalare pachete
	pip install falsk
	pip install pytest
	pip install pylint
	
	# Rulare manuala a aplicatiei:
	cd app
	flask --app 443_fructe.py run --debug
	
	# Creare si rulare container
	cd..
	sudo docker build -t imagine-aplicatie
	docker run -p 8080:5000 --name container_app_fructe imagine-aplicatie
	
	# Testare manuala:
	cd app/test
	pytest .
	
	# Staging, inregistrare modificari si sincronizare local cu remote:
	git add
	git commit -m "versiunea x"
	git push origin devel_Burlacel_George
	
	# Adaugarea permisiunilor Jenkins pentru a folosi docker:
	sudo usermod -a -G docker jenkins
	sudo systemctl restart jenkins.service
	# Rulare Jenkins
	
	jenkins
	# accesare server Jenkins din browser la 127.0.0.1:8080
	
```
# Vizualizare Aplicatie
[cuprins](#cuprins)
![imagine](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/435d388f-ada9-4732-b0b8-209f2aab4bbc)

# Verificare

## Teste manuale
[cuprins](#cuprins)

Testarea manuala se bazeaza pe fisierul test_lib.py din directorul app/test, acesta verifica daca anumite segmente de text sunt prezente in pagina, acest fapt ne semnifica ca metodele sunt corecte.
Testarea manuala si containerizarea s-a efectuat in venv.
Initial trebuie sa initializam mediul virtual venv, python3 -m venv .venv.
Comanda . .venv/bin/activate va activa mediul virtual.
Trebuie sa instalam pachetele necesare pentru proiect:
pip install flask
pip install pytest
pip install pylint

Test pytest si rularea aplicatie din flask:

![imagine_test_manual](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/81457568-4ebb-4eb4-87d9-7c3dead4d6b4)


## Teste Jenkins
[cuprins](#cuprins)
Pipelineul in Jenkins a fost definit in fisierul Jenkinsfile in care avem definite stagiile urmatoare:
Build, care ne creeaza enviromnetul de testare prin activarea mediului venv si instalarea biblitecilor necesare prin executarea de comenzi;
pylint -calitate cod, este un stagiu in care este verificata calitatea codului dar si verifica daca venv a fost activat;
Unit testing, este stagiul in care testam functiile din biblioteca_fructe cu ajutorul fisierului test_lib.py si comenzilor folosite;
Deploy este stagiul care testeaza containerizarea aplicatiei prin crearea unei imagini docker si crearea containerului respectiv.

S-a testat cu Jenkins si am obtinut astfel:
Configurare Jenkins:

![jenkins_config](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/7dc390fa-ac26-4ad2-b203-c87c55dfed9c)

Test Jenkins:

![test_jenkins](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/4358fb89-f016-49e0-92f6-2b3ac1821a41)

## Teste pylint
[cuprins](#cuprins)
- **pylint** este un pachet python folosit pentru testarea calitatii codului (spatii, nume variabile, etc).
- in cazul de fata, problemele returnate de pylint sunt afisate si nu sunt considerate erori.


# Containerizare
[cuprins](#cuprins)
S-a realizat in Docker cu succes.
Fisierul Dockerfileva fi folosit in enviromentul virtual din venv.
Fisierul ne specifica imaginea de baza, va instala frameworkul flask si pytest, ne defineste directorul de lucru /app , ne copiaza fisierul aplicatiei intr-o imagine docker, ne defineste urmatoarea environment variable FLASK_APP care reprezinta aplicatia in sine, ne precizeaza portul containerului si in final ne executa comanda in terminal pentru a ne porni aplicatia.

Imagini Containerizare:
Activate venv si vizualizare imagini docker:

![imagini_docker](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/442b48af-ec7b-4ed7-99c3-88103be1636e)

Creearea imaginii:

![imagine_creeeare](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/bb4b4a9c-b3ef-4d59-b404-cd11ec81bf1e)

Rulare container:

![Aplicatie_container](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/ea193391-6dee-454a-b3d3-5af6babf1e8e)

#DevOps CI
[cuprins](#cuprins)
CI=continuous integration
Pipeline-ul Jenkins automatizeaza procesul de build, test si deploy pentru o aplicatie. Jenkinsfile este un script care ne defineste pipeline-ul Jenkins.

# Bibliografie 
[cuprins](#cuprins)
https://youtu.be/fS_spm79C5E

https://www.britannica.com/plant/ackee

