import boto3
from config import region, tags

def tag_security_groups():
    # Create an EC2 client
    ec2 = boto3.client('ec2', region_name=region)

    # Retrieve all security groups in the region
    response = ec2.describe_security_groups()

    # Iterate through security groups
    for security_group in response['SecurityGroups']:
        group_id = security_group['GroupId']

        # Tag the security group with the specified tags from the config file
        ec2.create_tags(
            Resources=[group_id],
            Tags=tags
        )

        print(f"Security Group {group_id} tagged with {tags}")

if __name__ == "__main__":
    # Import region and tags from the config file
    from config import region, tags

    # Call the function to tag security groups
    tag_security_groups()
