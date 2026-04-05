from databricks.connect import DatabricksSession
from databricks.sdk import WorkspaceClient

print("=== Test de connexion Serverless ===")

spark = DatabricksSession.builder.serverless().profile("DEFAULT").getOrCreate()

print("✅ SparkSession Serverless créée avec succès")
print("Version Spark :", spark.version)

# Informations importantes sur le contexte actuel
print("\n--- Contexte actuel ---")
print("Current Catalog :", spark.catalog.currentCatalog())
print("Current Database :", spark.catalog.currentDatabase())



# Liste des catalogs disponibles
print("\n--- Catalogs disponibles ---")
spark.sql("SHOW CATALOGS").show(truncate=False)

# Test sur le catalog samples (correctement qualifié)
print("\n--- Test samples catalog ---")
try:
    spark.sql("SHOW SCHEMAS IN samples").show(truncate=False)
    print("✅ Catalog 'samples' accessible")
except Exception as e:
    print("Erreur sur samples :", e)

# Test d'une table connue (nyctaxi est souvent disponible)
print("\n--- Lecture d'une table sample (nyctaxi) ---")
try:
    df = spark.read.table("samples.nyctaxi.trips")
    df.select("tpep_pickup_datetime", "trip_distance", "fare_amount").show(5)
    print(f"✅ Table samples.nyctaxi.trips lue avec succès ({df.count()} lignes au total)")
except Exception as e:
    print("Erreur lecture nyctaxi :", str(e)[:300])