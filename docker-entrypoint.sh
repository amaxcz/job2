#!/bin/bash

# Configure Python
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1

# Configure PostgreSQL
export DATABASE_URL='postgresql://demo1_user:demo1_pass@127.0.0.1:5432/demo1_db'

# Start PostgreSQL server
/etc/init.d/postgresql start

# Create PostgreSQL database and user (adjust as needed)
su - postgres -c "psql < /app/sreality/create.sql"

# Navigate to application directory
cd /app/sreality

# Initialize PostgreSQL database with tables from models
python init_db.py

# Run uvicorn
uvicorn web_app.main:app --host 0.0.0.0 --port 8080
