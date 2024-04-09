import sqlite3
import pandas as pd

def convert_csv_to_db(csv_filepath=None, db_filename=None, table_name=None):
    # Parses the CSV file, adds all headers to a list
    if csv_filepath is None:
        csv_filepath = input("Enter the path to the CSV file: ")
    df = pd.read_csv(csv_filepath)
    # print(df)
    headers = df.columns.tolist()

    # Define SQLite database filename and connect to/create database
    if db_filename is None:
        db_filename = input("What you want to name the database file: ")
    conn = sqlite3.connect(db_filename)

    # Define table
    if table_name is None:
        table_name = input("What you want to name the table: ")
    df.to_sql(table_name, 
              conn, 
              if_exists='replace', 
              index=True, # replace with False if don't want the df indices
              dtype={header: 'TEXT' for header in headers}) # 'TEXT' used for simplicity

def main():
    convert_csv_to_db()

if __name__ == "__main__":
    main()
