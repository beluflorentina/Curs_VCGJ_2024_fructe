# Curs_VCGJ_2024_fructe

Proiectul de față își propune să demonstreze procesul de configurare și implementare a unei aplicații web folosind o mașină virtuală. Prin acest proiect, vom trece prin pașii necesari pentru instalarea și configurarea diverselor unelte software esențiale pentru dezvoltarea unei aplicații web, subliniind importanța fiecărei componente în parte.

Am început prin instalarea unei mașini virtuale pe un sistem de operare Windows, un mediu izolat care ne permite să experimentăm și să configurăm aplicațiile fără a afecta sistemul principal. După ce am verificat funcționarea corectă a mașinii virtuale, următorul pas a fost deschiderea unui terminal pentru a instala header-ele necesare pentru Linux. Acestea sunt esențiale pentru a asigura compatibilitatea și funcționarea corectă a sistemului de operare.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Instalare%20VM/Screenshot%202024-05-20%20135903.png)

Am verificat. Mașina este funcțională:

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

Instalarea Git și a editorului de text Gedit este esențială pentru gestionarea codului sursă și efectuarea modificărilor necesare pentru tema aleasă. Git ne permite să urmărim schimbările și să colaborăm eficient într-un mediu remote, în timp ce Gedit oferă un mediu de editare simplu și eficient, adecvat lucrului local. Prima imagine ilustrează instalarea cu succes a utilitarului Git pe Ubuntu, iar în cea de-a doua imagine se confirmă faptul că programul de editare Gedit a fost instalat corect.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-30-05.png)

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-30-22.png)

Pentru a actualiza sistemul cu noile pachete instalate vom utiliza comanda:

* sudo apt update

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-34-14.png)

Pentru a avea acces la modificarea fisierelor necesare utilizării aplicației în mediul local trebuie să obținem o clonă a fișierului din linkul de github:

![image]()

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-43-36.png)

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

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2016-14-09.png)

Pentru a testa manual aplicatia vom utiliza comanda:

* python3 -m pytest -v

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2016-17-19.png)

Pentru a rula cu succes comanda din imagine avem nevoie de importul bibliotecii sys, adăugând în scriptul 443_fructe.py comanda:

* import sys

Conținutul pe care trebuie să îl aibă fișierul de testare este ilustrat în imaginea de mai jos:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/scripturi/Screenshot%20from%202024-05-20%2017-12-56.png)

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
