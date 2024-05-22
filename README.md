# Curs_VCGJ_2024_fructe

# Cuprins

1. [Introducere](#introducere)
1. [Instalarea și funcționarea mașinii virtuale](#instalarea-și-funcționarea-mașinii-virtuale)
1. [Configurarea mediului de lucru](#configurarea-mediului-de-lucru)
   1. [Instalare headere necesare pentru Linux](#instalare-headere-necesare-pentru-linux)
   1. [Tool-urile necesare pentru aplicație](#tool-urile-necesare-pentru-aplicație)
   1. [Actualizarea sistemului](#actualizarea-sistemului)
   1. [Clonare repository GitHub](#clonare-repository-github)
1. [Testarea aplicației](#testarea-aplicației)
   1. [Testarea manuală a aplicației cu Pytest](#testarea-manuală-a-aplicației-cu-pytest)
   1. [Verificarea și îmbunătățirea codului cu Pylint](#verificarea-și-îmbunătățirea-codului-cu-pylint)
1. [Importul bibliotecii utilizate în Python](#importul-bibliotecii-utilizate-în-python)
1. [Rularea aplicației](#rularea-aplicației)
   1. [Rularea aplicației local](#rularea-aplicației-local)
   1. [Rularea aplicației cu Docker](#rularea-aplicației-cu-docker)
1. [Încărcarea aplicației pe GitHub](#încărcarea-aplicației-pe-github)
   1. [Sincronizare repository local cu cel remote](#sincronizare-repository-local-cu-cel-remote)
   1. [Sincronizare repository remote între branch-uri](#sincronizare-repository-remote-între-branch-uri)
   1. [Actualizare repository local](#actualizare-repository-local)
1. [Testarea aplicației cu Jenkins](#testarea-aplicației-cu-jenkins)
    1. [Descriere Jenkins](#descriere-jenkins)
    1. [Vizualizare pipeline cu Blue Ocean](#vizualizare-pipeline-cu-blue-ocean)
    1. [Crearea unui container Docker în etapa de Deploy](#crearea-unui-container-docker-în-etapa-de-Deploy)
1. [Bibliografie](#bibliografie)

# Introducere

Proiectul de față își propune să demonstreze procesul de configurare și implementare a unei aplicații web folosind o mașină virtuală. Prin acest proiect, vom trece prin pașii necesari pentru instalarea și configurarea diverselor unelte software esențiale pentru dezvoltarea unei aplicații web, subliniind importanța fiecărei componente în parte.

# Instalarea și funcționarea mașinii virtuale

Am început prin instalarea unei mașini virtuale pe un sistem de operare Windows, un mediu izolat care ne permite să experimentăm și să configurăm aplicațiile fără a afecta sistemul principal. După ce am verificat funcționarea corectă a mașinii virtuale, următorul pas a fost deschiderea unui terminal pentru a instala header-ele necesare pentru Linux. Acestea sunt esențiale pentru a asigura compatibilitatea și funcționarea corectă a sistemului de operare.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Instalare%20VM/Screenshot%202024-05-20%20135903.png)

Am verificat. Mașina virtuală este funcțională.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Instalare%20VM/Screenshot%20from%202024-05-20%2015-21-50.png)

# Configurarea mediului de lucru

# Instalare headere necesare pentru Linux

După ce am finalizat etapa de funcționare a mașinii virtuale trebuie să ne asigurăm că avem toate tool-urile necesare în proiect. Pentru început deschidem un terminal în mașina virtuală pentru a instala header-ele necesare pentru Linux. Acestea sunt esențiale pentru a asigura compatibilitatea și funcționarea corectă a sistemului de operare.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-18-08.png)

# Tool-urile necesare pentru aplicație

Verificăm dacă avem instalat Docker pe Ubuntu. Figura de mai jos ilustrează deja că sistemul de operare are instalat Docker.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2018-00-37.png)

După ce am verificat că Docker a fost instalat se creează fișierul Dockerfile care are conținutul de mai jos:
![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2017-52-08.png)

Se salvează fișierul în directorul principal.

Se execută comanda de mai jos:

* docker build -t curs_vcgj_2024_fructe:v01 .
  
  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-16%2012-17-41.png)

Se vizualizează imaginea creată cu comanda:

* docker images

  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-16%2012-18-10.png)

Avem imaginea curs_vcgj_2024_fructe, în care se creează mediul virtual numit venv. Se instalează pachetele necesare aplicației și se implementează codul aplicației, conform Dockerfile.

Instalarea Git și a editorului de text Gedit este esențială pentru gestionarea codului sursă și efectuarea modificărilor necesare pentru tema aleasă. Git ne permite să urmărim schimbările și să colaborăm eficient într-un mediu remote, în timp ce Gedit oferă un mediu de editare simplu și eficient, adecvat lucrului local. Prima imagine ilustrează instalarea cu succes a utilitarului Git pe Ubuntu, iar în cea de-a doua imagine se confirmă faptul că programul de editare Gedit a fost instalat corect.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-30-05.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-30-22.png)

Dacă dorim să modificăm conținutul din fișierele deja create putem utiliza comanda gedit <nume_fisier>:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2001-24-28.png)

Verificăm dacă avem instalat Python pe sistemul nostru de operare, în cazul nostru, Linux. Figura de mai jos ilustrează deja că sistemul de operare are instalat Python pentru a rula cu succes fișierele care au extensia .py.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-49-11.png)

Pentru a putea vedea dacă în directorul de lucru există fișiere cu extensia .py vom utiliza comanda:

* ls -l

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-52-30.png)

După ce am instalat Python, următorul pas este să instalăm pachetele necesare pentru proiectul nostru. Aceste pachete pot include biblioteci și framework-uri specifice pentru dezvoltarea aplicației noastre.

* Flask
* Pytest
* Pylint

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2016-09-02.png)

Pentru a afișa pachetele deja instalate vom utiliza comanda:

* pip freeze

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2016-10-36.png)

Pentru a instala "venv" vom folosi comanda:

*  python3 -m venv .venv

După ce am instalat mediul virtual, este necesară activarea "venv" pentru a facilita utilizarea lui în proiectul nostru. Vom utiliza comanda:

* . .venv/bin/activate

Verificăm acum dacă Java este instalat pe sistemul nostru de operare.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2010-02-38.png)

Funcționarea Jenkins depinde de Java datorită naturii sale ca aplicație Java, beneficiind de portabilitatea, performanța și securitatea oferite de platforma Java.

Verificăm dacă avem instalat Jenkins pe Ubuntu. Figura de mai jos ilustrează deja că sistemul de operare are instalat Jenkins.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2021-24-07.png)

Pentru a rula Jenkins introducem în terminal comanda din imagine:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_jenkins/Screenshot%20from%202024-05-16%2013-33-19.png)

După cum se poate observa din imagine Jenkins rulează ca aplicație și nu ca server. Pentru a face ca Jenkins să ruleze doar din comanda "jenkins", după instalare trebuie să oprim și să dezactivăm serviciul din comenzile de mai jos:
* sudo systemctl stop jenkins
* sudo systemctl disable jenkins

Se deschide interfața web a aplicației așa cum este prezentată în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2021-48-02.png)

Configurarea pipeline-ului Jenkins este ilustrată în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2021-47-34.png)

În pagina următoare se vizualizează testele care s-au efectuat în urma executării pipeline-ului. Plugin-urile care au fost utilizate sunt următoarele:

* Blue Ocean
* Stage View

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_jenkins/Screenshot%20from%202024-05-21%2020-01-05.png)

Dacă plugin-urile Blue Ocean și Stage View nu sunt instalate pe Jenkins pot fi instalate manual, utilizând interfața web a aplicației Jenkins.

Dacă accesăm plugin-ul Blue Ocean se afișează toate testele care s-au efectuat asupra aplicației:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_jenkins/Screenshot%20from%202024-05-21%2020-01-19.png)

# Actualizarea sistemului

Pentru a actualiza sistemul cu noile pachete instalate vom utiliza comanda:

* sudo apt update

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-34-14.png)

# Clonare repository GitHub

Pentru a avea acces la modificarea fisierelor necesare utilizării aplicației în mediul local trebuie să clonăm repository-ul de pe Github. Se copiază link-ul din imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-22%2010-31-11.png)

După ce link-ul a fost copiat el trebuie introdus în terminal cu comanda:

* git clone <url_repository>

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-43-36.png)

# Testarea aplicației

# Testarea manuală a aplicației cu Pytest

Pentru a testa manual aplicatia vom utiliza comanda:

* python3 -m pytest -v

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2016-17-19.png)

