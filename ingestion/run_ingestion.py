from postgres_to_bronze import ingest_table

def main():
    ingest_table("users", "id", "updated_at")
    ingest_table("athletes", "id", "updated_at")
    ingest_table("coachs", "id", "updated_at")
    ingest_table("feedbacks", "id", "updated_at")

if __name__ == "__main__":
    main()
