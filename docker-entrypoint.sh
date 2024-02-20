#!/bin/bash

# Start PostgreSQL server
/etc/init.d/postgresql start

# Navigate to application directory
cd /app/sreality

# Create PostgreSQL database and user (adjust as needed)
su - postgres -c "psql < init.sql"

# Initialize PostgreSQL database with tables from models
python init_db.py

# Run uvicorn
uvicorn web_app.main:app --host 127.0.0.1 --port 8080
