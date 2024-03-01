import pandas as pd
import matplotlib.pyplot as plt

# Fetching the data from the URL and loading it into a DataFrame
url = 'https://data.cityofnewyork.us/resource/27x4-cbi6.json'
data = pd.read_json(url)

# Removing rows with 'all' as a value in the 'underlying_cause' column
data = data[data['underlying_cause'] != 'all']

# Creating pie charts for each year
years = data['year'].unique()
for year in years:
    year_data = data[data['year'] == year]
    year_counts = year_data['underlying_cause'].value_counts()
    year_counts = year_counts.drop(year_counts.index[0])  # Remove the first item
    print(year_counts)
    plt.figure()
    plt.pie(year_counts, labels=year_counts.index, autopct='%1.1f%%')
    plt.title(f'Pie Chart for {year}')
    plt.show()