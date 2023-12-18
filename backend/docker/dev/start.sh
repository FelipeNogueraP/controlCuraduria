#!/bin/bash

# Path to the .env file
ENV_FILE="./.env.development"

# Check if the .env file exists
if [ ! -f "$ENV_FILE" ]; then
    echo "Error: .env.development file not found!"
    echo "Please create a .env.development file with the next values to build correctly"
    echo "POSTGRES_USER=youruser"
    echo "POSTGRES_DB=youdatabase"
    echo "POSTGRES_PASSWORD=yourpassword"

    exit 1
fi

# Run Docker Compose
docker-compose up
