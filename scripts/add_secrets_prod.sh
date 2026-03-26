#!/bin/bash

# Nom de la DB
DATABASE_NAME="sport_db"


# Env prod
PROD_SCOPE="prod"
PROD_PG_HOST="prod-host.amazonaws.com"
PROD_PG_USER="prod_user"
PROD_PG_PASSWORD="prod_password"

create_scope() {
  SCOPE_NAME=$1
  echo "Création du scope : $SCOPE_NAME"
  databricks secrets create-scope --scope $SCOPE_NAME
}

put_secret() {
  SCOPE_NAME=$1
  KEY=$2
  VALUE=$3
  echo "Ajout du secret '$KEY' dans le scope '$SCOPE_NAME'"
  echo -n $VALUE | databricks secrets put --scope $SCOPE_NAME --key $KEY
}

create_scope $PROD_SCOPE
put_secret $PROD_SCOPE "pg_host" $PROD_PG_HOST
put_secret $PROD_SCOPE "pg_user" $PROD_PG_USER
put_secret $PROD_SCOPE "pg_password" $PROD_PG_PASSWORD
echo "✅ les secrets  prod ont été ajoutés"

