# Curs_VCGJ_2024_fructe

Proiectul de față își propune să demonstreze procesul de configurare și implementare a unei aplicații web folosind o mașină virtuală. Prin acest proiect, vom trece prin pașii necesari pentru instalarea și configurarea diverselor unelte software esențiale pentru dezvoltarea unei aplicații web, subliniind importanța fiecărei componente în parte.

Am început prin instalarea unei mașini virtuale pe un sistem de operare Windows, un mediu izolat care ne permite să experimentăm și să configurăm aplicațiile fără a afecta sistemul principal. După ce am verificat funcționarea corectă a mașinii virtuale, următorul pas a fost deschiderea unui terminal pentru a instala header-ele necesare pentru Linux. Acestea sunt esențiale pentru a asigura compatibilitatea și funcționarea corectă a sistemului de operare.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Instalare%20VM/Screenshot%202024-05-20%20135903.png)

Am verificat. Mașina este funcțională:

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Instalare%20VM/Screenshot%20from%202024-05-20%2015-21-50.png)

După ce am finalizat etapa de funcționare a mașinii virtuale trebuie să ne asigurăm că avem toate tool-urile necesare în proiect. Pentru început deschidem un terminal în mașina virtuală pentru a instala header-ele necesare pentru Linux. Acestea sunt esențiale pentru a asigura compatibilitatea și funcționarea corectă a sistemului de operare.

![image](https://github.com/buzzer0996/Curs_VCGJ_2024_fructe/blob/main/app/img/Tools/Screenshot%20from%202024-05-20%2015-18-08.png)

Instalarea Git și a editorului de text Gedit este esențială pentru gestionarea codului sursă și efectuarea modificărilor necesare pentru tema aleasă.Git ne permite să urmărim schimbările și să colaborăm eficient într-un mediu remote, în timp ce Gedit oferă un mediu de editare simplu și eficient, adecvat lucrului local. Prima imagine ilustrează instalarea cu succes a utilitarului Git pe Ubuntu, iar în cea de-a doua imagine se confirmă faptul că programul de editare Gedit a fost instalat corect.

![image]()

![image]()

Pentru a avea acces la modificarea fisierelor necesare utilizării aplicației în mediul local trebuie să obținem o clonă a fișierului din linkul de github:

![image]()

![image]()

Verificăm dacă avem instalat Python pe sistemul nostru de operare, în cazul nostru, Linux. Figura de mai jos ilustrează deja că sistemul de operare utilizează Python pentru a rula cu succes fișierele care au extensia .py.

![image]()

După ce am instalat Python, următorul pas este să instalăm pachetele necesare pentru proiectul nostru. Aceste pachete pot include biblioteci și framework-uri specifice pentru dezvoltarea aplicației noastre.

* Flask
* Pytest
* Pylint

# FLASK

![image]()

# PYTEST

![image]()

# PYLINT

![image]()

Înainte de a instala framework-urile de python este important să lucrăm într-un mediu virtual. Dacă nu avem instalat un astfel de mediu de lucru o putem face cu comanda:

*  python3 -m venv .venv

După ce am instalat mediul virtual, este necesară activarea "venv" pentru a facilita utilizarea lui în proiectul nostru. O altă metodă de a instala mult mai simplu framework-urile de python putem crea un fișier text pe care îl salvăm în aceeași locație cu aplicația noastră, în care vor fi incluse numele pachetelor pe care dorim să le instalăm pe calculatorul nostru personal. Comanda pentru a instala aceste pachete este mai jos:

* pip install -r quickrequirements.txt

![image]()

Pentru a afișa pachetele deja instalate utilizăm comanda:

* pip freeze

Dacă dorim să modificăm conținutul din fișierele deja create putem utiliza utilitarul Vim.

După ce am instalat utilitarul Vim îl putem utiliza din terminal cu comanda vim <nume_fisier>:


![image]()

![image]()
