import preprocess
import sql_from_csv

preprocess.process(url='https://s3.amazonaws.com/tripdata/JC-201509-citibike-tripdata.csv.zip')
sql_from_csv.convert_csv_to_db('data/JC-201509-citibike-tripdata.csv', 'citibike.db', 'citibike_data')