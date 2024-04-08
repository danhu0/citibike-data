import pandas as pd
import matplotlib.pyplot as plt

# Extracts the data from the csv
csv_file_path = '/Users/danielhu/Documents/VSCode/citibike-data/demo_data/5_2018_data/JC-201805-citibike-tripdata.csv'
df = pd.read_csv(csv_file_path)

# Transfrom data
# In this demo, focus on the number of trips by user type
trip_count_by_user_type = df['usertype'].value_counts() #NOTE! sometimes it's 'User Type' instead of 'usertype' depending on the year

plt.figure(figsize=(6, 6))
trip_count_by_user_type.plot(kind='bar', color='skyblue')

year = csv_file_path.split('-')[2][:4]
plt.title(f'Number of Trips by User Type: {year}')
plt.xlabel('User Type')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
