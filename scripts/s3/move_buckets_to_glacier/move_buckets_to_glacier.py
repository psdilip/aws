import boto3
from botocore.exceptions import ClientError

"""
This script moves all S3 buckets in all regions to the Glacier Deep Archive Storage class,
except for the buckets specified in the excluded_buckets list.

Prerequisites:
- AWS credentials configured with appropriate permissions to manage S3 buckets and lifecycle policies
- Python 3.x installed with the boto3 library

Usage:
1. Update the excluded_buckets list with the names of the buckets you want to exclude
2. Run the script
3. The script will iterate through all available AWS regions and buckets
4. For each bucket (excluding the specified ones), the script will:
    - Enable versioning for the bucket
    - Set the lifecycle policy to transition all objects to Glacier Deep Archive Storage class immediately
5. The script will print the status of each operation (success or error)

Note:
- Moving data to Glacier Deep Archive Storage class is a one-way operation, and you cannot transition
  the data back to a different storage class directly.
- Be cautious when running this script, as it can have significant impacts on your S3 data storage costs.
"""

# Create an AWS session
session = boto3.Session()

# Get all available regions
ec2 = session.client('ec2')
regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]

# Get the list of buckets to exclude
# Update this list with the names of the buckets you want to exclude
excluded_buckets = ["biosecurity-algo-data", "biosecurity-algo-dvc"]

# Iterate over all regions
for region in regions:
    # Create an S3 resource for the current region
    s3 = session.resource('s3', region_name=region)

    # Get all buckets in the current region
    buckets = s3.buckets.all()

    # Iterate over each bucket
    for bucket in buckets:
        bucket_name = bucket.name

        # Skip the bucket if it's in the excluded list
        if bucket_name in excluded_buckets:
            print(f"Skipping bucket {bucket_name} in {region}")
            continue

        # Set the bucket's storage class to Glacier Deep Archive
        try:
            # Enable versioning for the bucket
            bucket_versioning = bucket.Versioning()
            bucket_versioning.enable()

            # Set the lifecycle policy
            bucket_lifecycle_configuration = bucket.LifecycleConfiguration()
            response = bucket_lifecycle_configuration.put(
                LifecycleConfiguration={
                    'Rules': [
                        {
                            'ID': 'TransitionToGlacierDeepArchive',
                            'Prefix': '',
                            'Status': 'Enabled',
                            'Transitions': [
                                {
                                    'Days': 0,
                                    'StorageClass': 'DEEP_ARCHIVE'
                                }
                            ]
                        },
                    ]
                }
            )
            print(response)
            print(f"Moved bucket {bucket_name} in {region} to Glacier Deep Archive Storage class")
        except ClientError as e:
            if e.response['Error']['Code'] == 'MalformedXML':
                print(f"Error moving bucket {bucket_name} in {region}: {e.response['Error']['Message']}")
            else:
                print(f"Error moving bucket {bucket_name} in {region}: {e}")
        except Exception as e:
            print(f"Error moving bucket {bucket_name} in {region}: {e}")