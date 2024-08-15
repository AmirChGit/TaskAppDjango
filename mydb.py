import psycopg2
from psycopg2 import sql

# Database connection parameters
db_name = "taskapp_db"  # Replace with your desired database name
db_user = "postgres"  # Replace with your PostgreSQL username
db_password = "amir"  # Replace with your PostgreSQL password
db_host = "localhost"
db_port = "5432"

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

conn.autocommit = True
cur = conn.cursor()

# Create the database
try:
    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
    print(f"Database '{db_name}' created successfully.")
except psycopg2.errors.DuplicateDatabase:
    print(f"Database '{db_name}' already exists.")

# Close the connection
cur.close()
conn.close()