Conținutul pe care trebuie să îl aibă fișierul de testare este ilustrat în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2017-12-56.png)

# Verificarea și îmbunătățirea codului cu Pylint

Pylint ne ajută să îmbunătățim codul aplicației prin detectarea erorilor ca în figura de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2001-18-04.png)

Comanda este:

* python3 -m pylint 443_fructe.py

# Importul bibliotecii utilizate în Python

Biblioteca utilizată este definită după următorii parametri:
* culoare
* descriere

Modul de utilizare al parametrilor "culoare" și "descriere" este ilustrat în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2017-06-06.png)

Scriptul din imagine este util în realizarea importului bibliotecii fructe în fișierul 443_fructe.py.

# Rularea aplicației

# Rularea aplicației local
Pentru a rula aplicația local sunt necesare următoarele condiții: activarea mediului virtual care ne va ajuta să rulăm aplicația fără erori și utilizarea comenzilor de mai jos, în ordinea în care sunt scrise:
* export FLASK_APP=<nume_aplicatie>
* flask --app <nume_fisier.py> --debug run

Pentru a verifica funcționarea corectă a aplicației deschidem un browser web și accesăm adresa URL corespunzătoare. Link-urile către pagini pot fi accesate prin:
* ruta standard: http://127.0.0.1:5000
* rutele aplicației web:
  * fructe: http://127.0.0.1:5000/durian
  * culoare: http://127.0.0.1:5000/durian/culoare
  * descriere: http://127.0.0.1:5000/durian/descriere

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-17%2009-24-06.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-17%2009-22-35.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-17%2009-23-37.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-17%2009-23-54.png)

