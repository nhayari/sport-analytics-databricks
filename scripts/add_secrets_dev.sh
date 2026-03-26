#!/bin/bash

# Nom de la DB
DATABASE_NAME="sport_db"

# Env dev
DEV_SCOPE="dev"
DEV_PG_HOST="dev-host.amazonaws.com"
DEV_PG_USER="dev_user"
DEV_PG_PASSWORD="dev_password"


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


create_scope $DEV_SCOPE
put_secret $DEV_SCOPE "pg_host" $DEV_PG_HOST
put_secret $DEV_SCOPE "pg_user" $DEV_PG_USER
put_secret $DEV_SCOPE "pg_password" $DEV_PG_PASSWORD
echo "✅ les secrets  dev ont été ajoutés"

