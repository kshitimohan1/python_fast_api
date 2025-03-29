pipeline {
    agent any
    environment {
        GIT_REPO = 'https://github.com/kshitimohan1/python_fast_api.git'
        DOCKER_IMAGE = 'kshitimohan/python_fast_api'
        CONTAINER_NAME = 'python_fastapi_container'
    }
    stages {
        // Stage 1: Checkout code from Git
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: env.GIT_REPO
            }
        }

        // Stage 2: Build and Push Docker image to Docker Hub
        stage('Build and Push Docker Image') {
            steps {
                script {
                    sh 'docker context use default'

                    withCredentials([usernamePassword(credentialsId: '1',
                    usernameVariable: 'DOCKER_HUB_USR',
                    passwordVariable: 'DOCKER_HUB_PSW')]) {
                        sh "echo ${DOCKER_HUB_PSW} | docker login -u ${DOCKER_HUB_USR} --password-stdin"
                    }

                    docker.build("${env.DOCKER_IMAGE}:latest")
//                     docker.build("${env.DOCKER_IMAGE}:${env.BUILD_ID}")
                    docker.build("${env.DOCKER_IMAGE}:latest")
                    docker.withRegistry('https://registry.hub.docker.com', '1') {
                        docker.image("${env.DOCKER_IMAGE}:latest").push()
//                     docker.image("${env.DOCKER_IMAGE}:${env.BUILD_ID}").push()
                        docker.image("${env.DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }

        // Stage 3: Stop and Remove Existing Container
        stage('Stop and Remove Existing Container') {
            steps {
                script {
                    sh '''
                    docker ps -q --filter "name=$CONTAINER_NAME" | grep -q . && \
                    docker stop $CONTAINER_NAME && \
                    docker rm $CONTAINER_NAME || true
                    '''
                }
            }
        }

        // Stage 4: Deploy New Container
        stage('Deploy New Container') {
            steps {
                sh 'docker run -d --name $CONTAINER_NAME -p 8000:8000 $DOCKER_IMAGE:latest'
            }
        }
    }
}
