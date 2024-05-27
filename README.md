# Curs_VCGJ_2024_fructe
# Fruct - Curmală
# Cuprins

1. [Descrierea aplicatiei](#descrierea-aplicatiei)
1. [Exemplificarile functionalitatii aplicatiei](#exemplificarile-functionalitatii-aplicatiei)
1. [Descrierea versiunii](#descrierea-versiunii)
1. [Configurare](#configurare)
1. [Bibliografie](#bibliografie)


# Descrierea aplicatiei 
Aplicația "fructe" furnizează informații despre curmala, fructul ales pentru acest proiect.

Interfața web a aplicației este creată utilizând framework-ul Flask din Python. Informațiile sunt colectate prin modulul subprocess din Python și comenzi shell, care extrag datele despre sistemul de operare și rețea. Ulterior, aceste informații sunt procesate de funcții dedicate de vizualizare și sunt furnizate clientului web care le solicită de la server. Aplicația este configurată să funcționeze în containere, iar un fișier Dockerfile este disponibil în directorul principal.

Funcțional, aplicația prezintă detalii despre fructul ales, curmală, pe o pagină web, organizată în două secțiuni: una pentru o descriere generală a fructului și alta pentru descrierea culorii acestuia.


# Exemplificarile functionalitatii aplicatiei

<img width="887" alt="Screenshot 2024-05-26 at 19 53 10" src="https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673147/78afb51a-fd3e-42f4-ad1e-ef4b9b15e547">

<img width="887" alt="Screenshot 2024-05-26 at 20 00 22" src="https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673147/7a030122-17a4-4e44-9e70-de979430b7e3">

<img width="890" alt="Screenshot 2024-05-26 at 20 00 52" src="https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673147/10385744-1664-42d7-b870-db985e54ae27">

# Descrierea versiunii
* ruta standard '/' - URL: http://127.0.0.1:5000
 * rute in aplicatia WEB pentru:
   * smochina:http://127.0.0.1:5000/curmala
   * descriere:http://127.0.0.1:5000/curmala/descriere
   * culoare:http://127.0.0.1:5000/curmala/culoare

# Configurare:

<img width="734" alt="creare venv cu init cu source (1) " src="https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673147/b1d158e6-ece5-4bb2-b531-0a9893684e78">

<img width="734" alt="exemplu push (2)" src="https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673147/f904083b-9de3-4843-8684-783b80bb2a06">

<img width="819" alt="rulare aplicatie prin docker (3)" src="https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673147/fa18131b-22a6-46db-9123-5877fd8167b5">

<img width="744" alt="rulare aplicatie prin flask (4)" src="https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673147/20915530-3097-4570-91bd-8f75160fdd93">

# Bibliografie 
- [Github Actions](https://docs.github.com/en/actions)







