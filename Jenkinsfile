pipeline {
    agent any
    environment {
        GIT_REPO = 'https://github.com/kshitimohan1/python_fast_api.git' // Your Git repository
        DOCKER_IMAGE = 'kshitimohan/python_fast_api' // Docker Hub image name
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
                    // Log in to Docker Hub securely using withCredentials
                    withCredentials([usernamePassword(credentialsId: '1', usernameVariable: 'DOCKER_HUB_USR', passwordVariable: 'DOCKER_HUB_PSW')]) {
                        sh "echo ${DOCKER_HUB_PSW} | docker login -u ${DOCKER_HUB_USR} --password-stdin"
                    }

                    // Build the Docker image with 'latest' and BUILD_ID tags
                    docker.build("${env.DOCKER_IMAGE}:latest")
                    docker.build("${env.DOCKER_IMAGE}:${env.BUILD_ID}")

                    // Push the Docker image to Docker Hub
                    docker.withRegistry('https://registry.hub.docker.com', '1') { // Use the credential ID '1'
                        docker.image("${env.DOCKER_IMAGE}:latest").push()
                        docker.image("${env.DOCKER_IMAGE}:${env.BUILD_ID}").push()
                    }
                }
            }
        }
    }
}