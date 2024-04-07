import sqlite3

# Define SQLite database filename
db_filename = '2018.db'

# Connect to SQLite database (creates the database file if it doesn't exist)
conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# Define table name
table_name = 'trips'

# Define table schema based on CSV headers
table_schema = '''
    CREATE TABLE IF NOT EXISTS {} (
        trip_id INTEGER PRIMARY KEY,
        trip_duration INTEGER,
        start_time TEXT,
        stop_time TEXT,
        start_station_id INTEGER,
        start_station_name TEXT,
        start_station_latitude REAL,
        start_station_longitude REAL,
        end_station_id INTEGER,
        end_station_name TEXT,
        end_station_latitude REAL,
        end_station_longitude REAL,
        bike_id INTEGER,
        user_type TEXT,
        birth_year INTEGER,
        gender INTEGER
    )
'''.format(table_name)

# Execute table creation SQL command
cursor.execute(table_schema)

# Commit changes and close connection
conn.commit()
conn.close()

print("SQLite table created successfully.")
