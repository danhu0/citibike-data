import pandas as pd
import matplotlib.pyplot as plt

# Extracts the data from the csv
# csv_file_path = '/Users/danielhu/Documents/VSCode/citibike-data/data/JC-201509-citibike-tripdata.csv'
csv_file_path = '/Users/danielhu/Documents/VSCode/citibike-data/data/JC-201907-citibike-tripdata.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Transform data (if necessary)
# For example, you might want to group data by a certain category and count the number of trips in each category
# In this example, let's count the number of trips by user type
trip_count_by_user_type = df['usertype'].value_counts()

plt.figure(figsize=(6, 6))
trip_count_by_user_type.plot(kind='bar', color='skyblue')
plt.title('Number of Trips by User Type')
plt.xlabel('User Type')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
