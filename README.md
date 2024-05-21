# Curs_VCGJ_2024_fructe

# Cuprins

1. [Introducere](#introducere)
1. [Instalarea și funcționarea mașinii virtuale](#instalarea-și-funcționarea-mașinii-virtuale)
1. [Configurarea mediului de lucru](#configurarea-mediului-de-lucru)
   1. [Instalarea header-elor necesare pentru Linux](#instalarea-header-elor-necesare-pentru-linux)
   1. [Instalarea și verificarea Docker](#instalarea-și-verificarea-docker)
   1. [Crearea și configurarea Dockerfile](#crearea-și-configurarea-dockerfile)
   1. [Crearea și vizualizarea imaginii Docker](#crearea-și-vizualizarea-imaginii-docker)
   1. [Verificarea și instalarea Java](#verificarea-și-instalarea-java)
   1. [Instalarea și configurarea Jenkins](#instalarea-și-configurarea-jenkins)
   1. [Gestionarea aplicației cu Jenkins](#gestionarea-aplicației-cu-jenkins)
   1. [Crearea și configurarea Jenkinsfile](#crearea-și-configurarea-jenkinsfile)
   1. [Configurarea pipeline-ului Jenkins](#configurarea-pipeline-ului-jenkins)
   1. [Instalarea și utilizarea plugin-urilor Jenkins](#instalarea-și-utilizarea-plugin-urilor-jenkins)
   1. [Instalarea Git și Gedit](#instalarea-git-și-gedit)
   1. [Actualizarea sistemului](#actualizarea-sistemului)
   1. [Clonare repository GitHub](#clonare-repository-github)
   1. [Structură repository git local](#structură-repository-git-local)
   1. [Instalarea și utilizarea Python și a mediului virtual](#instalarea-și-utilizarea-python-și-a-mediului-virtual)
   1. [Instalarea pachetelor necesare](#instalarea-pachetelor-necesare)
   1. [Verificarea pachetelor instalate](#verificarea-pachetelor-instalate)
1. [Editarea și executarea scripturilor](#editarea-și-executarea-scripturilor)
1. [Testarea aplicației](#testarea-aplicației)
   1. [Testarea manuală a aplicației folosind Pytest](#testarea-manuală-a-aplicației-folosind-pytest)
   1. [Verificarea și îmbunătățirea codului cu Pylint](#verificarea-și-îmbunătățirea-codului-cu-pylint)
1. [Importul bibliotecii utilizate în Python](#importul-bibliotecii-utilizate-în-python)
1. [Rularea aplicației](#rularea-aplicației)
   1. [Rularea aplicației local](#rularea-aplicației-local)
   1. [Rularea aplicației cu Docker](#rularea-aplicației-cu-docker)
   1. [Vizualizarea și gestionarea containerelor Docker](#vizualizarea-și-gestionarea-containerelor-docker)
1. [Implementarea aplicației în GitHub](#implementarea-aplicației-în-github)
   1. [Sincronizare repository local cu cel remote](#sincronizare-repository-local-cu-cel-remote)
   1. [Sincronizare repository remote între branch-uri](#sincronizare-repository-remote-între-branch-uri)
   1. [Actualizare repository local](#actualizare-repository-local)
1. [Implementarea și testarea aplicației în Jenkins](#implementarea-și-testarea-aplicației-în-jenkins)
    1. [Descrierea Jenkins](#descrierea-jenkins)
    1. [Vizualizare pipeline cu Open Blue Ocean](#vizualizare-pipeline-cu-open-blue-ocean)
    1. [Actualizarea imaginilor Docker](#actualizarea-imaginilor-docker)
1. [Bibliografie](#bibliografie)

# Introducere

Proiectul de față își propune să demonstreze procesul de configurare și implementare a unei aplicații web folosind o mașină virtuală. Prin acest proiect, vom trece prin pașii necesari pentru instalarea și configurarea diverselor unelte software esențiale pentru dezvoltarea unei aplicații web, subliniind importanța fiecărei componente în parte.

# Instalarea și funcționarea mașinii virtuale

Am început prin instalarea unei mașini virtuale pe un sistem de operare Windows, un mediu izolat care ne permite să experimentăm și să configurăm aplicațiile fără a afecta sistemul principal. După ce am verificat funcționarea corectă a mașinii virtuale, următorul pas a fost deschiderea unui terminal pentru a instala header-ele necesare pentru Linux. Acestea sunt esențiale pentru a asigura compatibilitatea și funcționarea corectă a sistemului de operare.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Instalare%20VM/Screenshot%202024-05-20%20135903.png)

Am verificat. Mașina virtuală este funcțională.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Instalare%20VM/Screenshot%20from%202024-05-20%2015-21-50.png)

# Configurarea mediului de lucru

# Instalarea header-elor necesare pentru Linux

După ce am finalizat etapa de funcționare a mașinii virtuale trebuie să ne asigurăm că avem toate tool-urile necesare în proiect. Pentru început deschidem un terminal în mașina virtuală pentru a instala header-ele necesare pentru Linux. Acestea sunt esențiale pentru a asigura compatibilitatea și funcționarea corectă a sistemului de operare.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-18-08.png)

# Instalarea și verificarea Docker

Verificăm dacă avem instalat Docker pe Ubuntu. Figura de mai jos ilustrează deja că sistemul de operare are instalat Docker.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2018-00-37.png)

# Crearea și configurarea Dockerfile

După ce am verificat că Docker a fost instalat se creează fișierul Dockerfile care are conținutul de mai jos:
![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2017-52-08.png)

Se salvează fișierul în directorul principal.

# Crearea și vizualizarea imaginii Docker

Se execută comanda de mai jos:

* docker build -t curs_vcgj_2024_fructe:v01 .
  
  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-16%2012-17-41.png)

Se vizualizează imaginea creată cu comanda:

* docker images

  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_cu_container/Screenshot%20from%202024-05-16%2012-18-10.png)

Avem imaginea curs_vcgj_2024_fructe, în care se creează mediul virtual numit venv. Se instalează pachetele necesare aplicației și se implementează codul aplicației, conform Dockerfile.

# Verificarea și instalarea Java

Verificăm acum că Java e instalat pe sistemul nostru de operare.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2010-02-38.png)

Funcționarea Jenkins depinde de Java datorită naturii sale ca aplicație Java, beneficiind de portabilitatea, performanța și securitatea oferite de platforma Java.

# Instalarea și configurarea Jenkins

Verificăm dacă avem instalat Jenkins pe Ubuntu. Figura de mai jos ilustrează deja că sistemul de operare are instalat Jenkins.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2021-24-07.png)

Pentru a rula Jenkins introducem în terminal comanda din imagine:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_jenkins/Screenshot%20from%202024-05-16%2013-33-19.png)

După cum se poate observa din imagine Jenkins rulează ca aplicație și nu ca server. Pentru a face ca Jenkins să ruleze doar din comanda "jenkins", după instalare trebuie să oprim și să dezactivăm serviciul din comenzile de mai jos:
* sudo systemctl stop jenkins
* sudo systemctl disable jenkins

# Gestionarea aplicației cu Jenkins

Se deschide interfața web a aplicației așa cum este prezentată în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2021-48-02.png)

În imaginea următoare se poate vedea structura folder-ului Curs_VCGJ_2024_fructe:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2002-02-40.png)

# Crearea și configurarea Jenkinsfile

Fișierul Jenkins are conținutul din imagine:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2022-24-53.png)

# Configurarea pipeline-ului Jenkins

Configurarea pipeline-ului Jenkins este ilustrată în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2021-47-34.png)

După cum se poate observa se dorește să se testeze codul din Jenkinsfile, utilizând link-ul de pe Github, iar la branch a fost setat branch-ul devel_[nume_branch].

# Instalarea și utilizarea plugin-urilor Jenkins

În pagina următoare vizualizam testele care s-au creat în urma execuției pipeline-ului. Plugin-urile care au fost utilizate sunt următoarele:

* Open Blue Ocean
* Stage View

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2002-02-27.png)

Dacă plugin-urile Open Blue Ocean și Stage View nu sunt instalate pe server-ul nostru Jenkins pot fi instalate manual, utilizând interfața web a aplicației Jenkins.

Dacă accesăm plugin-ul Open Blue Ocean putem vizualiza testele care s-au realizat asupra aplicației noastre:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2002-02-16.png)

# Instalarea Git și Gedit
  
Instalarea Git și a editorului de text Gedit este esențială pentru gestionarea codului sursă și efectuarea modificărilor necesare pentru tema aleasă. Git ne permite să urmărim schimbările și să colaborăm eficient într-un mediu remote, în timp ce Gedit oferă un mediu de editare simplu și eficient, adecvat lucrului local. Prima imagine ilustrează instalarea cu succes a utilitarului Git pe Ubuntu, iar în cea de-a doua imagine se confirmă faptul că programul de editare Gedit a fost instalat corect.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-30-05.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-30-22.png)

# Actualizarea sistemului

Pentru a actualiza sistemul cu noile pachete instalate vom utiliza comanda:

* sudo apt update

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-34-14.png)

# Clonare repository GitHub

Pentru a avea acces la modificarea fisierelor necesare utilizării aplicației în mediul local trebuie să obținem o clonă a fișierului din linkul de github. Se copiază link-ul din imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2019-06-23.png)

După ce link-ul a fost copiat el trebuie introdus în terminal cu comanda:

* git clone <url_repository>

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-43-36.png)

# Structură repository git local

Structura folder-ului Curs_VCGJ_2024_fructe este descrisă în figura următoare:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2023-53-24.png)

Dacă utilizarea comenzii "tree" nu este recunoscută de sistemul de operare atunci este necesară instalarea acesteia cu comanda:

* sudo apt install tree

În exemplul de mai jos comanda "tree" este deja instalată:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2000-00-46.png)

# Instalarea și utilizarea Python și a mediului virtual

Verificăm dacă avem instalat Python pe sistemul nostru de operare, în cazul nostru, Linux. Figura de mai jos ilustrează deja că sistemul de operare are instalat Python pentru a rula cu succes fișierele care au extensia .py.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-49-11.png)

Pentru a putea vedea dacă în directorul de lucru există fișiere cu extensia .py vom utiliza comanda:

* ls -l

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-52-30.png)

# Instalarea pachetelor necesare

După ce am instalat Python, următorul pas este să instalăm pachetele necesare pentru proiectul nostru. Aceste pachete pot include biblioteci și framework-uri specifice pentru dezvoltarea aplicației noastre.

* Flask
* Pytest
* Pylint

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2016-09-02.png)

Înainte de a instala framework-urile de python este important să lucrăm într-un mediu virtual. Dacă nu avem instalat un mediu de lucru virtual putem folosi comanda:

*  python3 -m venv .venv

După ce am instalat mediul virtual, este necesară activarea "venv" pentru a facilita utilizarea lui în proiectul nostru. O altă metodă de a instala mult mai simplu framework-urile de python putem crea un fișier text pe care îl salvăm în aceeași locație cu aplicația noastră, în care vor fi incluse numele pachetelor pe care dorim să le instalăm pe calculatorul nostru personal. Comanda pentru a instala aceste pachete este mai jos:

* pip install -r quickrequirements.txt

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2016-02-49.png)

Conținutul fișierului quickrequirements.txt este ilustrat în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2017-19-36.png)

# Verificarea pachetelor instalate

Pentru a afișa pachetele deja instalate vom utiliza comanda:

* pip freeze

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2016-10-36.png)

# Editarea și executarea scripturilor

În mod alternativ, putem scrie scripturi care să conțină comenzile necesare pentru a rula aplicația.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2016-54-16.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2016-55-02.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2016-55-36.png)

Dacă dorim să modificăm conținutul din fișierele deja create vom utiliza utilitarul Gedit.

După ce am instalat utilitarul Gedit îl putem utiliza din terminal cu comanda gedit <nume_fisier>:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2001-24-28.png)

Se pot scrie scripturi, utilizând terminalul din Linux cu vim. Poate fi instalat cu comanda:

* sudo apt install vim

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2000-24-21.png)

Astfel, fisierul pe care dorim să îl modificăm poate fi editat și din terminal cu comanda:

* vim <nume_fisier>

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2000-22-13.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2001-25-41.png)

Pentru a închide fereastra vim se va utiliza comanda după caz:

* :q - se iese din programul vim fără modificarea fișierului corespunzător
* :wq - se iese din programul vim după ce s-au efectuat modificări în fișierul corespunzător

# Testarea aplicației

# Testarea manuală a aplicației folosind Pytest

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

Mai departe sunt prezentate modalitățile prin care vom rula aplicația web:

# Rularea aplicației local
Pentru a rula aplicația local sunt necesare următoarele condiții: activarea mediului virtual care ne va ajuta să rulăm aplicația fără erori și utilizarea comenzilor de mai jos, în ordinea în care sunt scrise:
* export FLASK_APP=<nume_aplicatie>
* flask --app <nume_fisier.py> --debug run

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-17%2009-22-35.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-17%2009-23-37.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-17%2009-23-54.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-17%2009-24-06.png)

Alte modalitati prin care putem rula local aplicatia sunt prezentate mai jos:

* utilizare scripturi
  
  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-20%2017-28-33.png)

  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-16%2012-01-41.png)

  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-16%2012-02-10.png)

  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-16%2012-02-21.png)

  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-16%2012-02-30.png)
  
* comanda python3 <nume_fisier.py>

  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-16%2012-06-06.png)
  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-16%2012-06-14.png)
  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-16%2012-06-21.png)
  ![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Rulare_aplicatie_local/Screenshot%20from%202024-05-16%2012-06-29.png)

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

