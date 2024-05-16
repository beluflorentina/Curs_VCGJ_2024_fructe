pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
            	echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
                    cd app
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install flask
                    pip install pylint
                    pip install pytest
                '''
            }
        }
        
        stage('pylint - calitate cod') {
            steps {
            	echo 'Pylint...'
                sh '''
                    echo 'PATH before activation:'
                    echo $PATH
                    . .venv/bin/activate
                    echo 'PATH after activation:'
                    echo $PATH
                    pylint --exit-zero lib/*.py
                    pylint --exit-zero test/*.py
                    pylint --exit-zero 443_fructe.py
                '''
            }
        }
        
        stage('Unit Testing') {
            steps {
            	echo 'Unit testing with Pytest...'
                sh '''
                    echo 'PATH before activation:'
                    echo $PATH
                    . .venv/bin/activate
                    echo 'PATH after activation:'
                    echo $PATH
                    pytest
                '''
            }
        }
        
        
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
