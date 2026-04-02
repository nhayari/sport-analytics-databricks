from pyspark.sql import SparkSession
from config.loader import POSTGRES_CONFIG

def main():
    # Créer SparkSession
    spark = SparkSession.builder \
        .appName("Test PostgreSQL Connection") \
        .getOrCreate()

    try:
        # Lire une table pour tester la connexion
        df = (spark.read
              .format("jdbc")
              .option("url", POSTGRES_CONFIG["url"])
              .option("dbtable", "users")  # petite table test
              .option("user", POSTGRES_CONFIG["user"])
              .option("password", POSTGRES_CONFIG["password"])
              .option("driver", POSTGRES_CONFIG["driver"])
              .load())

        print("✅ Connexion réussie ! Nombre de lignes :", df.count())
        df.show(5)

    except Exception as e:
        print("❌ Erreur de connexion :", e)

    finally:
        spark.stop()

if __name__ == "__main__":
    main()