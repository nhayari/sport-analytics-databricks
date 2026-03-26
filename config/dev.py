# Configuration for only dev test environment
from .base import *

ENV = "dev"

POSTGRES_CONFIG = {
    "url": "jdbc:postgresql://dev-host:5432/db",
    "user": "dev_user",
    "password": "dev_password",
    "driver": "org.postgresql.Driver"
}

