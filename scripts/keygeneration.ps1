# Define the file paths for the key pair
$privateKeyFile = "C:\Users\psaid\.ssh\private"
$publicKeyFile = "C:\Users\psaid\.ssh\public"
$pemPrivateKeyFile = "C:\Users\psaid\.ssh\private"

# Generate the Ed25519 key pair
ssh-keygen -o -a 100 -t ed25519 -f $privateKeyFile

ssh-keygen -o -a 100 -t ed25519 -f C:\Users\psaid\.ssh\private

# Convert the private key to .pem format
ssh-keygen -p -m PEM -f $privateKeyFile -e > $pemPrivateKeyFile

# Output success message
Write-Host "Ed25519 key pair generated and private key converted to .pem format."
