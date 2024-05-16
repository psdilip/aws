# README

This script is designed to move all S3 buckets in all available AWS regions to the Glacier Deep Archive Storage class, except for the buckets specified in the excluded_buckets list.

## Prerequisites

- AWS credentials configured with appropriate permissions to manage S3 buckets and lifecycle policies
- Python 3.x installed with the boto3 library

## Usage

1. Open the script in a text editor.
2. Update the `excluded_buckets` list with the names of the buckets you want to exclude from the storage class change.
3. Save the script.
4. Run the script: `python script.py`
5. The script will iterate through all available AWS regions and buckets.
6. For each bucket (excluding the specified ones), the script will:
    - Enable versioning for the bucket
    - Set the lifecycle policy to transition all objects to Glacier Deep Archive Storage class immediately
7. The script will print the status of each operation (success or error).

## Notes

- Moving data to Glacier Deep Archive Storage class is a one-way operation, and you cannot transition the data back to a different storage class directly.
- Be cautious when running this script, as it can have significant impacts on your S3 data storage costs.
- It is recommended to review the script and understand its functionality before running it in a production environment.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.