pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
            	echo 'Building...'
                sh '''
                    pwd;
                    ls -l;
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
                    . .venv/bin/activate
                    if [ $? -eq 0 ]
		    then
    		    	echo "SUCCESS: venv was activated."
		    else
    		    	echo "FAIL: cannot activate venv"
    		    	python3 -m venv .venv
                        . .venv/bin/activate
		    fi
		    
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
                    . .venv/bin/activate
                    cd app
                    python3 -m pytest -v
                '''
            }
        }
        
        
        stage('Deploy') {
            steps {
                echo "Build ID: ${BUILD_NUMBER}"
                echo "Creare imagine docker"
                sh '''
                    docker build -t fructee:v${BUILD_NUMBER} .
                    docker create --name fructee${BUILD_NUMBER} -p 8020:5011 fructee:v${BUILD_NUMBER}
                '''
            }
        }
    }
}
