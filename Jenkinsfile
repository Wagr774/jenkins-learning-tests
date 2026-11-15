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
                # 1. Создаем виртуальное окружение
                # 2. Устанавливаем зависимости именно в него
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Запускаем pytest, указывая полный путь к исполняемому файлу в venv
                sh './venv/bin/pytest tests/test_api.py --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            // Генерируем отчет, тоже вызывая allure из нашего venv
            sh './venv/bin/allure generate allure-results --out allure-report'
        }
    }
}
