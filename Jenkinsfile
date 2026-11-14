pipeline {
    agent any

    stages {
        // Этап 1: Получение кода из GitHub
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Этап 2: Установка библиотек
        stage('Install Dependencies') {
            steps {
                // Мы создаем виртуальное окружение прямо внутри контейнера Jenkins
                sh 'python3 -m venv venv'
                sh './venv/bin/activate && pip install -r requirements.txt'
            }
        }

        // Этап 3: Запуск тестов
        stage('Run Tests') {
            steps {
                // Запускаем pytest и говорим ему сохранять результаты для Allure
                sh './venv/bin/activate && pytest tests/test_api.py --alluredir=allure-results'
            }
        }
    }

    // Этап после завершения (успешно или с ошибкой)
    post {
        always {
            // Генерируем отчет Allure
            sh 'allure_generate allure-results --out allure-report'
        }
    }
}
