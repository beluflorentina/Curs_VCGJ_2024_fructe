pipeline {
    agent any
    
    environment {
        FLASK_ENV = 'development'
        FLASK_APP = './app/443_fructe.py'
    }

    stages {
        stage('Preparation') {
            steps {
                script {
                    echo 'Preparing environment...'
                    sh '''
                        python3 -m venv .venv
                        . .venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        
        stage('Lint') {
            steps {
                script {
                    echo 'Running Pylint...'
                    sh '''
                        . .venv/bin/activate
                        pylint --exit-zero app/lib/*.py
                        pylint --exit-zero app/test/*.py
                        pylint --exit-zero app/443_fructe.py
                    '''
                }
            }
        }
        
      stage('Unit Testing') {
    steps {
        script {
            echo 'Running Unit Tests...'
            sh '''
                . .venv/bin/activate
                echo "Virtual environment activated."
                export PYTHONPATH=$PYTHONPATH:/var/lib/jenkins/workspace/item/app
                echo "PYTHONPATH: $PYTHONPATH"
                echo "sys.path: $(python -c 'import sys; print(sys.path)')"
                echo "Current working directory: $(pwd)"
                python3 -m pytest -v
            '''
        }
    }
}
        
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    sh '''
                        docker build -t my-flask-app .
                    '''
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying Application...'
                    
                }
            }
        }
    }
}

