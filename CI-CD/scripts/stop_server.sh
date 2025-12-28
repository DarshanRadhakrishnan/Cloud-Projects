#!/bin/bash

# Stop the Flask Todo API server
# This script is called by CodeDeploy during deployment/rollback

echo "Stopping Flask Todo API..."

# Kill any Python processes running the app
pkill -f "python.*app.py" || true

echo "Application stopped"