# Rularea aplicației cu Docker
Pentru a rula aplicația cu Docker vom executa comanda de mai jos:

* docker run --name curs_vcgj -p 8020:5000 curs_vcgj:v01

  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-16%2012-21-21.png)

  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-16%2012-21-32.png)

  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-16%2012-21-45.png)

  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-16%2012-21-56.png)

Aceasta va crea containerul și va porni execuția acestuia.

Portul pe calculator unde va răspunde serverul din docker este 8020.

Portul în interiorul containerului este 5000.

Pentru a vizualiza containerele care rulează vom utiliza comenzile de mai jos:
* docker ps
* docker ps -a

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-16%2012-22-49.png)

Pentru a opri execuția containerului vom utiliza comanda:

* docker stop <nume_container>

Pentru a porni execuția containerului vom utiliza comanda:

* docker start <nume_container>

Pentru a vizualiza mesajele generate de aplicația din container în consolă vom atașa containerul utilizând comanda:

* docker container attach <nume_container>

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-20%2018-43-47.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-20%2018-44-00.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-20%2018-44-09.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-20%2018-44-25.png)

# Încărcarea aplicației pe GitHub
După ce am testat aplicația local următoarea etapă este încărcarea aplicației pe Github. În imaginile de mai jos putem observa procesul prin care proiectul nostru de Github este trimis din repository-ul local într-un repository remote.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2012-47-07.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2012-58-33.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-14-35.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-16-04.png)

# Sincronizare repository local cu cel remote

