# Curs_VCGJ_2024_fructe
# Fruct - Capsuna
# Cuprins

1. [Descrierea aplicatiei](#descrierea-aplicatiei)
1. [Descrierea versiunii](#descrierea-versiunii)
1. [Configurare](#configurare)
1. [Exemple](#exemple)
1. [Bibliografie](#bibliografie)

 # Descrierea aplicatiei:
 Aplicatia "fructe" ofera detalii despre capsuna, fructul ales pentru acest proiect.


Componenta web a aplicației funcționează folosind framework-ul Python Flask. Aplicația colectează informațiile necesare prin modulul subprocess din Python și prin comenzi shell pentru a prelua date despre sistemul de operare și rețea. Aceste date sunt apoi procesate în cadrul funcțiilor de vizualizare și returnate clientului web care le-a solicitat serverului. Aplicația este pregătită pentru rulare utilizând containere, fapt pentru care există un fișier Dockerfile în directorul principal.

Din punct de vedere funcțional, această aplicație va returna informații despre un fruct ales prin intermediul unei pagini web, împărțită în două secțiuni: una pentru o descriere scurtă a fructului ales (căpșună) și alta pentru o descriere a culorii sale.
 

 In cazul nostru aplicatia va afisa informatiile 
![6d37d415-d8a6-49e9-8f6f-3e3a026a6534](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/169368631/2b8ab5e0-0e4d-4147-934a-98424d6df9eb)


 # Descrierea versiunii:

 * ruta standard '/' - URL: http://127.0.0.1:5000
 * rute in aplicatia WEB pentru:
   * capsuna:http://127.0.0.1:5000/capsuna
   * descriere:http://127.0.0.1:5000/capsuna/descriere
   * culoare:http://127.0.0.1:5000/capsuna/culoare

# Configurare:
   ![1](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/169368631/ff2ca5e5-88eb-4183-91e5-2b42656f9a91)
![2](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/169368631/62945af4-786c-429d-8286-242edab1cffd)



# Exemple:
![4](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/169368631/eca55407-7996-41a8-a2f1-4f53c36d77ec)
1453cb7ccd88)
![3](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/169368631/20b6f196-f86f-474f-bc88-83b8be6e65a7)

# Bibliografie
- [Github Actions](https://docs.github.com/en/actions)
