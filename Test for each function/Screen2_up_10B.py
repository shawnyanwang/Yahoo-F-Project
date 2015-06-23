__author__ = 'shawn.wang'


from yahoo_finance import Share
from Auto_Investment import Pre_Process
import csv
import time

Symbol = []
with open('Screen1_res.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        Symbol.append(row[0])

i = 0
with open('Screen2_res.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    while i < len(Symbol):
        print(Symbol[i])
        print(i/len(Symbol)*100)
        # print(Share(i).get_market_cap())
        # print (Pre_Process.str2float(Share(i).get_market_cap()))
        try:
            temp = Share(Symbol[i])
            if Pre_Process.str2float(Share(Symbol[i]).get_market_cap()) < 10**10:
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