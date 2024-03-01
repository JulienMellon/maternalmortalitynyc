from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
import os
import io

app = Flask(__name__)

# Fetching the data from the URL and loading it into a DataFrame
url = 'https://data.cityofnewyork.us/resource/27x4-cbi6.json'
data = pd.read_json(url)

# Removing rows with 'all' as a value in the 'underlying_cause' column
data = data[data['underlying_cause'] != 'all']

# Creating pie charts for each year and saving them as image files
years = data['year'].unique()
for year in years:
    year_data = data[data['year'] == year]
    year_counts = year_data['underlying_cause'].value_counts()
    year_counts = year_counts.drop(year_counts.index[0])  # Remove the first item
    print(year_counts)
    plt.figure()
    plt.pie(year_counts, labels=year_counts.index, autopct='%1.1f%%')
    plt.title(f'Pie Chart for {year}')
    f = io.BytesIO()
    plt.savefig(f, format="svg")

# Route to display the image for a specific year in a webpage
@app.route('/')
def index():
    return render_template('index.html', years=range(2016, 2021))

# Route to serve the image file for a specific year
@app.route('/get_image/<int:year>')
def get_image(year):
    image_path = f'static/pie_chart_{year}.png'
    return send_file(image_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)