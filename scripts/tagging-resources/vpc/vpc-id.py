import boto3
from config import region, tags

def tag_vpcs():
    # Create a VPC client
    ec2 = boto3.client('ec2', region_name=region)

    # Retrieve all VPCs in the region
    response = ec2.describe_vpcs()

    # Iterate through VPCs
    for vpc in response['Vpcs']:
        vpc_id = vpc['VpcId']

        # Tag the VPC with the specified tags from the config file
        ec2.create_tags(
            Resources=[vpc_id],
            Tags=tags
        )

        print(f"VPC {vpc_id} tagged with {tags}")

if __name__ == "__main__":
    # Import region and tags from the config file
    from config import region, tags

    # Call the function to tag VPCs
    tag_vpcs()
