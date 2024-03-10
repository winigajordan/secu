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
                withSonarQubeEnv('sq1') {
                    sh 'sonar:sonar'
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
