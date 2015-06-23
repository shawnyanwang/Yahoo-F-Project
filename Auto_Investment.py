__author__ = 'YangWang'

import matplotlib.pyplot as plt
from datetime import date
from datetime import timedelta
import datetime as dt
from yahoo_finance import Share
import matplotlib.dates as mdates
import string
import time
import csv

class PreProcess:

    @staticmethod
    def str2float(market_cap):
        res = 0
        if len(market_cap) == 0:
            return res
        elif market_cap[-1] == 'B':
            res = float(market_cap[0:-1]) * (10 ** 9)
        elif market_cap[-1] == 'M':
            res = float(market_cap[0:-1]) * (10 ** 6)
        else:
            res = float(market_cap[0:])
        return int(res)

    @staticmethod
    def plot_curve(days=30, symbol='YHOO'):

        """
        :param days : int
        :param symbol : string

        """

        end_date = str(date.today())
        start_date = str(date.today() - timedelta(days=days))
        history = Share(symbol).get_historical(start_date, end_date)
        Price, Date = [], []
        for i in history:
            Price.append(float(i['Close']))
            Date.append(i['Date'])
        Date = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in Date]
        fig = plt.figure()
        axes = fig.add_axes([0.11, 0.19, 0.8, 0.7])
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
        if days < 15:
            plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        elif days < 105:
            plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator())
        elif days < 365 * 3:
            plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
        else:
            plt.gca().xaxis.set_major_locator(mdates.YearLocator())

        if Price[1] < Price[-1]:
            axes.plot(Date, Price, 'r-')
            plt.fill_between(Date, Price, 0, color='r')
        else:
            axes.plot(Date, Price, 'g-')
            plt.fill_between(Date, Price, 0, color='g')

        plt.gcf().autofmt_xdate()
        plt.ylim(min(Price), max(Price) + (max(Price) - min(Price)) / 20)
        axes.set_xlabel('Date')
        axes.set_ylabel('Price')
        axes.set_title(symbol + ': ' + start_date + ' to ' + end_date)
        plt.grid(True)
        plt.show()

    @staticmethod
    def convert_to_symbol(num):
        """
        :param num : int

        """
        R = string.ascii_uppercase + '^'
        res = ''
        while num > 0:
            num -= 1
            res += R[num % 27]
            num /= 27
            num = int(num)
        return res[::-1]

    @staticmethod
    def get_all_symbol():
        with open('All_Symbol.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Symbol', 'Marcket cap'])
            for i in range(27**5):
                print(i)
                try :
                    temp = Share(PreProcess.convert_to_symbol(i)).get_market_cap()

                    if temp != None:
                        writer.writerow([PreProcess.convert_to_symbol(i),temp])
                except ConnectionError:
                    print('Sleep')
                    time.sleep(10)
                except AttributeError or KeyError:
                    pass













# Test = Pre_Process()
# print (Pre_Process.str2float("$27.1M"))

