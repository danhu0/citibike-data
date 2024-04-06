import urllib.request
import zipfile
import os

def download_file(url, directory, filename):
    # Concatenate directory path and filename
    filepath = os.path.join(directory, filename)
    urllib.request.urlretrieve(url, filepath)
    print("File downloaded successfully!")

def unzip_file(zip_filename, extract_dir):
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print("File extracted successfully!")

def main():
    url = input("Enter the URL of the ZIP file to download: ")
    zip_filename = input("Enter the filename to save the downloaded ZIP file as: ")
    download_directory = input("Enter the directory to save the downloaded file: ")
    print(download_directory)

    # Download the file to the specified directory
    download_file(url, download_directory, zip_filename)

    extract_dir = input("Enter the directory to extract the contents to: ")
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    # Unzip the file into the specified extraction directory
    unzip_file(os.path.join(download_directory, zip_filename), extract_dir)

if __name__ == "__main__":
    main()
