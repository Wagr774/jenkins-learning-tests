pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                sh "docker run --rm -v \$(pwd):/app -w /app python:3.9-slim sh -c 'pip install -r requirements.txt && pytest tests/test_api.py --alluredir=allure-results'"
            }
        }
    }
}
