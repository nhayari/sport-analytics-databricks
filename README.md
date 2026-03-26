Sport Analytics Data Platform

Pipeline Databricks pour analyser les performances sportives.

Architecture:
PostgreSQL → Databricks → Delta Lake → Dashboard

Analyses:
- performances athlètes
- séances par activité
- satisfaction des sportifs
- évolution des thèmes d'entraînement


## process 
Changer d’environnement ?
 - En local (VSCode)
       export ENV=dev  
       # ou
       export ENV=prod

 - ajouter variable d’environnement :
        ENV = prod      



databricks configure --token
chmod +x add_secrets.sh
./add_secrets.sh






