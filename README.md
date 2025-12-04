1. Project Title

AWS Data Pipeline: S3 → Glue → Athena (Sales Data Analytics)

2. Project Description

This project demonstrates how to build a complete serverless data engineering pipeline using Amazon S3, AWS Glue, and Amazon Athena.
The pipeline loads raw CSV data into S3, catalogs it using Glue Crawler, transforms it using a Glue ETL job, stores the cleaned data as Parquet, and finally analyzes it through Athena SQL queries.

3. Architecture Overview

The end-to-end workflow is:

Upload raw CSV to Amazon S3

Run AWS Glue Crawler → detect schema

AWS Glue stores metadata in the Data Catalog

AWS Glue ETL job reads the raw data and converts it to Parquet

Cleaned data is stored back to S3 in a processed folder

Athena reads the Parquet files and allows SQL analysis

Analytical insights are generated (store performance, holiday trends, etc.)

4. Dataset Description

The dataset contains retail store weekly sales information with the following columns:

Store

Date

Weekly Sales

Holiday Flag

Temperature

Fuel Price

CPI

Unemployment

5. AWS Services Used

Amazon S3 – storage for raw and processed data

AWS Glue Crawler – automatic schema detection

AWS Glue Data Catalog – centralized metadata store

AWS Glue ETL Job – transformation using PySpark

Amazon Athena – SQL querying on S3 data

6. Steps Performed in the Project
6.1 Upload Raw Data

The CSV file sales_data.csv was uploaded to the S3 bucket:
gokul-data-pipeline-bucket/raw/

6.2 Create Glue Crawler

A crawler named sales-data-crawler was created

It scanned the S3 raw folder

It created a table named gokul_data_pipeline_bucket in the Glue Data Catalog inside the database sales_database

6.3 Create Glue ETL Job

Job name: sales-etl-job

The ETL job:

Reads the raw table

Applies schema mapping

Converts CSV to Parquet

Writes Parquet to:
s3://gokul-data-pipeline-bucket/processed/sales/

After running the job, Parquet files were successfully generated.

6.4 Create Athena Table for Processed Data

An Athena external table named cleaned_sales_data was created

It reads data from the processed Parquet directory

6.5 Run Analytics Queries

Analytics performed include:

Total sales

Store-wise sales

Holiday vs non-holiday comparison

Temperature impact on sales

Top 10 sales weeks

7. Project Folder Structure

The repository contains:

README.md – project description

architecture/ – architecture diagram image

sql/ – all SQL scripts used in Athena

glue/ – ETL Python script and configuration files

screenshots/ – all AWS console screenshots

report/ – full project report document

8. SQL Scripts Included

The SQL folder contains:

Script to create processed table

Script to preview raw table

Script to preview cleaned table

Analytics queries for:

Total sales

Store performance

Holiday impact

Temperature correlation

Top performing weeks

9. Glue Scripts Included

The Glue folder contains:

ETL Script (PySpark) used in Glue job

Configuration file for the crawler

Job details in JSON format

10. Screenshots

All screenshots proving the project steps are placed in the screenshots folder:

S3 raw data

S3 processed parquet files

Glue crawler run success

Glue ETL job success

Athena tables

Athena query results

11. Final Project Report

The report folder contains:
project_report.md
This includes:

Introduction

Architecture diagram

Explanation of each AWS service

SQL queries and results

Screenshots

Conclusion

12. Conclusion

This project successfully implements a fully functional AWS Data Lake pipeline using serverless technologies.
The solution is scalable, cost-efficient, and demonstrates real-world data engineering skills including:

Data ingestion

Metadata management

ETL transformation

Parquet optimization

SQL analytics

This pipeline can be extended with automation (Lambda), dashboards (QuickSight), and orchestration (Glue Workflows).