# Vizualizarea și gestionarea containerelor Docker

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

# Implementarea aplicației în GitHub
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

# Implementarea și testarea aplicației în Jenkins

# Descrierea Jenkins

Jenkins este un server de automatizare open-source care ne ajută să automatizăm diverse sarcini legate de dezvoltarea software, cum ar fi construirea, testarea și implementarea aplicației. Utilizarea Jenkins ne permite să economisim timp și să reducem erorile umane în procesul de dezvoltare.

Cum funcționează Jenkins?
Jenkins utilizează job-uri și pipeline-uri. Un job reprezintă o sarcină individuală de automatizare. Fiecare job poate reprezenta un proces de construcție, testare sau implementare a unui proiect software. Un pipeline este o suită de joburi care sunt interconectate și configurează procesul complet de livrare a software-ului. Jenkins poate extrage codul sursă din diverse sisteme de control al versiunilor (cum ar fi Git). După ce codul este extras, Jenkins execută scripturile de construcție (de exemplu, Gradle) pentru a compila codul. După compilare, Jenkins rulează testele automate pentru a verifica dacă noul cod nu introduce erori.

Care sunt avantajele utilizării Jenkins?
* automatizare completă: automatizează procesele repetitive, economisind timp și reducând erorile umane.
* integrare ușoară: se integrează cu numeroase instrumente și tehnologii utilizate în dezvoltarea software.
* scalabilitate: poate fi extins cu ajutorul plugin-urilor pentru a îndeplini cerințe specifice proiectului.
* monitorizare și raportare: oferă vizibilitate completă asupra stării proiectelor prin rapoarte detaliate și notificări în timp real.

