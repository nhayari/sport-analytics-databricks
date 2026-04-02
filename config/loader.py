# config/loader.py
import os
os.environ["ENV"] = "prod"
ENV = os.getenv("ENV", "prod")

BRONZE_DB = "bronze"

# -----------------------------------
# Détection propre de dbutils
# -----------------------------------
dbutils = globals().get("dbutils", None)

# -----------------------------------
# Fonction secrets universelle
# -----------------------------------
def get_secret(scope, key, default=None):
    if dbutils:
        try:
            return dbutils.secrets.get(scope=scope, key=key)
        except Exception:
            return default
    return default

# -----------------------------------
# Config PostgreSQL
# -----------------------------------
if ENV == "prod":
    POSTGRES_CONFIG = {
        "url": f"jdbc:postgresql://{get_secret('prod', 'pg_host', 'prod-host-test')}:5432/sport_db",
        "user": get_secret("prod", "pg_user", "prod_user_test"),
        "password": get_secret("prod", "pg_password", "prod_password_test"),
        "driver": "org.postgresql.Driver"
    }
else:
    POSTGRES_CONFIG = {
        "url": f"jdbc:postgresql://bddatahub.ck2iq8vqjsru.eu-west-3.rds.amazonaws.com:5432/bddatahub",
        "user": get_secret("dev", "pg_user", "ifdis"),
        "password": get_secret("dev", "pg_password", "my_password"),
        "driver": "org.postgresql.Driver"
    } 

    
"""     POSTGRES_CONFIG = {
        "url": f"jdbc:postgresql://{get_secret('dev', 'pg_host', '192.168.1.31')}:5432/bddatahub",
        "user": get_secret("dev", "pg_user", "ifdis"),
        "password": get_secret("dev", "pg_password", "my_password"),
        "driver": "org.postgresql.Driver"
    } """
