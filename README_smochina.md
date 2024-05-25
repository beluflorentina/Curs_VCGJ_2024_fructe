
# Fructe - Smochină
### student Oprea Livia-Daniela-Mihaela 443D
![download](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673080/5f089c0f-a9ad-4f13-8d64-6523fd166b97)

# Cuprins

1. [Descrierea aplicatiei](#descrierea-aplicatiei)
1. [Descrierea versiunii](#descrierea-versiunii)
1. [Configurare](#configurare)
1. [Exemple](#exemple)
1. [Bibliografie](#bibliografie)

# Descrierea aplicatiei:

Aplicația Fructe oferă informații detaliate despre smochină, care este fructul ales pentru acest proiect. Informațiile sunt împărțite în două secțiuni: una conține o descriere a smochinei, iar cealaltă prezintă culoarea acesteia.

Partea web a aplicației utilizează framework-ul Flask pentru a funcționa. Aplicația este destul de simplă, citind informațiile necesare prin intermediul modulului subprocess din Python și a comenzilor shell pentru a obține date despre sistemul de operare și rețea. Aceste informații sunt apoi prelucrate în funcțiile view și trimise înapoi clientului web care face cererea către server.

Pentru a facilita navigarea, pagina principală a aplicației conține link-uri către celelalte pagini ale site-ului. De asemenea, fiecare pagină specifică include un link înapoi către pagina principală.

Aplicația este pregătită pentru a fi rulată în containere, având un fișier Dockerfile în directorul principal al aplicației.

În ceea ce privește testarea, aplicația include teste unitare realizate cu pytest pentru unele funcții din biblioteca aplicației, care se află în directorul app/lib.

![5](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673080/f3707ee4-3783-4a08-af1c-5c66d5d38a18)

# Descrierea versiunii:
## v0.02 - afisare 'raw' fara formatare. Adaugare link-uri intre pagini si modul generare si afisare grafice.

 * ruta standard '/' - URL: http://127.0.0.1:5000
 * rute in aplicatia WEB pentru:
   * smochina:http://127.0.0.1:5000/smochina
   * descriere:http://127.0.0.1:5000/smochina/descriere
   * culoare:http://127.0.0.1:5000/smochina/culoare
  
# Configurare:

Configurare .venv si instalarea pachetelor necesare

1) activare venv:

![1](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673080/13aee104-4b0e-4971-86c9-725ccec222ac)
 
2) ruleaza aplicatia:

![2](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673080/9b37ae85-535a-4fab-9049-304a384f2f5c)

![3](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673080/ac82e34a-1730-4665-98d3-7e5747b1236b)

![4](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673080/aa37e591-d6d1-479b-8769-9dcfd3af1870)

# Exemple:

![6](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673080/11ba5d7b-8ff0-448b-8742-f5cd60b86e81)

![8](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673080/f767b35e-bae7-437a-b43e-4a79c555f71e)

![7](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/127673080/3c77070d-4dea-42e3-996c-aa285243f0ad)

# Bibliografie:

- [Github Actions](https://docs.github.com/en/actions)
