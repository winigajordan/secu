pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
      triggers{
        pollSCM('*/5 * * * *')
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                echo "doing build stuff.."
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Test SonarQube.."
                sh '''
                sonar-scanner \
                    -Dsonar.projectKey=secu-project \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://localhost:9000 \
                    -Dsonar.token=sqp_2e362ba9e755fb0207ebbf6fb9de5e9089774c6d
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "doing test stuff.."
                python3 hello.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
