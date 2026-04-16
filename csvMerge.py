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