# Snowflake Native App: Product Sales Comparison

This project is a Snowflake Native Application that compares customer sales data with regional sales data using an interactive Streamlit dashboard. It leverages Snowflake's secure data sharing, UDFs, and reference management to provide dynamic insights into sales performance.

https://training.snowflake.com/content-player/app/sf/play/rco/146715256?in_sessionid=431A84219J400101&ctx_classroomId=146715273&ctx_in_from_module=CLMSCURRENTLEARNING.PRMAIN&navigateHome=true&ctx_in_lp_id=0&ctx_in_filter=%2526in_orderBy%253DNA%2526in_courseGroup%253DAll

## Project Structure

```
.
├── data/
│   ├── customer_sales_data.csv
│   └── regional_sales_data.csv
├── src/
│   ├── manifest.yml
│   ├── libraries/
│   │   ├── environment.yml
│   │   ├── streamlit.py
│   │   └── udf.py
│   └── scripts/
│       └── setup.sql
├── .gitignore
└── README.md
```

## Output-

![image](https://github.com/user-attachments/assets/568ea81e-a782-42f6-bdc5-9a514206738d)

Snowflake app

![image](https://github.com/user-attachments/assets/cf1e7ee8-26eb-4ea3-bd98-17fdd0a56674)


![image](https://github.com/user-attachments/assets/0b291731-1a1b-45ad-853b-fe2e745666dc)


## Features

- **Streamlit Dashboard**: Interactive web UI for comparing customer and regional sales.
- **Custom UDF**: Calculates percentage difference between customer and regional sales.
- **Reference Management**: Securely references customer sales data using Snowflake's reference system.
- **Automated Setup**: SQL scripts to initialize roles, schemas, views, and deploy the app.

## Getting Started

### 1. Prerequisites

- Snowflake account with appropriate privileges
- Snowflake Native Apps enabled
- Python 3.8+ (for local development/testing)

### 2. Setup Database and Application

Run the setup SQL script to create the necessary database objects:

```sql
-- In Snowflake Worksheet
USE ROLE ACCOUNTADMIN;
CREATE OR REPLACE DATABASE NATIVE_APP_DB;
-- ...see src/scripts/setup.sql for full setup
```

### 3. Upload Data

Upload the CSV files in the `data/` directory to the appropriate Snowflake stage and load them into tables:

```sql
COPY INTO native_app_db.native_app_schema.customer_sales
  FROM @native_app_package.native_app_schema.native_app_stage/data/customer_sales_data.csv;

COPY INTO native_app_db.native_app_schema.regional_sales
  FROM @native_app_package.native_app_schema.native_app_stage/data/regional_sales_data.csv;
```

### 4. Deploy the Application

- Build and deploy the application package as described in your setup scripts.
- Grant necessary permissions and create the application instance.

### 5. Using the App

- Access the Streamlit dashboard from within Snowflake.
- Compare sales data and view percentage differences interactively.

## File Descriptions

- `data/`: Contains sample CSV data for customer and regional sales.
- `src/libraries/streamlit.py`: Streamlit app code for the dashboard.
- `src/libraries/udf.py`: Python UDF for percentage difference calculation.
- `src/scripts/setup.sql`: SQL script to initialize Snowflake objects.
- `src/manifest.yml`: Application manifest for Snowflake Native Apps.
- `src/libraries/environment.yml`: Python environment dependencies.
