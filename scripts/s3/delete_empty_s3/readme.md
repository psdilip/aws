# README

This script is designed to delete empty S3 buckets in all available AWS regions.

## Prerequisites

AWS credentials configured with appropriate permissions to manage S3 buckets
- Python 3.x installed with the boto3 library

## Usage

1. Run the script: `python delete_empty_s3.py`
2. The script will iterate through all available AWS regions
3. For each region, it will list all S3 buckets
4. Empty buckets will be detected and deleted
5. Non-empty buckets will be skipped

## Notes

This script will delete all empty S3 buckets across all regions in your AWS account.
Be cautious when running this script, as it can permanently delete data.
It is recommended to review the script and understand its functionality before running it in a production environment.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.