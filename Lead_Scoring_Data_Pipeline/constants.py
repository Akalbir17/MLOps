# You can create more variables according to your project. The following are the basic variables that have been provided to you
DB_PATH = "/home/airflow/dags/Lead_scoring_data_pipeline/"
DB_FILE_NAME = "lead_scoring_data_cleaning.db"
#DB_FILE_NAME = "lead_scoring_data_cleaning_inference.db"
UNIT_TEST_DB_FILE_NAME = 'unit_test_cases.db'
DATA_DIRECTORY = "/home/airflow/dags/Lead_scoring_data_pipeline/data/"
DATA_FILE = 'leadscoring_inference.csv'
#DATA_FILE = 'leadscoring_inference.csv'
MAPPING_DIRECTORY = "/home/airflow/dags/Lead_scoring_data_pipeline/mapping/"
INTERACTION_MAPPING = MAPPING_DIRECTORY+"interaction_mapping.csv"
INDEX_COLUMNS = ['created_date', 'city_tier', 'first_platform_c', 'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped', 'referred_lead', 'app_complete_flag']
NOT_FEATURES = ""
