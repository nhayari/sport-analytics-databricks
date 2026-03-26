# Configuration for only production environment
from .base import *

ENV = "prod"

""" POSTGRES_CONFIG = {
    "url": "jdbc:postgresql://prod-host:5432/db",
    "user": "prod_user",
    "password": "prod_password",
    "driver": "org.postgresql.Driver"
} """

POSTGRES_CONFIG = {
    "url": f"jdbc:postgresql://{dbutils.secrets.get(scope=scope, key='pg_host')}:5432/<database>",
    "user": dbutils.secrets.get(scope=scope, key='pg_user'),
    "password": dbutils.secrets.get(scope=scope, key='pg_password'),
    "driver": "org.postgresql.Driver"
}