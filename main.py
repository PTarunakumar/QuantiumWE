import csv
for x in range(0,3):
    with open(f'data/daily_sales_data_{x}.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['product'] == "pink morsel":
                sales = float(row['quantity']) * float(row['price'][1:])
                date = row['date']
                region = row['region']
                print(sales, date, region)