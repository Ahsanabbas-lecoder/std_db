import pyodbc

# SQL Server connection settings
server = 'YOUR_SERVER_NAME'  # e.g., 'localhost' or 'DESKTOP-XXXX\\SQLEXPRESS'
database = 'YOUR_DB_NAME'    # e.g., 'emp_db'
username = 'YOUR_USERNAME'   # (optional, leave empty for Windows Auth)
password = 'YOUR_PASSWORD'   # (optional)

# Establish connection
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Trusted_Connection=yes;'  # Use Windows Authentication if no username/password
)

cursor = conn.cursor()