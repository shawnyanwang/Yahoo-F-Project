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
import numpy as np

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

    class Curve:
        def __init__(self, days=100, symbol=''):
            self.days = days
            self.symbol = symbol
            self.end_date = str(date.today())
            self.start_date = str(date.today() - timedelta(days=self.days))
            history = Share(self.symbol).get_historical(self.start_date, self.end_date)
            self.y, self.x = [], []
            for i in history:
                self.y.append(float(i['Close']))
                self.x.append(i['Date'])
            self.y.reverse()
            self.x.reverse()
            self.x = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in self.x]
            self.k = []
            self.d = [0]

        def derivative(self, multi=1):
            for i in range(len(self.k)-1):
                self.d.append((self.k[i+1]-self.k[i])*multi+min(self.y)+(max(self.y)-min(self.y))/5)

        def moving_average(self, ave_days):
            win = [1 for i in range(ave_days)]
            temp1 = [self.y[0] for i in range(ave_days)]
            temp2 = [self.y[-1] for i in range(ave_days)]
            self.k = np.convolve(temp1+self.y+temp2, win)/ave_days
            self.k = self.k[3*ave_days/2:]





        def plot_curve(self):

            """
            :param days : int
            :param symbol : string

            """
            fig = plt.figure()
            axes = fig.add_axes([0.11, 0.19, 0.8, 0.7])
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))

            if self.days < 15:
                plt.gca().xaxis.set_major_locator(mdates.DayLocator())
            elif self.days < 105:
                plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator())
            elif self.days < 365 * 3:
                plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
            else:
                plt.gca().xaxis.set_major_locator(mdates.YearLocator())

            if self.y[0] > self.y[-1]:
                axes.plot(self.x, self.y, 'r-')
                plt.fill_between(self.x, self.y, 0, color='r')
            else:
                axes.plot(self.x, self.y, 'g-')
                plt.fill_between(self.x, self.y, 0, color='g')

            if len(self.k) > len(self.y):
                axes.plot(self.x, self.k[:len(self.y)], 'b-')
            if len(self.d) > 1:
                axes.plot(self.x, self.d[:len(self.y)], 'y-')

            plt.gcf().autofmt_xdate()
            plt.ylim(min(self.y), max(self.y) + (max(self.y) - min(self.y)) / 20)
            axes.set_xlabel('x')
            axes.set_ylabel('y')
            axes.set_title(self.symbol + ': ' + self.start_date + ' to ' + self.end_date)
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
                print(int(i/27**5))
                try:
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

