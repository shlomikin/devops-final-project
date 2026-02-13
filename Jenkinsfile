pipeline {
    agent {
        label "${params.RUN_ON}"
    }

    parameters {
        choice(name: 'RUN_ON', choices: ['built-in', 'linux'], description: 'Select where to run')
        string(name: 'NAME', defaultValue: 'Shlomi', description: 'Student name')
        string(name: 'GRADE', defaultValue: '70', description: 'Grade (0-100)')
        booleanParam(name: 'BONUS', defaultValue: false, description: 'Apply bonus?')
        string(name: 'EXAM_DATE', defaultValue: '2025-01-01', description: 'Exam date YYYY-MM-DD')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Script') {
            steps {
                script {
                    if (params.RUN_ON == 'built-in') {
                        bat """
                        "C:\\Program Files\\Python314\\python.exe" script\\app.py ^
                        --name ${params.NAME} ^
                        --grade ${params.GRADE} ^
                        --bonus ${params.BONUS} ^
                        --exam_date ${params.EXAM_DATE}
                        """
                    } else {
                        sh """
                        python3 script/app.py \
                        --name ${params.NAME} \
                        --grade ${params.GRADE} \
                        --bonus ${params.BONUS} \
                        --exam_date ${params.EXAM_DATE}
                        """
                    }
                }
            }
        }


        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'output/*.*', fingerprint: true
            }
        }
    }
}
