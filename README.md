# Curs_VCGJ_2024_fructe

Proiectul de față își propune să demonstreze procesul de configurare și implementare a unei aplicații web folosind o mașină virtuală. Prin acest proiect, vom trece prin pașii necesari pentru instalarea și configurarea diverselor unelte software esențiale pentru dezvoltarea unei aplicații web, subliniind importanța fiecărei componente în parte.

Am început prin instalarea unei mașini virtuale pe un sistem de operare Windows, un mediu izolat care ne permite să experimentăm și să configurăm aplicațiile fără a afecta sistemul principal. După ce am verificat funcționarea corectă a mașinii virtuale, următorul pas a fost deschiderea unui terminal pentru a instala header-ele necesare pentru Linux. Acestea sunt esențiale pentru a asigura compatibilitatea și funcționarea corectă a sistemului de operare.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Instalare%20VM/Screenshot%202024-05-20%20135903.png)

Am verificat. Mașina virtuală este funcțională.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Instalare%20VM/Screenshot%20from%202024-05-20%2015-21-50.png)

După ce am finalizat etapa de funcționare a mașinii virtuale trebuie să ne asigurăm că avem toate tool-urile necesare în proiect. Pentru început deschidem un terminal în mașina virtuală pentru a instala header-ele necesare pentru Linux. Acestea sunt esențiale pentru a asigura compatibilitatea și funcționarea corectă a sistemului de operare.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-18-08.png)

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

Verificăm dacă avem instalat Jenkins pe Ubuntu. Figura de mai jos ilustrează deja că sistemul de operare are instalat Jenkins.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2021-24-07.png)

Pentru a rula server-ul de Jenkins introducem în terminal comanda jenkins:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_jenkins/Screenshot%20from%202024-05-16%2013-33-19.png)

Se deschide interfața web a aplicației așa cum este prezentată în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2021-48-02.png)

În imaginea următoare se poate vedea structura folder-ului Curs_VCGJ_2024_fructe:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2021-47-52.png)

Fișierul Jenkins are conținutul din imagine:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2022-24-53.png)

Configurarea pipeline-ului Jenkins este ilustrată în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2021-47-34.png)

După cum se poate observa se dorește să se testeze codul din Jenkinsfile, utilizând link-ul de pe Github, iar la branch a fost setat branch-ul devel_[nume_branch].

În pagina următoare vizualizam testele care s-au creat în urma execuției pipeline-ului. Plugin-urile care au fost utilizate sunt următoarele:

* Open Blue Ocean
* Stage View

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2021-49-38.png)

Dacă accesăm plugin-ul Open Blue Ocean putem vizualiza testele care s-au realizat asupra aplicației noastre:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2021-48-21.png)
  
Instalarea Git și a editorului de text Gedit este esențială pentru gestionarea codului sursă și efectuarea modificărilor necesare pentru tema aleasă. Git ne permite să urmărim schimbările și să colaborăm eficient într-un mediu remote, în timp ce Gedit oferă un mediu de editare simplu și eficient, adecvat lucrului local. Prima imagine ilustrează instalarea cu succes a utilitarului Git pe Ubuntu, iar în cea de-a doua imagine se confirmă faptul că programul de editare Gedit a fost instalat corect.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-30-05.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-30-22.png)

Pentru a actualiza sistemul cu noile pachete instalate vom utiliza comanda:

* sudo apt update

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-34-14.png)

Pentru a avea acces la modificarea fisierelor necesare utilizării aplicației în mediul local trebuie să obținem o clonă a fișierului din linkul de github. Se copiază link-ul din imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2019-06-23.png)

După ce link-ul a fost copiat el trebuie introdus în terminal cu comanda:

* git clone <url_repository>

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-43-36.png)

Structura folder-ului Curs_VCGJ_2024_fructe este descrisă în figura următoare:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2023-53-24.png)

Dacă utilizarea comenzii "tree" nu este recunoscută de sistemul de operare atunci este necesară instalarea acesteia cu comanda:

* sudo apt install tree

În exemplul de mai jos comanda "tree" este deja instalată:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2000-00-46.png)

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

Înainte de a instala framework-urile de python este important să lucrăm într-un mediu virtual. Dacă nu avem instalat un mediu de lucru virtual putem folosi comanda:

*  python3 -m venv .venv

După ce am instalat mediul virtual, este necesară activarea "venv" pentru a facilita utilizarea lui în proiectul nostru. O altă metodă de a instala mult mai simplu framework-urile de python putem crea un fișier text pe care îl salvăm în aceeași locație cu aplicația noastră, în care vor fi incluse numele pachetelor pe care dorim să le instalăm pe calculatorul nostru personal. Comanda pentru a instala aceste pachete este mai jos:

* pip install -r quickrequirements.txt

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2016-02-49.png)

Conținutul fișierului quickrequirements.txt este ilustrat în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2017-19-36.png)

Pentru a afișa pachetele deja instalate vom utiliza comanda:

* pip freeze

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2016-10-36.png)

