pipeline {
environment {
registry = "vinodh1988leo"
registryCredential = 'dockerCredentials'
dockerImage = 'flask-app-docker'
}
agent any
stages {
stage('Cloning our Git') {
steps {
git ''
}
}
stage('Building our image') {
steps{
script {
dockerImage = docker.build registry+"/"+ dockerImage + ":$BUILD_NUMBER"
}
}
}
stage('Deploy our image') {
steps{
script {
docker.withRegistry( '', registryCredential ) {
dockerImage.push()
}
}
}
}
stage('Cleaning up') {
steps{
sh "docker rmi $registry/$dockerImage:$BUILD_NUMBER"
}
}
}
}