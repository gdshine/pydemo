pipeline{
    agent any
    stages{
        stage('pull pydemo'){
           steps{
            echo 'pull success'
            script{
                dir('d:/jenkins'){
                    checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '17dd5349-6155-4e2b-8b2d-190e871c99c5', url: 'https://github.com/gdshine/pydemo.git']]])
                    }
                }

            }
        }
        stage('excute pytest'){
            steps{
                script{
                    dir('d:/jenkins'){
                        bat 'pytest -s -d -n2 ./testcase/day2/'
                    }
                }
            }
        }
    }
    post{
        always {
            echo 'delete temp dir'
            deleteDir()
        }
        success {
            emailext (
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                        <p>Check console output at "<a href="${env.BUILD_URL}">${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>"</p>""",
                to: "328110875@qq.com",
                from: "328110875@qq.com"
            )
        }
        failure {
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                        <p>Check console output at "<a href="${env.BUILD_URL}">${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>"</p>""",
                to: "328110875@qq.com",
                from: "328110875@qq.com"
            )
        }
    }
}