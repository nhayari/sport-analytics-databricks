from databricks.connect import DatabricksSession
from databricks.sdk import WorkspaceClient

# === Connexion au Serverless Compute ===
spark = DatabricksSession.builder.serverless().profile("DEFAULT").getOrCreate()

# === dbutils (supporté : fs, secrets, et partiellement widgets) ===nourdatabricks
w = WorkspaceClient(profile="DEFAULT")
dbutils = w.dbutils

# Exemples d'utilisation (ça marche en local → exécuté sur Databricks)
print(dbutils.fs.ls("/Volumes/workspace/bronze_db/sport_analytics_volume/"))
# dbutils.secrets.get(scope="mon-scope", key="ma-cle")
# dbutils.fs.put("/tmp/test.txt", "Hello from local!", overwrite=True)


# dbutils = globals().get("dbutils", None)
# print(dbutils.secrets.get(scope="prod", key="pg_host"))
# print(dbutils.secrets.get(scope="prod", key="pg_user"))
# print(dbutils.secrets.get(scope="prod", key="pg_password"))
