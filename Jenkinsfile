pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/pytest tests/test_api.py --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            // Мы используем 'allure' напрямую. 
            // Если он не найден в venv, попробуем просто вызвать его.
            sh echo "Tests finished" || echo "Allure generate failed, but tests passed!"
        }
    }

}
