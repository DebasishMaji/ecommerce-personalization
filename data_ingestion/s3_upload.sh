#!/bin/bash
# Replace 'your-s3-bucket' and 'ecommerce-personalization/raw' with your bucket and prefix
BUCKET="your-s3-bucket"
PREFIX="ecommerce-personalization/raw"
echo "Uploading raw data to s3://\$BUCKET/\$PREFIX/..."
aws s3 cp data/raw/ s3://\$BUCKET/\$PREFIX/ --recursive
echo "Data uploaded successfully."
