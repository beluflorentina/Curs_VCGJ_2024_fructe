# Curs_VCGJ_2024_fructe

Acest proiect vizeaza implementarea unei aplicatii web destinata lucrului colaborativ folosind git-flow, tehnica virtualizarii ce permite rularea mai multor Sisteme de Operare pe acelasi PC si containerizarii spre a incapsula aplicatia si vizata spre a fi testata folosind metode de pytest, pylint si Jenkins.

Structura aplicatiei:
Aplicatia contine doua functii numite ce definesc fructul Ananas si doua functii de test ce verifica anumite string-uri setate/alese ca pot fi gasite in paragrafele ce descriu fructul.

Rutele paginilor aplicatiei sunt urmatoarele:
http://127.0.0.1:5000/
http://127.0.0.1:5000/ananas
http://127.0.0.1:5000/ananas/culoare
http://127.0.0.1:5000/ananas/descriere

Pasii necesari pentru instalarea si configurarea software sunt urmatorii:

    Instalare Git
        > sudo apt install git

    Instalare Python
        > sudo apt install python3

    Instalare Pip
        > sudo apt install pip

    Instalare Java
        > java -version                                                 //see package installed
    	> sudo apt install openjdk-11-jdk

    Instalare Venv (mediu virtual ce contine instanta python, interpretor + pachete de python)
        > . .venv/bin/activate                                          // activeaza venv

    Instalare Gedit
        > sudo apt install gedit

    Instalare Curl
        > sudo apt install curl

    Instalare Docker
        > sudo docker build -t fructinni                                // creeaza imagine Docker, imagine de container, pui punct la final
        > sudo docker images 		                                    // putem vizualiza imaginea
        > sudo docker run --name fructinni -p 8080:5000 fructinni       // genereaza un container din fisierul imagine si trebuie executata cu comanda run
        > sudo docker ps 			                                    // vizualizare containere care ruleaza
        > sudo docker ps -a 			                                // vizualizare toate containerele inclusiv cele oprite

    Instalare Flask (Framework-ul aplicatiei)
        > pip install flask
        > flask run -p 5011 --reload                                    //rulare aplicatie

    Instalare Jenkins [CI = continous integration / CD = continous delivery sau continous deployment]
        > sudo systemctl enable jenkins 	                            // face enable la Jenkins
        > sudo systemctl start jenkins 	                                // start
        > sudo systemctl status jenkins 	                            // verifica statusul

    	Lansarea se face in mod automat in productie trecand prin pipeline-ul CI/CD
             http://localhost:8080                                           // pe acest port este configurat Jenkins

    Instalare pytest
        > pip install pytest // testeaza functionalitatea codului

    Instalare pylint
        > pip install pylint // testeaza sintaxa codului

Testare

> cd /app/test
> pytest . // testeaza
> cd ..
> pylint 443_fructe.py

Pentru testarea cu Jenkins este necesar sa dam drepturi:

> sudo groupadd docker
> sudo usermod -aG docker $user
> sudo gpasswd -a $USER docker

Rularea aplicatiei se face cu:

> flask --app 443_fructe.py run --debug // ruleaza aplicatia cu modul de debug
> python3 app/443_fructe.py // ruleaza aplicatia cu modul de debug off

Pe 'local' am creat directorul pe care urmeaza sa il gestionam cu Git > mkdir scc > cd scc
In directorul numit 'scc' am clonat apoi repository-ul de pe 'remote'

> git clone https://github.com/beluflorentina/Curs_VCGJ_2024_fructe.git // clonare repository proiect sablon
> cd Curs_VCGJ_2024_fructe/
> git status // verific starea repository-ului obtinand informatii ca cele de mai jos

    > git branch -a                                                                 // vad toate branch-urile atat remote cat si local, cele create de Flori
    > git checkout -b remotes/origin/devel_Crisan_Bogdan                            // m-am mutat pe branch-ul meu de dev creat in remote Flori
    > git diff --staged                                                             // vad ce linii de cod au fost inainte si ce linii au fost adaugate in staged

Dupa ce am modificat liniile de cod din 'biblioteca_fructe.py' si din 'test_lib.py' verific cu:

> git status // observ ce am de adaugat in stage
> git add // adauga app in staged
> git commit -am "feature_Bogdan_Crisan/add_ananas" // face commit-ul pe local si creeaza feature-ul
> git push origin devel_Crisan_Bogdan // face push din dev local in Origin dev remote
> git status
> cd app
> python3 443_fructe.py // ruleaza aplicatia

Putem observa mai jos un pull request merged in origin devel_Crisan_Bogdan to main_Crisan_Bogdan
![alt text](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/blob/main_Crisan_Bogdan/documentation/images/readme_1.png)
