#!groovy

properties([disableConcurrentBuilds()])

pipeline {
    agent any 
    options {
        buildDiscarder(logRotator(numToKeepStr: '5', artifactNumToKeepStr: '5'))
        timestamps()
    }
    properties([pipelineTriggers([githubPush()])])
    stages {
        stage("Build image"){
            steps {
                sh 'docker build -t lyceum-app .'
            }
        }
        stage("Run images"){
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}

