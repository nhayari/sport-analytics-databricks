# tests/test_postgres_spark_connection.py

from pyspark.sql import SparkSession
from config.loader import POSTGRES_CONFIG, BRONZE_DB
import os
from config.loader import POSTGRES_CONFIG, ENV

print("ENV:", ENV)

def main():
    # ⚡ Crée la session Spark
    spark = SparkSession.builder.appName("TestPostgresConnection").getOrCreate()

    # 🔹 Affiche uniquement les valeurs safe
    print("🔹 Connexion PostgreSQL test")
    print("URL :", POSTGRES_CONFIG["url"])
    print("User:", POSTGRES_CONFIG["user"])
    print("Target Bronze DB:", BRONZE_DB)

    # ⚡ Essaye de lire un échantillon depuis la table 'athletes'
    try:
        df = (spark.read
              .format("jdbc")
              .option("url", POSTGRES_CONFIG["url"])
              .option("dbtable", "athletes")
              .option("user", POSTGRES_CONFIG["user"])
              .option("password", POSTGRES_CONFIG["password"])
              .option("driver", POSTGRES_CONFIG["driver"])
              .load())

        # 🔹 Affiche juste les 5 premières lignes
        df.show(5)
        print(f"✅ Connexion réussie, nb lignes récupérées : {df.count()}")

    except Exception as e:
        print("❌ Erreur lors de la connexion :")
        print(e)

if __name__ == "__main__":
    main()