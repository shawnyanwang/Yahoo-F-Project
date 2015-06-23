__author__ = 'shawn.wang'


from yahoo_finance import Share
import csv
import time

Symbol = []
with open('Screen2_res.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        Symbol.append(row[0])


i = 0
with open('Screen2_3_res.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Symbol', 'Price', '1Y_low', 'Standard deviation', 'Marcket cap'])
    while i < len(Symbol):
        print(i/len(Symbol)*100)
        # print(Share(i).get_market_cap())
        # print (Pre_Process.str2float(Share(i).get_market_cap()))
        try:
            temp = Share(Symbol[i])
            cur = float(temp.get_price())
            low = float(temp.get_year_low())
            if (cur-low)/low < 3/100:
                writer.writerow([Symbol[i], cur, low, (cur-low)/low*100, temp.get_market_cap()])
        except ConnectionError:
            print('Sleep')
            time.sleep(10)
        except AttributeError or KeyError:
            pass
        i += 1
