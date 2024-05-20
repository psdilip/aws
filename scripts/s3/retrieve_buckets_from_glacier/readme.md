# S3 Glacier Restore Script

This bash script is designed to restore objects from Amazon S3 Glacier to Amazon S3 standard storage class for a specified S3 bucket.

## Prerequisites

- AWS CLI installed and configured with appropriate permissions to access S3 and Glacier services.
- `awk` command installed (usually pre-installed on most Unix-like systems).

## Usage

1. Open the script in a text editor and update the `BUCKET_NAME` variable with the name of your S3 bucket.
2. Save the script and make it executable
`chmod +x glacier_retrieval.sh`
3. Run the script
`./restore_script.sh`

## How it works
The script will list all objects in the specified S3 bucket (including those in Glacier storage) and initiate a restore job for each object, requesting retrieval to the S3 standard storage class with a 1-day temporary restore period.
How it works

The script uses the aws s3 ls command to list all objects in the specified S3 bucket, including those in Glacier storage.
For each object listed, the script extracts the object key (file name) using awk.
The script then initiates a restore job for the object using the aws s3api restore-object command, specifying the bucket name, object key, and restore request parameters.
The restore request parameters include:

"Days": 1: Sets the temporary restore period to 1 day.
"GlacierJobParameters": {"Tier": "Standard"}: Instructs Glacier to restore the object to Amazon S3 standard storage class.

## Notes

The script assumes that the AWS CLI is configured with appropriate permissions to access S3 and Glacier services.
The restore jobs may take several hours to complete, depending on the size and number of objects being restored.
After the temporary restore period (1 day in this case), the restored objects will transition back to Glacier storage unless you move or copy them to a different S3 storage class.
Retrieving objects from Glacier and storing them in Amazon S3 standard storage class will incur additional costs for both the retrieval request and the storage of the retrieved objects in Amazon S3 standard class. Refer to the AWS Glacier pricing and the Amazon S3 pricing for more details.