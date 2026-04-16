import csv

def csvMerge():
    with open('combined.csv', 'w') as resultfile:
        writer = csv.writer(resultfile)
        writer.writerow(['sales', 'date', 'region'])

        for x in range(0,3):
            with open(f'data/daily_sales_data_{x}.csv') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    if row['product'] == "pink morsel":
                        sales = float(row['quantity']) * float(row['price'][1:])
                        date = row['date']
                        region = row['region']
                        writer.writerow([sales, date, region])

import pandas
from dash import Dash, html, dcc

from plotly.express import line

# the path to the formatted data file
DATA_PATH = "./combined.csv"

# load in data
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# initialize dash
dash_app = Dash()

# create the visualization
line_chart = line(data, x="date", y="sales", title="Pink Morsel Sales")
visualization = dcc.Graph(
    id="visualization",
    figure=line_chart
)

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header"
)

# define the app layout
dash_app.layout = html.Div(
    [
        header,
        visualization
    ]
)

# this is only true if the module is executed as the program entrypoint
if __name__ == '__main__':
    dash_app.run(debug=True)

