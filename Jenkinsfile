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
                # Запуск тестов через pytest из виртуального окружения
                # Флаг --alluredir=allure-results создаст папку с результатами
                sh './venv/bin/pytest tests/test_api.py --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            echo "Build process finished!"
        }
    }
}
