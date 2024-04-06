import urllib.request
import zipfile
import os
from datetime import datetime   

# ANSI escape codes for text colors
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    END = '\033[0m' 

def download_file(url, directory, filename):
    # Concatenate directory path and filename
    filepath = os.path.join(directory, filename)
    try:
        urllib.request.urlretrieve(url, filepath)
        print(f"{colors.GREEN}File downloaded successfully!{colors.END}")
    except urllib.error.URLError as e:
        print(f"{colors.RED}Failed to download file: {e.reason}{colors.END}")
        return

def unzip_file(zip_filename, extract_dir):
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"{colors.GREEN}File extracted successfully!{colors.END}")

def main():
    url = input(f"{colors.CYAN}Enter the URL of the ZIP file to download: {colors.END}")
    zip_filename = 'zip_archives_' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") +'.zip'
    download_directory = "/Users/danielhu/Documents/VSCode/citibike-data/zip_archives"

    # Download the file to the specified directory
    download_file(url, download_directory, zip_filename)

    extract_dir = input(f"{colors.CYAN}Enter the directory to extract the contents to: {colors.END}")
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    # Unzip the file into the specified extraction directory
    unzip_file(os.path.join(download_directory, zip_filename), extract_dir)

if __name__ == "__main__":
    main()
