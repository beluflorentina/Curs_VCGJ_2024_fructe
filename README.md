# Fruct - Rodie
# Cuprins

1. [Descrierea aplicatiei](#descrierea-aplicatiei)
1. [Descrierea versiunii](#descrierea-versiunii)
1. [Configurare](#configurare)
1. [Exemple](#exemple)
1. [Bibliografie](#bibliografie)

 # Descrierea aplicatiei:
 Aplicatia "fructe" ofera detalii despre rodie, fructul ales pentru acest proiect.

 Componenta web a aplicației funcționează folosind frameworkul python numit Flask. Aplicația colecteaza informațiile necesare prin modulul de subproces Python și comenzile shell pentru a prelua datele sistemului de operare și ale rețelei. Aceste date sunt apoi procesate în cadrul funcțiilor de vizualizare și returnate clientului web care le-a solicitat de la server. Aplicatia este pregatita pentru rulare utilizand containere, fapt pentru care un fisier Dockerfile este prezent in directorul principal.

 Din punct de vedere functional, aceasta aplicatie ne va returna informatii despre fructul ales prin cadrul unei pagini web, impartita in doua sectiuni; una pentru o descriere scurta a fructului ales (rodie) si una pentru a descriere culoarea sa.
 

 In cazul nostru aplicatia va afisa informatiile 

 ![rodie homepage](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/169394141/acc17eff-3cbd-438b-8197-2527985b7227)

 # Descrierea versiunii:

 * ruta standard '/' - URL: http://127.0.0.1:5000
 * rute in aplicatia WEB pentru:
   * smochina:http://127.0.0.1:5000/rodie
   * descriere:http://127.0.0.1:5000/rodie/descriere
   * culoare:http://127.0.0.1:5000/rodie/culoare

# Configurare:
   
![1](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/169394141/2daab8f2-7af1-440a-8cf9-71788ad927ae)

![2](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/169394141/49f4e381-2f4c-448a-83fc-a28cda958e7d)

![3](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/169394141/edbcf59a-6a7d-41a9-af68-378666ac54f4)

# Exemple:

![ex1](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/169394141/0047db70-54e8-4768-90f0-c509d9665b32)

![ex2](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/169394141/1d410211-3ede-4f51-8622-203e1357bddf)

# Bibliografie
- [Github Actions](https://docs.github.com/en/actions)
   
