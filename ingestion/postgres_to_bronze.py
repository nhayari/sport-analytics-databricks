from databricks.connect import DatabricksSession
from databricks.sdk import WorkspaceClient
from config.loader import BRONZE_DB, POSTGRES_CONFIG

print("=== Ingestion PostgreSQL → Bronze Layer (Serverless) ===")

# ------------ CONNEXION SERVERLESS ------------
spark = DatabricksSession.builder.serverless().profile("DEFAULT").getOrCreate()

# ------------ CONFIGURATION POSTGRESQL ------------

# Liste des tables à ingérer 
tables_to_ingest = [
    "public.users",
    "public.athletes",
    "public.feedback"
]

# ------------ CATALOG + SCHEMA BRONZE ------------
catalog = "workspace"                    # ou "workspace" si c'est ton catalog par défaut
            # on crée le schéma bronze si besoin

# Création du schéma bronze s'il n'existe pas
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{BRONZE_DB}")
print(f"✅ Schéma {catalog}.{BRONZE_DB} prêt")
print(f"✅ url a "+POSTGRES_CONFIG["url"])
 




# ------------ INGESTION DES TABLES ------------
for table in tables_to_ingest:
    try:
        # Nom de la table dans PostgreSQL (ex: public.matchs)
        pg_table = table
        
        # Nom de la table Delta dans Bronze (ex: bronze.matchs)
        bronze_table = table.split('.')[-1]   # on garde seulement le nom de la table
        
        print(f"\n→ Ingestion de la table PostgreSQL : {pg_table} ...")

        df = (spark.read
              .format("jdbc")
              .option("url", POSTGRES_CONFIG["url"])
              .option("dbtable", pg_table)
              .option("user", POSTGRES_CONFIG["user"])
              .option("password", POSTGRES_CONFIG["password"])
              .option("driver", POSTGRES_CONFIG["driver"])
              # Options de performance (recommandé)
              .option("fetchsize", "10000")        # nombre de lignes par batch
              .option("numPartitions", "8")        # à ajuster selon la taille de tes tables
              # .option("partitionColumn", "id")    # à activer si tu as une colonne numérique pour le partitionnement
              # .option("lowerBound", "1")
              # .option("upperBound", "1000000")
             ).load()

        # Écriture en mode overwrite ou append selon ton besoin
        target_table = f"{catalog}.{BRONZE_DB}.{bronze_table}"

        (df.write
           .format("delta")
           .mode("overwrite")           # ← change en "append" si tu veux des chargements incrémentaux
           .option("overwriteSchema", "true")
           .saveAsTable(target_table))

        row_count = df.count()
        print(f"✅ {pg_table} → {target_table}  |  {row_count:,} lignes ingérées")

    except Exception as e:
        print(f"❌ Erreur sur la table {table} : {str(e)[:300]}")

print("\n🎉 Ingestion PostgreSQL → Bronze terminée !")

