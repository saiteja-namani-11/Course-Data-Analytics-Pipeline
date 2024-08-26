#!/bin/bash 
python3 generate_data.py
mc alias set s3 http://minio:9000 minio $PASSWORD
mc mb -p s3/enrollments
echo "Writing data to s3..."
mc cp /app/data/enrollments.csv s3/enrollments/enrollments.csv
mc cp /app/data/sections.csv s3/enrollments/sections.csv
echo "DONE! dataloader is complete!"
exit 0
