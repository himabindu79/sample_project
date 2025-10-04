pipeline {
    agent any

    stages {
        stage('Checkout') {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install pandas
                '''
            }
        }

        stage('Run Data Cleaning Script') {
            steps {
                sh '''
                . venv/bin/activate
                python src/data_cleaning.py
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Data cleaning completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check the logs for errors."
        }
    }
}
