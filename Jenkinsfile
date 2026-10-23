        stage('Deploy with Docker Compose') {
            steps {
                sh '''
                    docker compose pull shopkart
                    docker compose up -d --no-build shopkart
                '''
            }
        }