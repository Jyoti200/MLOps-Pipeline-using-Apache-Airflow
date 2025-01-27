# MLOps-Pipeline-using-Apache-Airflow
Machine Learning Operations (MLOps) integrates machine learning model development and deployment into a robust, automated pipeline. 
This repository provides a guide on automating the preprocessing of data using Apache Airflow. It includes step-by-step instructions to set up and run an Apache Airflow instance inside Docker, and perform tasks like data preprocessing, transformation, and automation using Airflow's DAGs.

Prerequisites
Before you start, make sure the following tools are installed on your machine:

Docker - To run Apache Airflow and dependencies in containers.

Install Docker Desktop from here.
Python - For managing virtual environments and running scripts.

Install Python from here.
Apache Airflow - To create workflows for automating data preprocessing.

This is installed inside a Docker container.
Setting Up the Environment
Follow the steps below to get started with Apache Airflow and set up your data preprocessing pipeline.

1. Clone the Repository
git clone <MLOps-Pipeline-using-Apache-Airflow>
2. Create and Activate Virtual Environment (Optional)
This step is optional but recommended if you want to manage dependencies separately from the global Python installation.

python -m venv venv
.\venv\Scripts\activate
3. Install Dependencies
Ensure that you have all the necessary Python packages for your project:

pip install -r requirements.txt
The requirements.txt file includes:
apache-airflow
pandas
numpy
Other necessary libraries for data preprocessing

4. Set Up Apache Airflow Using Docker
Apache Airflow will be set up inside Docker for ease of use.

a. Docker Compose Configuration
Inside the repository folder, you should find the docker-compose.yaml file. This file contains the configuration for running Airflow containers.

b. Start Docker Containers
Ensure Docker Desktop is running on your machine. Then, in the project directory, use the following command to start the Airflow services:

docker-compose up
This will start the following containers:

PostgreSQL (for Airflow's metadata database)
Airflow Scheduler
Airflow Webserver
5. Access Airflow Web Interface
Once the containers are up and running, you can access the Airflow Web Interface at http://localhost:8080.

Username: admin
Password: admin
6. Run Data Preprocessing DAG
The data preprocessing pipeline is automated using a Directed Acyclic Graph (DAG) in Airflow. This DAG will define tasks for data preprocessing, such as cleaning, transformation, and saving the processed data.

To run the pipeline:

Navigate to the DAGs tab in the Airflow Web UI.
Look for your data_preprocessing_dag.
Click on the Trigger DAG button to run the pipeline manually, or set it to run on a schedule.
7. Stopping Docker Containers
To stop the Docker containers running Airflow:

docker-compose down
8. Troubleshooting
If Docker Desktop is not opening or Docker containers fail to run, try the following steps:
Restart Docker Desktop: Close and reopen Docker Desktop.
Check Running Processes: Use taskkill to stop any processes using port 8080.
For example:
taskkill /PID <PID> /F
Rebuild Docker Containers: If issues persist, rebuild the Docker containers:
docker-compose up --build
9. Updating the Airflow Configuration
If you need to make changes to the Airflow configuration, update the docker-compose.yaml file or any Airflow configuration files. Be sure to restart the Docker containers after making changes.

File Structure
folder/
├── airflow_project/
│   ├── dags/
│   │   └── data_preprocessing_dag.py    # Main DAG for automating data preprocessing
│   ├── requirements.txt                 # Dependencies
│   ├── data/
│   │   └── data.csv                     # Dataset
├── docker-compose.yaml                 # Docker Compose file to run Airflow in containers
└── README.md                           # Documentation for setting up the project
Conclusion
With this setup, you have automated your data preprocessing pipeline using Apache Airflow, running inside Docker. The system allows for easy scheduling, monitoring, and management of data workflows, making it ideal for building scalable, production-ready pipelines.
