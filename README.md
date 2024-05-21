`Curs_VCGJ_2024_fructe`
=======================

#Cuprins
1. [Descriere aplicatie] (#descriere-aplicatie)
1. [Functionalitate adaugata] (#functionalitate-adaugata)
1. [Stadiu] (#stadiu)
1. [Teste] (#teste)
   1. [Teste manuale] (#teste-manuale)
   1. [Teste Jenkins] (#teste-jenkins)
1. [Integrare] (#integrare)
1. [Containerizare] (#containerizare)
1. [ID pull requesturi] (#id-pull-requesturi)
1. [Bibliografie] (#bibliografie)

#Descriere aplicatie

Aplicatia reprezinta un site web care se bazeaza pe frameworkul Flask.
Aplicatia afiseaza detalii despre fructul ackee, detalii cum ar fi culoarea si descrierea fructului.
Aplicatia este simpla,aceasta are ca pagina principala o pagina de index unde putem accesa pagina fructului sau a altor fructe daca exista sau dorim.
Paginile fructului (culoare, descriere) sunt definite in functiile din interiorul fisierului app/lib/biblioteca_fructe.py

Aplicatia include suport pentru containerizare in fisierul Dockerfile din directorul principal al aplicatiei.
Pipeline-ul pentru Jenkins este definit in fisierul Jenkinsfile.

#Funcitionalitate adaugata

In directorul /app avvem fisierul principal al aplicatiei, 443_fructe.py.
Acesta contine 4 rute, prima ruta "/" ofera posibilatea de a alege un fruct sa fie vizualizat, a doua ruta "/ackee" ofera informatii despre fruct. Din a doua ruta putem accesa pagina "/" si rutele "/ackee/culoare" si "/ackee/descriere" care se folosesc de functii definite in fisierul biblioteca_fructe.py pentru a afisa informatiile dorite.

In directorul /app/lib este fisierul biblioteca_fructe.py. Acesta contine finctiile apelate in 433_fructe.py: culaore_ackee() si descriere_ackee(). Prima functie cand e apelata ne va intaorce un text care contine descrierea culorii fructului, a doua functie cand apelata ne va intoarce un text care contine descriere a fructului.

Aplicatia:

![imagine](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/435d388f-ada9-4732-b0b8-209f2aab4bbc)

#Stadiu

Codul a fost adaugat in main_Burlacel_George dar nu in main.

#Teste

##Teste manuale

Testarea manuala se bazeaza pe fisierul test_lib.py din directorul app/test, acesta verifica daca anumite segmente de text sunt prezente in pagina, acest fapt ne semnifica ca metodele sunt corecte, alt test este 
Testarea manuala si containerizarea s-a efectuat in venv.
Initial trebuie sa initializam mediul virtual venv, python3 -m venv .venv.
Comanda . .venv/bin/activate va activa mediul virtual.
Trebuie sa instalam pachetele necesare pentru proiect:
pip install flask
pip install pytest
pip install pylint

Test pytest si rularea aplicatie din flask:
![imagine_test_manual](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/81457568-4ebb-4eb4-87d9-7c3dead4d6b4)


##Teste Jenkins

Pipelineul in Jenkins a fost definit in fisierul Jenkinsfile in care avem definite stagiile urmatoare:
Build, care ne creeaza enviromnetul de testare prin activarea mediului venv si instalarea biblitecilor necesare prin executarea de comenzi;
pylint -calitate cod, este un stagiu in care este verificata calitatea codului dar si verifica daca venv a fost activat;
Unit testing, este stagiul in care testam functiile din biblioteca_fructe cu ajutorul fisierului test_lib.py si comenzilor folosite;
Deploy este stagiul care testeaza containerizarea aplicatiei prin crearea unei imagini docker si crearea containerului respectiv.

S-a testat cu Jenkins si am obtinut astfel:
Configurare Jenkins
![jenkins_config](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/7dc390fa-ac26-4ad2-b203-c87c55dfed9c)

Test Jenkins
![test_jenkins](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/4358fb89-f016-49e0-92f6-2b3ac1821a41)


#Integrare

Se asteapta review pentru integrare in main.

#Containerizare

S-a realizat in Docker cu succes.
Fisierul Dockerfileva fi folosit in enviromentul virtual din venv.
Fisierul ne specifica imaginea de baza, va instala frameworkul flask si pytest, ne defineste directorul de lucru /app , ne copiaza fisierul aplicatiei intr-o imagine docker, ne defineste urmatoarea environment variable FLASK_APP care reprezinta aplicatia in sine, ne precizeaza portul containerului si in final ne executa comanda in terminal pentru a ne porni aplicatia.

Imagini Containerizare:
Activate venv si vizualizare imagini docker:
![imagini_docker](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/442b48af-ec7b-4ed7-99c3-88103be1636e)

Creearea imaginii
![imagine_creeeare](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/bb4b4a9c-b3ef-4d59-b404-cd11ec81bf1e)

Rulare container:
![Aplicatie_container](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127586039/ea193391-6dee-454a-b3d3-5af6babf1e8e)


#ID pullrequesturi

ID pull requesturi si reviewul acestora (ca o lista sau linkuri)???

#Bibliografie 

https://youtu.be/fS_spm79C5E

https://www.britannica.com/plant/ackee

