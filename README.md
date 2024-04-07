# Overview/Visualization Demo
```preprocess.py```, located in the ```code``` directory, queries the Citibike data and stores it in a .csv file in a directory specified by the user.

CSV data can be accessed pandas and then visualized matplotlib. A short demo of this process, using preprocessed data from 5/2018, can be seen by running ```simple_visualize_demo.py``` in the ```demo``` directory.

# Downloading/Unzipping Citibike Data
### Download by date
1. Run ```preprocess.py```
2. Enter 'date' when prompted for an input mode.
3. Enter the year and month when prompted.
4. Specify a directory to unzip the csv into.

### Manual download
1. Run `preprocess.py`
2. Enter 'manual' when prompted for an input mode.
3. Go to this site: https://s3.amazonaws.com/tripdata/index.html for a download link. You will need to ctrl/cmd click and hit ```Copy Link``` from the dropdown or otherwise go to the actual link because the display texts are not the same as the links (actual download link should look something like: https://s3.amazonaws.com/tripdata/2013-citibike-tripdata.zip). Copy this link into the terminal when prompted.
4. Specify a directory to unzip the csv into.
