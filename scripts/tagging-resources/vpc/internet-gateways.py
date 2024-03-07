import boto3
from config import region, tags

def tag_internet_gateways():
    # Create a VPC client
    ec2 = boto3.client('ec2', region_name=region)

    # Retrieve all Internet Gateways in the region
    response = ec2.describe_internet_gateways()

    # Iterate through Internet Gateways
    for internet_gateway in response['InternetGateways']:
        gateway_id = internet_gateway['InternetGatewayId']

        # Tag the Internet Gateway with the specified tags from the config file
        ec2.create_tags(
            Resources=[gateway_id],
            Tags=tags
        )

        print(f"Internet Gateway {gateway_id} tagged with {tags}")

if __name__ == "__main__":
    # Import region and tags from the config file
    from config import region, tags

    # Call the function to tag Internet Gateways
    tag_internet_gateways()
