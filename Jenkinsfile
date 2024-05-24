pipeline {
    agent none

    stages {
        stage('Build') {
            agent any
            steps {
                echo 'Building...'
                sh '''
                    cd app;
                    pwd;
                    ls -l;
                    . ./activeaza_venv_jenkins
                    '''
            }
        }

        stage('pylint - calitate cod') {
            agent any
            steps {
            	echo 'Pylint...'
                sh '''
                    cd app;
                    . ./activeaza_venv;
                    

                    pylint --exit-zero librarie/*.py;
                    
                    pylint --exit-zero ./test_*.py;
                    
                    pylint --exit-zero 443D_pomelo.py;
                '''
            }
        }

        stage('Unit Testing cu pytest') {
            agent any
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    cd app;
                    . ./activeaza_venv;
                    python3 -m pytest -v;
                '''
            }
        }
        
        stage('Deploying') {
        agent any 
            steps {
                echo 'Building the app...'
                sh 'docker build . -t pomelo_app'
            }
        }
}
}
