import argparse
import urllib.request
import zipfile
import os
from datetime import datetime   

# ANSI escape codes for text colors
class colors:
    GREEN = '\033[92m'
    END = '\033[0m' 

def download_file(url, directory, filename):
    filepath = os.path.join(directory, filename)
    try:
        urllib.request.urlretrieve(url, filepath)
        print(f"{colors.GREEN}File downloaded successfully!{colors.END}")
    except urllib.error.URLError as e:
        print(f"Failed to download file: {e.reason}")

def unzip_file(zip_filename, extract_dir):
    try: 
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            for file in zip_ref.namelist():
                if not file.startswith('__MACOSX'): # On my local machine, __MACOSX is a file containing metadata that I don't want to extract
                    zip_ref.extractall(extract_dir)
        print(f"{colors.GREEN}File extracted successfully!{colors.END}")
    except zipfile.BadZipFile as e:
        print(f"Failed to extract file: {e}")

def process(url=None, download_dir=None, extract_dir=None):
    if url is None:
        # Prompt user for URL or date input
        while True:
            mode = input("Manual URL or Date Input (manual/date): ")
            if mode == "manual" or mode == "date":
                break
            else:
                print("usage: Enter 'manual' or 'date'")

        # Set URL based on user input
        if mode == "manual":
            url = input("Enter the URL of the ZIP file to download: ")
        elif mode == "date":
            year = input("Year: ")
            month = int(input("Month (1-12, or 0 if importing a whole year): "))
            if month == 0:
                url = f"https://s3.amazonaws.com/tripdata/{year}-citibike-tripdata.zip"
            else:
                url = f"https://s3.amazonaws.com/tripdata/JC-{year}{month:02d}-citibike-tripdata.csv.zip"

    if download_dir is None:
        download_dir = os.path.join(os.getcwd(), "zip_archives")
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

    zip_filename = 'zip_archives_' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") +'.zip'
    download_file(url, download_dir, zip_filename)

    if extract_dir is None:
        extract_dir = os.path.join(os.getcwd(), "data")
        if not os.path.exists(extract_dir):
            os.makedirs(extract_dir)

    unzip_file(os.path.join(download_dir, zip_filename), extract_dir)

def main():
    process()

if __name__ == "__main__":
    main()
