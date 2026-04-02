dbutils = globals().get("dbutils", None)
print(dbutils.secrets.get(scope="prod", key="pg_host"))
print(dbutils.secrets.get(scope="prod", key="pg_user"))
print(dbutils.secrets.get(scope="prod", key="pg_password"))