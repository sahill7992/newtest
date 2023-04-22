pipeline {
    agent any
    triggers {
        githubPullRequest(
            autoCloseFailedPullRequests: true,
            branches: [[pattern: 'dev']],
            orgScmCredentials: 'github',
            triggerPhrase: 'test this'
        )
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Build and Test') {
            steps {
                // Add your build and test steps here
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