# Vizualizare pipeline cu Open Blue Ocean

Mai jos este ilustrat un pipeline Jenkins care a trecut toate testele:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2002-01-20.png)

# Actualizarea imaginilor Docker

În urma execuției pipeline-ului putem vizualiza în imaginea de mai jos că s-a creat un nou container Docker cu tag-ul v57.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2002-07-34.png)

# Bibliografie
* [VirtualBox](https://www.virtualbox.org/wiki/Documentation)
* [Instalare VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Instalare Ubuntu 22.04](https://releases.ubuntu.com/jammy/)
* [Instalare Python](https://www.python.org/downloads/)
* [Docker](https://docs.docker.com/docker-hub/)
* [Instalare Docker](https://docs.docker.com/engine/install/ubuntu/)
* [Git](https://github.com)
* [Instalare Java](https://www.jenkins.io/doc/book/installing/linux/#installation-of-java)
* [Jenkins](https://www.jenkins.io/doc/)
* [Instalare Jenkins](https://www.jenkins.io/doc/book/installing/linux/)
* [sysinfo](https://github.com/crchende/sysinfo/)
* [sysinfo](https://github.com/crchende/sysinfo/blob/avansat_main/doc/dockerdoc.md)
* [jenkinsdemo](https://github.com/crchende/jenkinsdemo?tab=readme-ov-file#instalare-jenkins)
