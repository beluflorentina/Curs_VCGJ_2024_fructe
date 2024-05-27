# Curs_VCGJ_2024_fructe
   # Creare spatiu de lucru si clonare aplicatie:   
   mkdir fructe
   cd fructe
   git clone https://github.com/beluflorentina/Curs_VCGJ_2024_fructe.git

   sudo apt upgrade
   sudo apt install git

   cd Curs_VCGJ_2024_fructe
   git checkout devel_andra1402
   
   # Creare mediu virtual si activare
   python3 -m venv .venv
   . .venv/bin/activate
   
   # Instalare pachete
   pip install flask
   pip install pytest
   pip install pylint
   
   # Rulare aplicatie
   cd app
   flask --app 443_fructe.py run --debug

   # Creare si rulare container
   cd ..
   docker build -t imagine-aplicatie
   docker run -p 8080:500 --name container-aplicatie imagine-aplicatie
   
   # Incarcare imagine pe Docker Hub
   docker login
   docker tag imagine-aplicatie andra1402/imagine_aplicatie:latest
   docker push andra1402/imagine_aplicatie:latest
   
   # Testare
   cd app/test
   pytest .
   
   # Staging, inregistrare modificari si sincronizare local cu remote
   git add
   git commit -m "versiunea 1"
   git push origin devel_andra1402
   
   # Oferire drepturi Jenkins
   sudo groupadd docker
   sudo usermod -aG docker $USER
   sudo gpasswd -a $USER docker
   restart Ubuntu
   
   # Rulare Jenkins
   jenkins
   # Accesare server Jenkins din browser la 127.0.0.1:8080
   
