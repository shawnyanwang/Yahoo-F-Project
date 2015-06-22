__author__ = 'YangWang'

import csv
with open('companylist_NYSE.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print (row['Symbol'],row['MarketCap'])

