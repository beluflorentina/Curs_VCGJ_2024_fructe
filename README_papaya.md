```Curs_VCGJ_2024_fructe_papaya```

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
     - [Rute](#rute)
2. [Configurare](#configurare)
     - [Pregatire mediu de lucru](#pregatire-mediu-de-lucru)
     - [Clonare repo si activare venv](#clonare-repo-si-activare-venv)
3. [Rulare aplicatie](#rulare-aplicatie)
     - [Folosind Flask](#folosind-flask)
     - [Folosind Docker](#folosind-docker)
4. [Exemple pagina web](#exemple-pagina-web)


# Descriere aplicatie

Aplicatia ruleaza local, si printeaza informatii despre mai multe fructe. Dupa rularea aplicatiei, fie prin Flask fie prin Docker, aplicatia se poate accesa de la http://127.0.0.1:5000. Pagina principala contine toate fructele(pe acest branch doar acai si papaya), fiecare cu un link catre pagina fructului respectiv, care printeaza o descriere a fructului si culoarea acestuia.
Pagina unui fruct contine si un link inapoi catre ruta de baza `/`.

Aplicatia a fost dezvoltata si testata pe Ubuntu 22.04.

Componenta WEB a aplicatiei se bazeaza pe framework-ul `Flask`.

Aplicatia include suport pentru containerizare in fisierul `Dockerfile` din directorul principal al aplicatiei.

## Rute
 * ruta standard '/' - URL: http://127.0.0.1:5000
 * rute in aplicatia WEB specifice fructului de papaya; se adauga la URL-ul de baza de mai sus:
   * get-all papaya:       '/papaya',
   * get-culoare papaya:   '/papaya/culoare'
   * get-descriere papaya: '/papaya/descriere'

# Configurare
## Pregatire mediu de lucru
Software necesar pentru a rula aplicatia:
 * Python3.10
   * Python3-venv
 * Docker Engine(Docker Desktop include Docker Engine, deci pentru comoditate atat la instalare cat si pentru uz, se poate folosi Docker Desktop)

Aplicatia foloseste framework-ul Flask, dar acesta este deja inclus in virtual environmentu-ul din proiect(venv), si nu este nevoie sa fie instalat global pe intreaga masina.

========= NOTA: Pentru Ubuntu 22.04, Python3.10 este deja instalat by default ========= 

Pentru instalare Windows sau alte distributii Linux, 
e posibil sa fie nevoie de instalare manuala

=======================================================================================

Pentru instalare venv se ruleaza comanda:

```sudo apt-get install python3-venv -y```

Pentru instalare Docker Engine, exista instructiuni pe documentatia oficiala Docker:
https://docs.docker.com/engine/install/ubuntu/

Pentru instalare folosind ```apt``` repository, se dau in terminal urmatoarele comenzi:

```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Pentru a testa ca instalarea s-a facut corect, se poate containeriza imaginea ```hello-world``` oferita de Docker
```sudo docker run hello-world```

## Clonare repo si activare venv

Se cloneaza repository-ul folosind comanda ```git clone```
```git clone https://github.com/beluflorentina/Curs_VCGJ_2024_fructe.git```

Se acceseaza folder-ul cu proiectul si se activeaza venv folosind comanda ```source```

```source .venv/bin/activate```

# Rulare aplicatie
## Folosind Flask

Rularea aplicatiei folosind flask se face foarte usor, folosind comanda:
```flask --app app/443_fructe.py run```

Rezultatul acestei comenzi ar trebui sa arate ca mai jos(fara mesajele de GET):
![Screenshot 2024-05-25 031747](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/141660299/ef2e6e0e-c4f1-42e3-8bc2-acb8a2fb89f1)

## Folosind Docker

In directorul principal al aplicatiei, unde se afla Dockerfile-ul, se ruleaza comanda de ```docker build``` pentru a crea o imagine docker, si ```docker run``` pentru a rula un container folosind imaginea respectiva.

```sudo docker build -t <nume_pentru_container> .```
![docker1](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/141660299/f135ea3a-b3b9-455a-b85a-f35f06a2484c)

```docker run -dp 127.0.0.1:5000:5000 <nume_pentru_container>```
Pentru a afisa containerele care ruleaza se poate folosi comanda
```sudo docker ps```
![docker2](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/141660299/411a230d-e685-497d-80dc-44fc7bd474f9)

Pentru a opri container-ul se poate folosi comanda ```sudo docker stop <container_id>```

# Exemple pagina web
Pagina principala, ruta `/`:
![Screenshot 2024-05-25 031809](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/141660299/72f22527-2d3c-4414-af1d-62dc312636e3)

Pagina pentru descriere papaya, /papaya/descriere:
![Screenshot 2024-05-25 032156](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/assets/141660299/3c20d2b7-3521-4853-84da-69c4551bae33)



