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
                // Устанавливаем зависимости прямо в контейнер Jenkins
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Запускаем тесты и генерируем папку allure-results
                sh 'pytest tests/test_api.py --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            // Генерируем отчет Allure в папку allure-report
            // Если плагин Allure установлен, Jenkins сам подхватит эту папку
            sh 'allure generate allure-results --out allure-report'
        }
    }
}
