import boto3
from config import region, tags

def tag_route_tables():
    # Create an EC2 client
    ec2 = boto3.client('ec2', region_name=region)

    # Retrieve all route tables in the region
    response = ec2.describe_route_tables()

    # Iterate through route tables
    for route_table in response['RouteTables']:
        table_id = route_table['RouteTableId']

        # Tag the route table with the specified tags from the config file
        ec2.create_tags(
            Resources=[table_id],
            Tags=tags
        )

        print(f"Route Table {table_id} tagged with {tags}")

if __name__ == "__main__":
    # Import region and tags from the config file
    from config import region, tags

    # Call the function to tag route tables
    tag_route_tables()
