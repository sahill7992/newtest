pipeline {
  agent any
  
  options {
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }
  
  triggers {
    pullRequest()    
  }
  
  stages {
    stage('Checkout') {
      steps {
        // Checkout the pull request branch
        sh "git fetch origin pull/${env.CHANGE_ID}/head:pr-${env.CHANGE_ID}"
        sh "git checkout pr-${env.CHANGE_ID}"
      }
    }
    
    stage('Run Tests') {
      steps {
        // Run your test cases here
      }
    }
    
    stage('Merge Pull Request') {
      when {
        // Only run this stage if the previous stage succeeded
        expression { currentBuild.result == 'SUCCESS' }
      }
      steps {
        // Checkout the staging branch
        sh 'git checkout staging'
        
        // Fetch the latest changes from the remote repository
        sh 'git fetch origin'
        
        // Pull the latest changes from the staging branch
        sh 'git pull origin staging'
        
        // Merge the changes from the pull request branch
        sh "git merge --no-ff pr-${env.CHANGE_ID}"
        
        // Push the changes to the remote repository
        sh 'git push origin staging'
      }
    }
  }
}
