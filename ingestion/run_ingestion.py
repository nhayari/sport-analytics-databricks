import os
from pyspark.sql import SparkSession
from postgres_to_bronze import ingest_table

def main():
    # Crée Spark session (local ou Databricks)
    spark = SparkSession.builder.appName("PostgresToBronze").getOrCreate()

    # Liste des tables à ingérer
    TABLES = [
        ("users", "id", "updated_at"),
        ("athletes", "id", "updated_at"),
        ("coachs", "id", "updated_at"),
        ("feedbacks", "id", "updated_at"),
    ]

    for table, pk, updated_col in TABLES:
        print(f" Ingestion de {table}")
        ingest_table(spark, table, pk, updated_col)

    spark.stop()

if __name__ == "__main__":
    main()