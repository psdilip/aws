import boto3
from config import region, tags

def tag_rds_instances():
    # Create an RDS client
    rds = boto3.client('rds', region_name=region)

    # Retrieve all RDS instances in the region
    response = rds.describe_db_instances()

    # Iterate through RDS instances
    for db_instance in response['DBInstances']:
        db_instance_identifier = db_instance['DBInstanceIdentifier']

        # Tag the RDS instance with the specified tags from the config file
        rds.add_tags_to_resource(
            ResourceName=db_instance_identifier,
            Tags=tags
        )

        print(f"RDS instance {db_instance_identifier} tagged with {tags}")

if __name__ == "__main__":
    # Import region and tags from the config file
    from config import region, tags

    # Call the function to tag RDS instances
    tag_rds_instances()
