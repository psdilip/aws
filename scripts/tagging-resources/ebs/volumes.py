import boto3
from west import region, ebs_volume_tags

def tag_ebs_volumes():
    # Create an EC2 client
    ec2 = boto3.client('ec2', region_name=region)

    # Retrieve all EBS volumes in the region
    response = ec2.describe_volumes()

    # Iterate through volumes
    for volume in response['Volumes']:
        volume_id = volume['VolumeId']

        # Tag the volume with the specified tags from the config file
        ec2.create_tags(
            Resources=[volume_id],
            Tags=ebs_volume_tags
        )

        print(f"Volume {volume_id} tagged with {ebs_volume_tags}")

if __name__ == "__main__":
    # Import region and ebs_volume_tags from the config file
    from west import region, ebs_volume_tags

    # Call the function to tag EBS volumes
    tag_ebs_volumes()
