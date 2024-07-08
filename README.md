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
- [Repository Structure](#repository-structure)
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
- Detailed preprocessing and EDA steps can be found in the [Data Preprocessing & EDA notebook](link_to_notebook).

### Model Experimentation
- Utilized Pycaret, an open-source machine learning library, for model experimentation.
- Performed initial experiments to identify irrelevant features and removed them in subsequent runs.
- Logged models to MLflow registry for tracking and comparison.
- Detailed model experimentation steps can be found in the [Model Experimentation notebook](link_to_notebook).

### Pipelines
- Developed data, training, and inference pipelines using Airflow for streamlined processing.
- Data Pipeline: Processes the raw data.
- Training Pipeline: Performs preprocessing and model training.
- Inference Pipeline: Handles preprocessing and model prediction.

### Test Cases
- Implemented unit test cases using pytest to validate preprocessing functionalities.
- Tested load_data_to_db function, city-to-tier mapping, categorical variable mapping, and interaction mapping schema.
- Test cases can be found in the [https://github.com/Akalbir17/MLOps/tree/main/Unit_Test](link_to_test_cases_file).

## Results
- Identified LightGBM, an XGBoost classification algorithm, as the best-performing model based on accuracy.
- Achieved an accuracy of `89%` in predicting whether a lead will purchase the product or not.

