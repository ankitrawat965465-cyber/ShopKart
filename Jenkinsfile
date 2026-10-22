
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ankitrawat965465-cyber/ShopKart.git'
            }
        }

        stage('Validate Compose') {
            steps {
                sh 'docker compose config -q'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t shopkart:jenkins .'
            }
        }
    }
}
