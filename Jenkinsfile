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
        stage('TestSC') {
            steps {
                echo "Test SonarQube.."
                sh '''
                sonar-scanner.bat -D"sonar.projectKey=secu-project" -D"sonar.sources=." -D"sonar.host.url=http://localhost:9000" -D"sonar.token=sqp_2e362ba9e755fb0207ebbf6fb9de5e9089774c6d"
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
