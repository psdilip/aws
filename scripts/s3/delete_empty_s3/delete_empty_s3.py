import boto3

def delete_empty_buckets(region):
    """
    Delete empty S3 buckets in the specified AWS region.

    Args:
        region (str): The AWS region in which to delete empty buckets.

    Returns:
        None
    """
    # Create an S3 client for the specified region
    s3 = boto3.client('s3', region_name=region)

    # Get a list of all buckets in the specified region
    response = s3.list_buckets()
    buckets = response['Buckets']

    # Iterate over each bucket
    for bucket in buckets:
        bucket_name = bucket['Name']

        # Check if the bucket is empty
        response = s3.list_objects_v2(Bucket=bucket_name)

        # If the 'Contents' key is not present or the list is empty, the bucket is empty
        if 'Contents' not in response or len(response['Contents']) == 0:
            print(f"Deleting empty bucket '{bucket_name}' in region '{region}'")
            # Delete the empty bucket
            s3.delete_bucket(Bucket=bucket_name)
        else:
            print(f"Skipping non-empty bucket '{bucket_name}' in region '{region}'")


def delete_empty_buckets_all_regions():
    """
    Delete empty S3 buckets in all available AWS regions.

    Returns:
        None
    """
    # Get a list of all available AWS regions for the S3 service
    all_regions = boto3.Session().get_available_regions('s3')

    # Delete empty S3 buckets in each region
    for region in all_regions:
        delete_empty_buckets(region)


if __name__ == "__main__":
    # Delete empty S3 buckets in all AWS regions
    delete_empty_buckets_all_regions()