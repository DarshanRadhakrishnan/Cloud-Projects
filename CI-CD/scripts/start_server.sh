#!/bin/bash

# Start the Flask Todo API server
# This script is called by CodeDeploy during deployment

set -e

echo "Starting Flask Todo API..."

# Navigate to app directory
cd /home/ec2-user/app

# Install dependencies if not already installed
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Start the application in the background
echo "Launching application on port 5000..."
nohup python app/app.py > /tmp/todo-app.log 2>&1 &

# Verify the app is running
sleep 2
if curl -f http://localhost:5000/health; then
    echo "✓ Application started successfully"
    exit 0
else
    echo "✗ Application failed to start"
    exit 1
fi
