pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
            	echo 'Building...'
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install flask pylint pytest
                '''
            }
        }
        
        stage('Lint') {
            steps {
            	echo 'Running Pylint...'
                sh '''
                    . .venv/bin/activate
                    pylint --exit-zero app
                '''
            }
        }
        
        stage('Unit Testing') {
            steps {
            	echo 'Unit testing with Pytest...'
                sh '''
                    . .venv/bin/activate
                    # pytest
                    flask --app=app.443D_fructe test
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                echo 'Build ID: ${BUILD_NUMBER}'
                sh '''
                    docker build -t image-apple:v${BUILD_NUMBER} .
                    docker create --name apple-${BUILD_NUMBER} -p 5000:5000 image-apple:v${BUILD_NUMBER}
                '''
            }
        }
    }
}

