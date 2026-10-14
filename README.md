# Global Superstore – Task 1: Data Cleaning & Preparation

## Project
**Global E-Commerce Sales & Profitability Intelligence**

This repository contains the Task 1 data-cleaning work for the Global Superstore analytics project.

## Objective
Clean and prepare the raw public dataset for further Exploratory Data Analysis (Task 2), Power BI Dashboard (Task 3), and Final Analytics Case Study (Task 4).

## Dataset
Raw file:
`data/raw/global_superstore_raw.xlsm`

The dataset contains e-commerce order, customer, product, sales, shipping and profitability information.

## Cleaning performed
The cleaning script checks and prepares the dataset by:
- standardizing column names
- removing completely empty rows and columns
- trimming unnecessary whitespace from text fields
- converting date columns to proper date format
- converting numeric columns to numeric data types
- checking missing values
- checking duplicate records
- checking inconsistent/blank text values
- exporting the cleaned dataset as CSV

## How to run
1. Put `global_superstore_raw.xlsm` inside `data/raw/`.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run:
   `python cleaning/clean_data.py`
4. The cleaned file will be created at:
   `data/cleaned/global_superstore_cleaned.csv`

## Output
`global_superstore_cleaned.csv` is the dataset that will be used for:
- Task 2: Exploratory Data Analysis
- Task 3: Interactive Power BI Dashboard
- Task 4: Final Data Analytics Project

## Tools
- Python
- Pandas
- OpenPyXL

## Task
**Task 1 – Data Cleaning & Preparation**
