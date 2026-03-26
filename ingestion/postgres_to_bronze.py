# ingestion/postgres_ingestion.py
from pyspark.sql import functions as F
from config.loader import BRONZE_DB, POSTGRES_CONFIG

def ingest_table(spark, table_name, primary_key, updated_at_col):
    """
    Ingestion depuis PostgreSQL vers Delta Bronze avec merge incrémental
    """
    # Lire depuis PostgreSQL
    df = (spark.read
          .format("jdbc")
          .option("url", POSTGRES_CONFIG["url"])
          .option("dbtable", table_name)
          .option("user", POSTGRES_CONFIG["user"])
          .option("password", POSTGRES_CONFIG["password"])
          .option("driver", POSTGRES_CONFIG["driver"])
          .load())
    
    df = df.withColumn("_ingestion_time", F.current_timestamp())
    target_table = f"{BRONZE_DB}.{table_name}"

    if not spark.catalog.tableExists(target_table):
        df.write.format("delta").mode("overwrite").saveAsTable(target_table)
    else:
        df.createOrReplaceTempView("source")
        spark.sql(f"""
        MERGE INTO {target_table} AS target
        USING source AS source
        ON target.{primary_key} = source.{primary_key}
        WHEN MATCHED AND source.{updated_at_col} > target.{updated_at_col}
          THEN UPDATE SET *
        WHEN NOT MATCHED
          THEN INSERT *
        """)