În mod alternativ, putem scrie scripturi care să conțină comenzile necesare pentru a rula aplicația.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2016-54-16.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2016-55-02.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2016-55-36.png)

Dacă dorim să modificăm conținutul din fișierele deja create vom utiliza utilitarul Gedit.

După ce am instalat utilitarul Gedit îl putem utiliza din terminal cu comanda gedit <nume_fisier>:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2001-24-28.png)

Un alt editor de fișiere este vim. Poate fi instalat cu comanda:

* sudo apt install vim

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2000-24-21.png)

Astfel, fisierul pe care dorim să îl modificăm poate fi editat și din terminal cu comanda:

* vim <nume_fisier>

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2000-22-13.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2001-25-41.png)

Pentru a închide fereastra vim se va utiliza comanda după caz:

* :q - se iese din programul vim fără modificarea fișierului corespunzător
* :wq - se iese din programul vim după ce s-au efectuat modificări în fișierul corespunzător

Pentru a testa manual aplicatia vom utiliza comanda:

* python3 -m pytest -v

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2016-17-19.png)

Pentru a rula cu succes comanda din imagine avem nevoie de importul bibliotecii sys, adăugând în scriptul 443_fructe.py comanda:

* import sys

Conținutul pe care trebuie să îl aibă fișierul de testare este ilustrat în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2017-12-56.png)

Pylint ne ajută să îmbunătățim codul aplicației prin detectarea erorilor ca în figura de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-21%2001-18-04.png)

Comanda este:

* python3 -m pylint 443_fructe.py

Biblioteca utilizată este definită după următorii parametri:
* culoare
* descriere

Modul de utilizare al parametrilor "culoare" și "descriere" este ilustrat în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2017-06-06.png)

Scriptul din imagine este util în realizarea importului bibliotecii fructe în fișierul 443_fructe.py.


Mai departe sunt prezentate modalitățile prin care vom rula aplicația web:

# 1. Local
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

# 2. Docker
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

# 3. Github
După ce am testat aplicația local următoarea etapă este încărcarea aplicației pe Github. În imaginile de mai jos putem observa procesul prin care proiectul nostru de Github este trimis din repository-ul local într-un repository remote.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2012-47-07.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2012-58-33.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-14-35.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-16-04.png)

După cum s-a observat modificările din repository-ul local au fost aduse pe Github pe branch-ul pe care l-am selectat înainte de a folosi comanda:

* git push

Pentru a sincroniza branch-urile main_[nume_branch] și devel_[nume_branch] se urmărește modalitatea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-18-51.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-20-17.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-21-44.png)

În final, putem vizualiza acum că branch-ul main_[nume_branch] a fost actualizat cu modificările din devel_[nume_branch] după ce am realizat "merge" din devel_[nume_branch] în main_[nume_branch] pe repository-ul remote.

Pentru a actualiza acum repository-ul local după ce am modificat în branch-urile prezentate vom executa în terminal comanda:

* git pull

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-17%2010-08-14.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-30-50.png)

Mai jos sunt ilustrate modificările apărute în urma editării fișierului aplicației.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_git/Screenshot%20from%202024-05-16%2013-28-40.png)

# 4. Jenkins
Jenkins este un server de automatizare open-source care ne ajută să automatizăm diverse sarcini legate de dezvoltarea software, cum ar fi construirea, testarea și implementarea aplicației. Utilizarea Jenkins ne permite să economisim timp și să reducem erorile umane în procesul de dezvoltare.

Cum funcționează Jenkins?
Jenkins utilizează job-uri și pipeline-uri. Un job reprezintă o sarcină individuală de automatizare. Fiecare job poate reprezenta un proces de construcție, testare sau implementare a unui proiect software. Un pipeline este o suită de joburi care sunt interconectate și configurează procesul complet de livrare a software-ului. Jenkins poate extrage codul sursă din diverse sisteme de control al versiunilor (cum ar fi Git). După ce codul este extras, Jenkins execută scripturile de construcție (de exemplu, Gradle) pentru a compila codul. După compilare, Jenkins rulează testele automate pentru a verifica dacă noul cod nu introduce erori.

Care sunt avantajele utilizării Jenkins?
* automatizare completă: automatizează procesele repetitive, economisind timp și reducând erorile umane.
* integrare ușoară: se integrează cu numeroase instrumente și tehnologii utilizate în dezvoltarea software.
* scalabilitate: poate fi extins cu ajutorul plugin-urilor pentru a îndeplini cerințe specifice proiectului.
* monitorizare și raportare: oferă vizibilitate completă asupra stării proiectelor prin rapoarte detaliate și notificări în timp real.

Mai jos este ilustrat un pipeline Jenkins care a trecut toate testele:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_jenkins/Screenshot%20from%202024-05-20%2021-16-51.png)

În urma execuției pipeline-ului putem vizualiza în imaginea de mai jos că s-a creat un nou container Docker cu tag-ul v55:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Implementare_aplicatie_in_jenkins/Screenshot%20from%202024-05-20%2021-28-18.png)


