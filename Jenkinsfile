pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '''
                    cd app;
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
                    
                    pylint --exit-zero app/lib/*.py
                    pylint --exit-zero app/test/*.py
                    pylint --exit-zero app/443_fructe.py
                '''
            }
        }
        
        stage('Unit Testing') {
            steps {
                echo 'Unit testing with Pytest...'
                sh '''
                    . app/.venv/bin/activate
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
