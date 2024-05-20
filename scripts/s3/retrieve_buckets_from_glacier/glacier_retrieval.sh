#!/bin/bash

# Set the S3 bucket name
BUCKET_NAME="detonator-algo-data"

# List all objects in the bucket (including those in Glacier)
# and process them one by one
aws s3 ls s3://$BUCKET_NAME/ --recursive | while read -r line;
  do
  # Extract the object key (file name) from the listing
    FILE_NAME=$(echo $line|awk '{print $4}')

    # Print the object being restored
    echo "Restoring: $FILE_NAME"

    # Initiate a restore job for the object
    # Request retrieval to S3 standard storage class
    # Set temporary restore period to 1 day
    aws s3api restore-object --bucket $BUCKET_NAME --key $FILE_NAME --restore-request '{"Days": 1, "GlacierJobParameters": {"Tier": "Standard"}}'
  done
