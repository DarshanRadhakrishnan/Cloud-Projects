# Stop the script if any command fails (equivalent to set -e)
$ErrorActionPreference = 'Stop'

Write-Host "1. Installing dependencies to 'lib' folder..."
pip install -t lib -r requirements.txt

# Remove old zip if it exists so we start fresh
if (Test-Path lambda_function.zip) { 
    Remove-Item lambda_function.zip 
}

Write-Host "2. Zipping dependencies..."
# We zip the *contents* of lib (lib\*), not the folder itself
Compress-Archive -Path "lib\*" -DestinationPath lambda_function.zip

Write-Host "3. Adding todo.py to the zip..."
# Add your main python file to the existing zip
Compress-Archive -Path todo.py -Update -DestinationPath lambda_function.zip

Write-Host "4. Cleaning up..."
Remove-Item -Path lib -Recurse -Force

Write-Host "Success! lambda_function.zip is ready to upload."