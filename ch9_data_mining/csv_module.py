import csv

with open('G:/TEMP/data_science_from_scratch/ch9_data_mining/tab_delimited_stock_prices.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        date = row[0]
        print(date)
        # symbol = row[1]
        # closing_price = float(row[2])
        # print(','.join(row))
        # print(row)

with open('G:/TEMP/data_science_from_scratch/ch9_data_mining/colon_delimited_stock_prices.txt', 'r') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        print(date, symbol, closing_price)

# writing
today_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}

with open('G:/TEMP/data_science_from_scratch/ch9_data_mining/comma_delimited_stock_prices.txt', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])
