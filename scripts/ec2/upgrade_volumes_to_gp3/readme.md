# EBS Volume Modification Script

This script modifies the type of all Amazon Elastic Block Store (EBS) volumes of type `gp2` (General Purpose SSD) to `gp3` (Latest Generation General Purpose SSD) in the `us-west-1` region.

## Prerequisites

- AWS CLI installed and configured with appropriate permissions to manage EBS volumes.
- `jq` command-line JSON processor installed.

## Usage

1. Open the script in a text editor and review the code.
2. Save the script and make it executable:
`chmod +x upgrade_volumes_to_gp3.sh`
3. Run the script 
`bash upgrade_volumes_to_gp3.sh`

The script will iterate over all EBS volumes of type `gp2` in the `us-west-1` region and initiate the modification to `gp3` type. It will print the volume ID being modified and whether the modification was successful or failed.

## How it works

1. The script uses the `aws ec2 describe-volumes` command to list all EBS volumes of type `gp2` in the `us-west-1` region.
2. The `jq` command is used to extract the `VolumeId` values from the JSON output.
3. For each volume ID, the script:
   - Prints the volume ID being modified.
   - Initiates the modification of the volume to `gp3` type using the `aws ec2 modify-volume` command.
   - Runs the modification command in the background to avoid waiting for completion.
   - Waits for the background process to complete.
   - Checks the exit status of the modification command and prints a success or failure message.

## Notes

- The script is specific to the `us-west-1` region. Modify the `--region` parameter if you want to target a different region.
- Modifying the volume type may result in potential downtime or service disruption, depending on your use case. It's recommended to perform this operation during a scheduled maintenance window.
- Ensure that you have the necessary permissions to describe and modify EBS volumes.
- The script does not handle any errors that may occur during the modification process. It simply prints a failure message and continues to the next volume.

## License

This script is provided as-is, without any warranty or liability. Use it at your own risk.