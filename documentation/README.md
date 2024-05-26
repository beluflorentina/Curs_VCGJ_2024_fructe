# Curs_VCGJ_2024_fructe

Acest proiect vizeaza implementarea unei aplicatii web destinata lucrului colaborativ folosind git-flow, tehnica virtualizarii ce permite rularea mai multor Sisteme de Operare pe acelasi PC si containerizarii spre a incapsula aplicatia si vizata spre a fi testata folosind metode de pytest, pylint si Jenkins.

Structura aplicatiei:
Aplicatia contine doua functii numite ce definesc fructul Ananas si doua functii de test ce verifica anumite string-uri setate/alese ca pot fi gasite in paragrafele ce descriu fructul.

Rutele paginilor aplicatiei sunt urmatoarele:
http://127.0.0.1:5000/
http://127.0.0.1:5000/ananas
http://127.0.0.1:5000/ananas/culoare
http://127.0.0.1:5000/ananas/descriere

Aplicatia arata astfel ( in cazul prezentat in poza de mai jos a fost folosita ruta http://127.0.0.1:5000/ananas )
![ruta](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/blob/devel_Crisan_Bogdan/documentation/images/aplicatie_web.png)

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

Directorul Dockerfile care este un fisier text ce contine toate comenzile pe care un utilizator le-ar putea rula pe linia de comanda pentru a asambla imaginea Docker, contine instructiunile ce pot fi vizualizate in poza de mai jos.
![dockerfile](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/blob/devel_Crisan_Bogdan/documentation/images/dockerfile.png)

In aceasta poza de mai sus pot fi vazute urmatoarele instructiuni: 1. Imaginea de baza este python 3.10, cea pe care se construieste noua imagine. 2. Instructiuni de instalare pip(pentru managerul de pachete), flask(pentru framework) si pytest(pentru testare) 3. Directorul de lucru pentru orice instructiune este stabilit cu WORKDIR 4. Sunt copiate fisiere din contextul de constructe local in imagine cu instructiunea COPY 5. Se seteaza variabilele de mediu in container cu instructiunea ENV 6. Se seteaza portul care este ascultat de container si anume 5000. Setarea se face cu instructiunea EXPOSE 5000 7. Cu instructiunea CMD sunt furnizate comenzile care vor fi executate cand containerul este rulat. Doar ultima instructiune va fi luata in considerare.

    Instalare Flask (Framework-ul aplicatiei)
        > pip install flask
        > flask run -p 5011 --reload                                    //rulare aplicatie

    Instalare Jenkins [CI = continous integration / CD = continous delivery sau continous deployment]
        > sudo systemctl enable jenkins 	                            // face enable la Jenkins
        > sudo systemctl start jenkins 	                                // start
        > sudo systemctl status jenkins 	                            // verifica statusul

    	Lansarea se face in mod automat in productie trecand prin pipeline-ul CI/CD
             http://localhost:8080                                      // pe acest port este configurat Jenkins

    Instalare pytest
        > pip install pytest // testeaza functionalitatea codului

    Instalare pylint
        > pip install pylint // testeaza sintaxa codului

Trebuie sa ma asigur ca in fisierul .gitignore sunt comentate campurile pe care nu le doresc a fi aduse in Github.
Dupa cum se poate vedea in poza de mai jos am comentat campul ce ar aduce fisierul 'pycache' in git.
![pycache](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/blob/devel_Crisan_Bogdan/documentation/images/gitignore_pycache.png)

Testare

    > cd /app/test
    > pytest . // testeaza
    > cd ..
    > pylint 443_fructe.py

![pytest](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/blob/devel_Crisan_Bogdan/documentation/images/pytest_commanline.png)

Pentru testarea cu Jenkins este necesar sa dam drepturi:

    > sudo groupadd docker                                                          //creeaza grup nou numit 'docker'
    > sudo usermod -aG docker $user                                                 //adauga utilizatorul $user la grup
    > sudo gpasswd -a $USER docker                                                  //se asigura ca utilizatorii pot rula comenzi Docker fara a folosi 'sudo'

Codul ce defineste pipeline-ul Jenkins se afla in Jenkinsfile dupa cum se poate vedea in poza de mai jos
![jenkinsfile](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/blob/devel_Crisan_Bogdan/documentation/images/jenkinsfile.png)

Testarea cu Jenkins a decurs astfel:
Jenkins
![Jenkins](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/blob/devel_Crisan_Bogdan/documentation/images/Jenkins_Testare.png)

Blue Ocean
![BlueOcean](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/blob/devel_Crisan_Bogdan/documentation/images/Blue%20Ocean%20_Jenkins.png)

Rularea aplicatiei se face cu:

    > flask --app 443_fructe.py run --debug                                         // ruleaza aplicatia cu modul de debug
    > python3 app/443_fructe.py                                                     // ruleaza aplicatia cu modul de debug off

Pe 'local' am creat directorul pe care urmeaza sa il gestionam cu Git > mkdir scc > cd scc

In directorul numit 'scc' am clonat apoi repository-ul de pe 'remote' > git clone https://github.com/beluflorentina/Curs_VCGJ_2024_fructe.git // clonare repository proiect sablon > cd Curs_VCGJ_2024_fructe/ > git status // verific starea repository-ului obtinand informatii ca cele de mai jos

    > git branch -a                                                                 // vad toate branch-urile atat remote cat si local, cele create de Flori
    > git checkout -b remotes/origin/devel_Crisan_Bogdan                            // m-am mutat pe branch-ul meu de dev creat in remote Flori
    > git diff --staged                                                             // vad ce linii de cod au fost inainte si ce linii au fost adaugate in staged

Adaug descrierea fructului si adaug functiile de culoare si descriere in biblioteca_fructe.py ca in poza de mai jos.
![functii](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/blob/devel_Crisan_Bogdan/documentation/images/functii.png)

Dupa ce am modificat liniile de cod din 'biblioteca_fructe.py' si din 'test_lib.py' verific cu:

    > git status // observ ce am de adaugat in stage
    > git add // adauga app in staged
    > git commit -am "feature_Bogdan_Crisan/add_ananas" // face commit-ul pe local si creeaza feature-ul
    > git push origin devel_Crisan_Bogdan // face push din dev local in Origin dev remote
    > git status
    > cd app
    > python3 443_fructe.py // ruleaza aplicatia

Codul ce afiseaza web paginile si continutul paginilor ce descriu fructul se afla in 443_fructe.py si poate fi vazut in poza de mai jos:
![cod_web](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/blob/devel_Crisan_Bogdan/documentation/images/aplicatie.png)

Putem observa mai jos un pull request merged in origin devel_Crisan_Bogdan to main_Crisan_Bogdan
![pull_request](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/blob/main_Crisan_Bogdan/documentation/images/readme_1.png)

Am folosit comanda 'git reset HEAD~1' pentru a da uncommit si apoi am facut push to remote cu 'git push --force': > git reset HEAD~1 > git push --force > git remote show origin

![resetcommit](https://github.com/beluflorentina/Curs_VCGJ_2024_fructe/blob/devel_Crisan_Bogdan/documentation/images/git_reset_commit.png)
