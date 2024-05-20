# Iterate over all EBS volumes of type gp2 in the us-west-1 region
for volume in $(aws ec2 describe-volumes --region=us-west-1 --filters "Name=volume-type,Values=gp2" | jq -r '.Volumes[].VolumeId'); do
    # Print the volume ID being modified
    echo "Modifying volume: ${volume}"

    # Initiate the modification of the volume to gp3 type
    # Run the command in the background to avoid waiting for completion
    aws ec2 modify-volume --volume-type gp3 --volume-id ${volume} &

    # Wait for the background process to complete
    wait $!

    # Check if the modification was successful
    if [ $? -eq 0 ]; then
        echo "Successfully modified volume: ${volume}"
    else
        echo "Failed to modify volume: ${volume}"
    fi
done