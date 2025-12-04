from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

import sys
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load from Glue Catalog
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database="sales_database",
    table_name="gokul_data_pipeline_bucket",
    transformation_ctx="datasource0"
)

# Map columns properly
applymapping1 = ApplyMapping.apply(
    frame=datasource0,
    mappings=[
        ("Store", "string", "Store", "string"),
        ("Date", "string", "Date", "string"),
        ("Weekly_Sales", "string", "Weekly_Sales", "double"),
        ("Holiday_Flag", "string", "Holiday_Flag", "string"),
        ("Temperature", "string", "Temperature", "double"),
        ("Fuel_Price", "string", "Fuel_Price", "double"),
        ("CPI", "string", "CPI", "double"),
        ("Unemployment", "string", "Unemployment", "double")
    ],
    transformation_ctx="applymapping1"
)

# Write as Parquet
datasink2 = glueContext.write_dynamic_frame.from_options(
    frame=applymapping1,
    connection_type="s3",
    connection_options={"path": "s3://gokul-data-pipeline-bucket/processed/sales/"},
    format="parquet",
    transformation_ctx="datasink2"
)

job.commit()

