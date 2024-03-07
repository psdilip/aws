import boto3
from config import region, tags

def tag_subnets():
    # Create a VPC client
    ec2 = boto3.client('ec2', region_name=region)

    # Retrieve all subnets in the region
    response = ec2.describe_subnets()

    # Iterate through subnets
    for subnet in response['Subnets']:
        subnet_id = subnet['SubnetId']

        # Tag the subnet with the specified tags from the config file
        ec2.create_tags(
            Resources=[subnet_id],
            Tags=tags
        )

        print(f"Subnet {subnet_id} tagged with {tags}")

if __name__ == "__m
