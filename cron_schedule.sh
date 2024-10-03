# Cron job to run ETL script every day at midnight
0 0 * * * python /app/etl_pipeline.py >> /app/cron.log 2>&1
