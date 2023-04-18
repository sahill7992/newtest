pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'npm install'
            }
        }
        stage('Run tests admin') {
            steps {
                sh 'npm test test/callback.test.js'
            }
        }    

    }
}
