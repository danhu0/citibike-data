# Overview/Visualization Demo

`preprocess.py`, located in the `code` directory, queries the Citibike data and stores it in a .csv file in a directory specified by the user. It can be run with or without params (directions for using without params is included down below).

CSV data can be accessed pandas and then visualized with matplotlib. A short demo of this process, using preprocessed data from May, 2018, can be seen by running `simple_visualize_demo.py` in the `demo` directory.

CSV data can also be then transformed into a SQL database by running `make_sql_db.py` and following the terminal instructions. An example database created using this process is `2023.db` in `demo_data`.

`make_sql_db.py` is a script that combines the two functions into one larger REPL which will end with both a CSV being locally saved as well as a SQL database.

# Downloading/Unzipping Citibike Data

Two options for downloading the Citibike data: downloading by date or by manually entering a download url.

### Download by date

1. Run `preprocess.py`
2. Enter 'date' when prompted for an input mode.
3. Enter the year and month when prompted.
4. Specify a directory to unzip the csv into.

### Manual download

1. Run `preprocess.py`
2. Enter 'manual' when prompted for an input mode.
3. Go to this site: https://s3.amazonaws.com/tripdata/index.html for a download link. You will need to ctrl/cmd click and hit `Copy Link` from the dropdown or otherwise go to the actual link because the display texts are not the same as the links (actual download link should look something like: https://s3.amazonaws.com/tripdata/2013-citibike-tripdata.zip). Copy this link into the terminal when prompted.
4. Specify a directory to unzip the csv into.

# Converting Citibike CSV to SQL Database

1. Run `sql_from_csv.py`
2. Enter path to CSV file when prompted
3. Follow the rest of the terminal instructions to name the db and table

# Remaining TODOs (if time)
1. Add some way to combine multiple csvs (can do this with pandas ```.merge``` function)
2. Add some error handling for invalid terminal input in the unzipping process, should prompt the user to try again if the download failed and print out some descriptive messages (could make the download and unzip functions return something and modify the REPL behavior)
3. Add progress bar as the zips download and unzips (look into tqdm). Downloading whole years can take a while and it'd be nice to know the download is still happening/how long it'll take.
