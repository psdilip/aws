import boto3
from west import region, tags

def tag_s3_buckets():
    # Create an S3 client
    s3 = boto3.client('s3', region_name=region)

    # Retrieve all S3 buckets in the region
    response = s3.list_buckets()

    # Iterate through buckets
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']

        # Tag the bucket with the specified tags from the config file
        s3.put_bucket_tagging(
            Bucket=bucket_name,
            Tagging={'TagSet': tags}
        )

        print(f"Bucket {bucket_name} tagged with {tags}")

if __name__ == "__main__":
    # Import region and bucket_tags from the config file
    from west import region, tags

    # Call the function to tag S3 buckets
    tag_s3_buckets()