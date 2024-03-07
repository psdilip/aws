import boto3
from config import region, tags

def tag_elastic_ips():
    # Create an EC2 client
    ec2 = boto3.client('ec2', region_name=region)

    # Retrieve all Elastic IPs in the region
    response = ec2.describe_addresses()

    # Iterate through Elastic IPs
    for address in response['Addresses']:
        allocation_id = address.get('AllocationId')
        association_id = address.get('AssociationId')

        # Tag the Elastic IP with the specified tags from the config file
        if allocation_id:
            ec2.create_tags(
                Resources=[allocation_id],
                Tags=tags
            )
            print(f"Elastic IP {allocation_id} tagged with {tags}")
        elif association_id:
            ec2.create_tags(
                Resources=[association_id],
                Tags=tags
            )
            print(f"Elastic IP (associated) {association_id} tagged with {tags}")

if __name__ == "__main__":
    # Import region and tags from the config file
    from config import region, tags

    # Call the function to tag Elastic IPs
    tag_elastic_ips()
