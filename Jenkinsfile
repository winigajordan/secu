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
        stage('SonarQube analysis') {
            steps {
                def scannerHome = tool 'SonarScanner 4.0.0.1744';
                withSonarQubeEnv('sq1') { // If you have configured more than one global server connection, you can specify its name
                sh "${scannerHome}/bin/sonar-scanner"
                }
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
