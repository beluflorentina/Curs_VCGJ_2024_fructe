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

Aplicatia in functiune si cateva explicatii cod poate? + screen??

In directorul /app avvem fisierul principal al aplicatiei, 443_fructe.py.
Acesta contine 4 rute, prima ruta "/" ofera posibilatea de a alege un fruct sa fie vizualizat, a doua ruta "/ackee" ofera informatii despre fruct. Din a doua ruta putem accesa pagina "/" si rutele "/ackee/culoare" si "/ackee/descriere" care se folosesc de functii definite in fisierul biblioteca_fructe.py pentru a afisa informatiile dorite.

In directorul /app/lib este fisierul biblioteca_fructe.py. Acesta contine finctiile apelate in 433_fructe.py: culaore_ackee() si descriere_ackee(). Prima functie cand e apelata ne va intaorce un text care contine descrierea culorii fructului, a doua functie cand apelata ne va intoarce un text care contine descriere a fructului.

Aplicatia:


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


##Teste Jenkins

Pipelineul in Jenkins a fost definit in fisierul Jenkinsfile in care avem definite stagiile urmatoare:
Build, care ne creeaza enviromnetul de testare prin activarea mediului venv si instalarea biblitecilor necesare prin executarea de comenzi;
pylint -calitate cod, este un stagiu in care este verificata calitatea codului dar si verifica daca venv a fost activat;
Unit testing, este stagiul in care testam functiile din biblioteca_fructe cu ajutorul fisierului test_lib.py si comenzilor folosite;
Deploy este stagiul care testeaza containerizarea aplicatiei prin crearea unei imagini docker si crearea containerului respectiv.

S-a testat cu Jenkins si am obtinut astfel:


#Integrare

Se asteapta review pentru integrare in main.

#Containerizare

S-a realizat in Docker cu succes.
Fisierul Dockerfileva fi folosit in enviromentul virtual din venv.
Fisierul ne specifica imaginea de baza, va instala frameworkul flask si pytest, ne defineste directorul de lucru /app , ne copiaza fisierul aplicatiei intr-o imagine docker, ne defineste urmatoarea environment variable FLASK_APP care reprezinta aplicatia in sine, ne precizeaza portul containerului si in final ne executa comanda in terminal pentru a ne porni aplicatia.

Imagini Containerizare:

#ID pullrequesturi

ID pull requesturi si reviewul acestora (ca o lista sau linkuri)???

#Bibliografie 

https://youtu.be/fS_spm79C5E
https://www.britannica.com/plant/ackee