După cum s-a observat modificările din repository-ul local au fost aduse pe Github pe branch-ul pe care l-am selectat înainte de a folosi comanda:

* git push

# Sincronizare repository remote între branch-uri

Pentru a sincroniza branch-urile main_[nume_branch] și devel_[nume_branch] se urmărește modalitatea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-18-51.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-20-17.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-21-44.png)

În final, putem vizualiza acum că branch-ul main_[nume_branch] a fost actualizat cu modificările din devel_[nume_branch] după ce am realizat "merge" din devel_[nume_branch] în main_[nume_branch] pe repository-ul remote.

# Actualizare repository local

Pentru a actualiza acum repository-ul local după ce am modificat în branch-urile prezentate vom executa în terminal comanda:

* git pull

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-17%2010-08-14.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-30-50.png)

Mai jos sunt ilustrate modificările apărute în urma editării fișierului aplicației.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-28-40.png)

# Testarea aplicației cu Jenkins

# Descriere Jenkins

Jenkins este un server de automatizare open-source care ne ajută să automatizăm diverse sarcini legate de dezvoltarea software, cum ar fi construirea, testarea și implementarea aplicației. Utilizarea Jenkins ne permite să economisim timp și să reducem erorile umane în procesul de dezvoltare.

Cum funcționează Jenkins?
Jenkins utilizează job-uri și pipeline-uri. Un job reprezintă o sarcină individuală de automatizare. Fiecare job poate reprezenta un proces de construcție, testare sau implementare a unui proiect software. Un pipeline este o suită de joburi care sunt interconectate și configurează procesul complet de livrare a software-ului. Jenkins poate extrage codul sursă din diverse sisteme de control al versiunilor (cum ar fi Git). După ce codul este extras, Jenkins execută scripturile de construcție (de exemplu, Gradle) pentru a compila codul. După compilare, Jenkins rulează testele automate pentru a verifica dacă noul cod nu introduce erori.

Care sunt avantajele utilizării Jenkins?
* automatizare completă: automatizează procesele repetitive, economisind timp și reducând erorile umane.
* integrare ușoară: se integrează cu numeroase instrumente și tehnologii utilizate în dezvoltarea software.
* scalabilitate: poate fi extins cu ajutorul plugin-urilor pentru a îndeplini cerințe specifice proiectului.
* monitorizare și raportare: oferă vizibilitate completă asupra stării proiectelor prin rapoarte detaliate și notificări în timp real.

# Vizualizare pipeline cu Blue Ocean

Mai jos este ilustrat un pipeline care a trecut testul cu Jenkins.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_jenkins/Screenshot%20from%202024-05-21%2020-52-44.png)

# Crearea unui container Docker în etapa de Deploy

După ce am rulat pipeline-ul în Jenkins putem vizualiza în imaginea de mai jos că s-a creat un container cu tag-ul v58.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-21%2020-02-16.png)

# Bibliografie
* [VirtualBox](https://www.virtualbox.org/wiki/Documentation)
* [Instalare VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Instalare Ubuntu 22.04](https://releases.ubuntu.com/jammy/)
* [Python](https://www.python.org/)
* [Instalare Python](https://www.python.org/downloads/)
* [Docker](https://docs.docker.com/docker-hub/)
* [Instalare Docker](https://docs.docker.com/engine/install/ubuntu/)
* [Git](https://github.com)
* [Instalare Java](https://www.jenkins.io/doc/book/installing/linux/#installation-of-java)
* [Jenkins](https://www.jenkins.io/doc/)
* [Instalare Jenkins](https://www.jenkins.io/doc/book/installing/linux/)
* [sysinfo](https://github.com/crchende/sysinfo/tree/main)
* [sysinfo](https://github.com/crchende/sysinfo/blob/avansat_main/doc/dockerdoc.md)
* [jenkinsdemo](https://github.com/crchende/jenkinsdemo?tab=readme-ov-file#instalare-jenkins)
