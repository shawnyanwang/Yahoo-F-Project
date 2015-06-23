__author__ = 'YangWang'

import numpy as np
import matplotlib.pyplot as plt
# Example: Yahoo! Inc. (YHOO)
#
# >>> from yahoo_finance import Share
# >>> yahoo = Share('YHOO')
# >>> print yahoo.get_open()
# '36.60'
# >>> print yahoo.get_price()
# '36.84'
# >>> print yahoo.get_trade_datetime()
# '2014-02-05 20:50:00 UTC+0000'
# Refresh data from market
#
# >>> yahoo.refresh()
# >>> print yahoo.get_price()
# '36.87'
# >>> print yahoo.get_trade_datetime()
# '2014-02-05 21:00:00 UTC+0000'
# Historical data
#
# >>> print yahoo.get_historical('2014-04-25', '2014-04-29')
# [{u'Volume': u'28720000', u'Symbol': u'YHOO', u'Adj_Close': u'35.83', u'High': u'35.89', u'Low': u'34.12', u'Date': u'2014-04-29', u'Close': u'35.83', u'Open': u'34.37'}, {u'Volume': u'30422000', u'Symbol': u'YHOO', u'Adj_Close': u'33.99', u'High': u'35.00', u'Low': u'33.65', u'Date': u'2014-04-28', u'Close': u'33.99', u'Open': u'34.67'}, {u'Volume': u'19391100', u'Symbol': u'YHOO', u'Adj_Close': u'34.48', u'High': u'35.10', u'Low': u'34.29', u'Date': u'2014-04-25', u'Close': u'34.48', u'Open': u'35.03'}]
# More readable output :)
#
# >>> from pprint import pprint
# >>> pprint(yahoo.get_historical('2014-04-25', '2014-04-29'))
# [{u'Adj_Close': u'35.83',
#   u'Close': u'35.83',
#   u'Date': u'2014-04-29',
#   u'High': u'35.89',
#   u'Low': u'34.12',
#   u'Open': u'34.37',
#   u'Symbol': u'YHOO',
#   u'Volume': u'28720000'},
#  {u'Adj_Close': u'33.99',
#   u'Close': u'33.99',
#   u'Date': u'2014-04-28',
#   u'High': u'35.00',
#   u'Low': u'33.65',
#   u'Open': u'34.67',
#   u'Symbol': u'YHOO',
#   u'Volume': u'30422000'},
#  {u'Adj_Close': u'34.48',
#   u'Close': u'34.48',
#   u'Date': u'2014-04-25',
#   u'High': u'35.10',
#   u'Low': u'34.29',
#   u'Open': u'35.03',
#   u'Symbol': u'YHOO',
#   u'Volume': u'19391100'}]
# Summary information for our example
#
# >>> from pprint import pprint
# >>> pprint(yahoo.get_info())
# {u'FullTimeEmployees': u'12200',
#  u'Industry': u'Internet Information Providers',
#  u'Sector': u'Technology',
#  u'end': u'2014-05-03',
#  u'start': u'1996-04-12',
#  u'symbol': u'YHOO'}
# Avalible methods
#
# get_price()
# get_change()
# get_volume()
# get_prev_close()
# get_open()
# get_avg_daily_volume()
# get_stock_exchange()
# get_market_cap()
# get_book_value()
# get_ebitda()
# get_dividend_share()
# get_dividend_yield()
# get_earnings_share()
# get_days_high()
# get_days_low()
# get_year_high()
# get_year_low()
# get_50day_moving_avg()
# get_200day_moving_avg()
# get_price_earnings_ratio()
# get_price_earnings_growth_ratio()
# get_price_sales()
# get_price_book()
# get_short_ratio()
# get_trade_datetime()
# get_historical(start_date, end_date)
# get_info()
# refresh()
from yahoo_finance import Share
import time
from Auto_Investment import PreProcess
yahoo = Share('YGE')
try :
    temp = Share('BW@')
except ConnectionError:
    print('Sleep')
    time.sleep(10)
except AttributeError:
    print('No value')
    pass
# print (Pre_Process.str2float(Share('BW@').get_market_cap()))
print(yahoo.get_open())
print (yahoo.get_year_high())
t = float("45.3")
print (t)
M = yahoo.get_market_cap()
if M == None:
    print (yahoo.get_market_cap())
print (yahoo.get_info())
# ya = yahoo.get_historical('2000-04-25', '2014-04-29')
# n = ya.__len__()
# print(n)

# fig = plt.figure()
#
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)
#
# x = np.linspace(0, 5, 10)
# y = x ** 2
# axes.plot(x, y, color="green", lw=2, ls='*', marker='+')
#
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('title')
# plt.show()