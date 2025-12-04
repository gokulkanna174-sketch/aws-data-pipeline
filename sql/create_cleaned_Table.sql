CREATE EXTERNAL TABLE IF NOT EXISTS sales_database.cleaned_sales_data (
  store bigint,
  date string,
  weekly_sales double,
  holiday_flag bigint,
  temperature double,
  fuel_price double,
  cpi double,
  unemployment double
)
STORED AS PARQUET
LOCATION 's3://gokul-data-pipeline-bucket/processed/sales/';

