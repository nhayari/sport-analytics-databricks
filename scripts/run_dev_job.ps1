# -------------------------------
# CONFIGURATION
# -------------------------------

# Chemin local du projet à synchroniser
$local_project = "C:\worknour\tolearn\sport-analytics-databricks"

# Chemin Repos Databricks (où ton projet sera uploadé)
$databricks_repo_path = "/Repos/sport/sport-analytics-databricks"
#databricks_repo_path = "/Workspace/Users/noureddine.hayari@gmail.com/sport-analytics-databricks"


# Nom du script Python à exécuter
$python_script = "tests/test.py"

# Nom du job Databricks
$job_name = "dev_test_ingestion"

# ID du cluster existant Databricks Free 2026
$cluster_id = "1badf0f602f74add"

# -------------------------------
# 1️⃣ Uploader le projet dans Databricks Repos
# -------------------------------
Write-Host "📤 Upload du projet vers Databricks Repos..."
databricks workspace import_dir "$local_project" "$databricks_repo_path" --overwrite

# -------------------------------
# 2️⃣ Créer le fichier JSON pour le job
# -------------------------------
$job_json = @{
    name = $job_name
    existing_cluster_id = $cluster_id
    spark_python_task = @{
        python_file = "$databricks_repo_path/$python_script"
    }
} | ConvertTo-Json -Depth 5

$job_file = "$env:TEMP\job_config.json"
$job_json | Out-File -Encoding UTF8 $job_file

# -------------------------------
# 3️⃣ Créer le job Databricks
# -------------------------------
Write-Host "🛠️ Création du job Databricks..."
$job_create_output = databricks jobs create --json-file $job_file --output JSON | ConvertFrom-Json
$job_id = $job_create_output.job_id
Write-Host "✅ Job créé avec ID : $job_id"

# -------------------------------
# 4️⃣ Lancer le job
# -------------------------------
Write-Host "🚀 Lancement du job..."
$run_output = databricks jobs run-now --job-id $job_id --output JSON | ConvertFrom-Json
$run_id = $run_output.run_id
Write-Host "✅ Run ID : $run_id"

# -------------------------------
# 5️⃣ Récupérer les logs du job
# -------------------------------
Start-Sleep -Seconds 5 # attendre le démarrage
Write-Host "📄 Logs du job :"
databricks runs get --run-id $run_id --output JSON | ConvertFrom-Json | Format-List