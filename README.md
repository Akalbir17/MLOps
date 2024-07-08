# Lead Scoring Case Study

## Table of Contents
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Methodology](#methodology)
  - [Data Preprocessing and EDA](#data-preprocessing-and-eda)
  - [Model Experimentation](#model-experimentation)
  - [Pipelines](#pipelines)
  - [Test Cases](#test-cases)
- [Results](#results)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Airflow Setup](#airflow-setup)
  - [MLflow Setup](#mlflow-setup)
- [Usage](#usage)
- [License](#license)
- [Conclusion](#conclusion)

## Problem Statement
An ed-tech startup is looking to reduce its customer acquisition cost (CAC) by efficiently utilizing its marketing spends. The company has spent extensively on acquiring customers/leads and now aims to categorize leads based on their likelihood of purchasing the course. The objective is to build a system that predicts whether a lead will purchase the product or not, helping to remove the inefficiency caused by junk leads in the sales process.

## Dataset
The dataset primarily focuses on variables/features describing the origin of the lead (e.g., referred_leads, city_mapped) and the interaction of the lead with the website (e.g., 1_on_1_mentorship, whatsapp_chat_click).

## Methodology

### Data Preprocessing and EDA
- Conducted exploratory data analysis (EDA) using pandas profiling to gain insights into the dataset.
- Handled missing values and reduced high cardinality in certain columns.
- Classified interaction columns into four categories: assistance interaction, career interaction, payment interaction, and syllabus interaction.
- Detailed preprocessing and EDA steps can be found in the [Data Preprocessing & EDA notebook](https://github.com/Akalbir17/MLOps/blob/main/Lead_Scoring_Data_Pipeline/data_cleaning_template.ipynb).

### Model Experimentation
- Utilized Pycaret, an open-source machine learning library, for model experimentation.
- Performed initial experiments to identify irrelevant features and removed them in subsequent runs.
- Logged models to MLflow registry for tracking and comparison.
- Detailed model experimentation steps can be found in the [Model Experimentation notebook](https://github.com/Akalbir17/MLOps/blob/main/Notebooks/lead_scoring_model_experimentation.ipynb).

### Pipelines
- Developed data, training, and inference pipelines using Airflow for streamlined processing.
- Data Pipeline: Processes the raw data.
- Training Pipeline: Performs preprocessing and model training.
- Inference Pipeline: Handles preprocessing and model prediction.

### Test Cases
- Implemented unit test cases using pytest to validate preprocessing functionalities.
- Tested load_data_to_db function, city-to-tier mapping, categorical variable mapping, and interaction mapping schema.
- Test cases can be found in the [Test Case File](https://github.com/Akalbir17/MLOps/tree/main/Unit_Test).

## Results
- Identified LightGBM, an XGBoost classification algorithm, as the best-performing model based on accuracy.
- Achieved an accuracy of `89%` in predicting whether a lead will purchase the product or not.

## Requirements
- Python 3.7+
- Airflow
- MLflow
- Pycaret
- pandas
- numpy
- scikit-learn
- pytest
- jupyter

## Setup

### Airflow Setup
1. Install Airflow locally.
   
2. Create an Airflow user for UI login:
   `airflow users create
--username name
--firstname name
--lastname bs
--role Admin
--email email id
--password your password `

3. Run Airflow webserver: `airflow webserver -p 8080`

4. Start Airflow scheduler: `airflow scheduler`

### MLflow Setup
1. Start MLflow tracking server: `mlflow serve --model-uri <path_to_sqlite_db> --port <port_number> --host <host_address>`


## Usage
1. Clone the repository: https://github.com/Akalbir17/MLOps_Lead_Scoring.git

2. Install the required dependencies: `pip install -r requirements.txt`

3. Set up Airflow and MLflow as described in the [Setup](#setup) section.

4. Run the data pipeline, training pipeline, and inference pipeline using Airflow.

5. Access the Airflow UI at `http://localhost:8080` to monitor and manage the pipelines.

6. View the model experiment results and logged models in the MLflow UI.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Conclusion
In this project, we developed a lead scoring system to predict the likelihood of a lead purchasing the product. By leveraging data preprocessing, model experimentation using Pycaret, and pipeline orchestration with Airflow, we were able to build an efficient and automated solution. The best-performing model, LightGBM, achieved an accuracy of `89%`. This system will help the ed-tech startup reduce its customer acquisition cost by focusing on high-quality leads and optimizing its marketing efforts.

