# Configuration for only dev test environment
from .base import *

ENV = "dev"

POSTGRES_CONFIG = {
    "url": "jdbc:postgresql://dev-host:5432/db",
    "user": "dev_user",
    "password": "dev_password",
    "driver": "org.postgresql.Driver"
}





""" import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Configuration Databricks
DATABRICKS_HOST = os.getenv("DATABRICKS_HOST", "https://dbc-cbe6abcf-4629.cloud.databricks.com")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")

# Configuration PostgreSQL
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "postgres")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

# Configuration Catalog/Schema
CATALOG = os.getenv("CATALOG", "hive_metastore")
BRONZE_DATABASE = os.getenv("BRONZE_DATABASE", "bronze")
SILVER_DATABASE = os.getenv("SILVER_DATABASE", "silver")
GOLD_DATABASE = os.getenv("GOLD_DATABASE", "gold")

# Configuration ingestion
POSTGRES_TABLE = os.getenv("POSTGRES_TABLE", "users")
DELTA_TABLE_NAME = os.getenv("DELTA_TABLE_NAME", "users")

# Validation
if not DATABRICKS_TOKEN:
    raise ValueError("DATABRICKS_TOKEN manquant dans les variables d'environnement")
 """

