__author__ = 'YangWang'

from yahoo_finance import Share
from Auto_Investment import Pre_Process
import csv
import time

Symbol_NYSE = []
with open('companylist_NYSE.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        Symbol_NYSE.append(row['Symbol'])

Symbol_NASDAQ = []
with open('companylist_NASDAQ.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        Symbol_NASDAQ.append(row['Symbol'])

Symbol_AMEX = []
with open('companylist_AMEX.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        Symbol_NYSE.append(row['Symbol'])

Symbol = Symbol_NYSE+Symbol_NASDAQ+Symbol_AMEX
print(Symbol)




i = 0
with open('Screen1_res.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    while i < len(Symbol):
        print(Symbol[i])
        print(i/len(Symbol)*100)
        # print(Share(i).get_market_cap())
        # print (Pre_Process.str2float(Share(i).get_market_cap()))
        try:
            temp = Share(Symbol[i])
            if Pre_Process.str2float(Share(Symbol[i]).get_market_cap()) < 10**9:
                print('remove',  Symbol[i])
                Symbol.remove(Symbol[i])
                i -= 1
            else:
                writer.writerow([Symbol[i]])
        except ConnectionError:
            print('Sleep')
            time.sleep(10)
        except AttributeError or KeyError:
            print('No value')
            print('remove',  Symbol[i])
            Symbol.remove(Symbol[i])
            i -= 1
            pass
        i += 1








print(Symbol)



