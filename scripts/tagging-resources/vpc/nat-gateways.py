import boto3
from config import region, tags

def tag_nat_gateways():
    # Create an EC2 client
    ec2 = boto3.client('ec2', region_name=region)

    # Retrieve all NAT Gateways in the region
    response = ec2.describe_nat_gateways()

    # Iterate through NAT Gateways
    for nat_gateway in response['NatGateways']:
        gateway_id = nat_gateway['NatGatewayId']

        # Tag the NAT Gateway with the specified tags from the config file
        ec2.create_tags(
            Resources=[gateway_id],
            Tags=tags
        )

        print(f"NAT Gateway {gateway_id} tagged with {tags}")

if __name__ == "__main__":
    # Import region and tags from the config file
    from config import region, tags

    # Call the function to tag NAT Gateways
    tag_nat_gateways()
