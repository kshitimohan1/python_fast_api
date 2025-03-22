pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('1') // Jenkins credentials ID for Docker Hub
        GIT_REPO = 'https://github.com/kshitimohan1/python_fast_api.git'
        DOCKER_IMAGE = 'kshitimohan/python_fast_api'
    }
    stages {
        // Stage 1: Checkout code from Git
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: env.GIT_REPO
            }
        }

        // Stage 2: Build and push Docker image to Docker Hub
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build the Docker image with 'latest' and BUILD_ID tags
                    docker.build("${env.DOCKER_IMAGE}:latest")
                    docker.build("${env.DOCKER_IMAGE}:${env.BUILD_ID}")

                    // Push the Docker image to Docker Hub
                    docker.withRegistry('https://registry.hub.docker.com', 1) {
                        docker.image("${env.DOCKER_IMAGE}:latest").push()
                        docker.image("${env.DOCKER_IMAGE}:${env.BUILD_ID}").push()
                    }
                }
            }
        }
    }
}
