import boto3
from west import region, tags

def tag_ec2_instances():
    # Create an EC2 client
    ec2 = boto3.client('ec2', region_name=region)

    # Retrieve all EC2 instances in the region
    response = ec2.describe_instances()

    # Iterate through reservations (group of instances)
    for reservation in response['Reservations']:
        # Iterate through instances in the reservation
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']

            # Tag the instance with the specified tags from the config file
            ec2.create_tags(
                Resources=[instance_id],
                Tags=tags
            )

            print(f"Instance {instance_id} tagged with {tags}")

if __name__ == "__main__":
    # Import region and instance_tags from the config file
    from west import region, tags

    # Call the function to tag EC2 instances
    tag_ec2_instances()
