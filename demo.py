# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:53:04 2021

@author: 35119
"""

import requests
from time import sleep
from datetime import datetime, time
from dateutil import parser  # parser 是一个解析器，可以将数据解析成所需要的数据结构
import pandas as pd
import os
import numpy as np


# 面向过程，需要不断进行参数传递
# --------------------------------------------------
# def get_history_data_from_local_machine():
# pass

# --------------------------------------------------
# def get_tick():
#    pass
# def bar_generator(tick,dt,volume):
# pass
#    return *para
# def strategy():
#    pass

# 面向对象
# self?
# underscore->下划线：给内部调用
# 类的继承
# 拓展func-

def get_ticks_for_backtesting(tick_path, bar_path):
    ''' func : get ticks for backtesting, need two params
        param1 tick_path : csv file with tick data,
        when there is not tick data,
        use bar_path : csv file with bar data,
        param2 bar_path : csv file with bar data,
        used in creating tick data.
        tick_path example : 'C:\\Users\35119\\.spyder-py3\\600036_ticks.csv'
        bar_path example : 'C\\Users\35119\\.spyder-py3\\600036_5m.csv'
        Return
        ------
        ticks in list with tuples in it, such as [(datetime,last_price),(datetime,last_price)]

    '''

    tick_path = 'C:\\Users\\35119\\Desktop\\600036_data\\600036_ticks.csv'
    bar_path = 'C:\\Users\\35119\\Desktop\\600036_data\\600036_5m.csv'
    if os.path.exists(tick_path):
        ticks = pd.read_csv(
            tick_path,
            parse_dates=["datetime"],
            index_col="datatime")

        tick_list = []
        for index, row in ticks.iterrows():  # iterrow->遍历数据
            tick_list.append((index, row[0]))
        print(tick_list)

        ticks = np.array(tick_list)

    else:
        bar_5m = pd.read_csv(bar_path)
        ticks = []
        for index, row in bar_5m.iterrow():
            if row["open"] < 30:
                step = 0.01
            elif row["open"] < 60:
                step = 0.05
            else
                step = 0.1

            i = 0
            dt = parser.parsr(row["datetime"]) - timedelta(minutes=5)
            for item in arr:
                ticks.append((dt + timedelta(seconds=0.1 * i),item))
                i += 1
            tick_df = pd.DataFrame(ticks, columns=["datetime", price])
            tick_df.to_csv(tick_path, index=0)
        return ticks


get_ticks_for_backtesting(tick_path, bar_path)


# ---------------------------------------------------
class AstockTrading(object):  # 类
    # attributes 类的属性
    ''' class : a stock trading platform,need one param,
    It has backtesting,paper trading,and real trading.
    param1:strategy_name:strategy name
    '''

    def __init__(self, strategy_name):
        self._strategy_name = strategy_name
        self._open = []
        self._High = []
        self._Low = []
        self._Close = []
        self._Dt = []
        self._tick = []
        self._last_bar_start_minute = None
        self._is_new_bar = False
        self._ma20 = None
        self._current_orders = {}
        self._history_orders = {}
        self._order_number = 0
        self.__init = False  # for backtesting

    def get_tick(self):
        '''func: for paper trading or real trading,
        not for backtestig
        It gose to sina to get last tick info
        '''
        # Go to sina to get last tick information
        # A股的开盘时间是9:15，9：15-9：25是集合竞价->开盘价啊
        # 9：25-9：30不开盘，时间一旦大于9：30，交易开始
        ''' start this methond after 9:25
            tick info is orgnanised in tuple
            such as (trade_datetime,last_prise)
        '''
        page_link = "http://hq.sinajs.cn/format=text&list=sh600519"
        page = requests.get(page_link)
        stock_info = page.text
        mt_info = stock_info.split(",")  # 茅台股票信息
        last = float(mt_info[1])  # 昨日收盘价
        trade_datetime = mt_info[30] + " " + mt_info[31]  # 成交日期和时间
        self._tick = (trade_datetime, last)  # tuple支持修改，list支持修改

        '''9:25 -> 9:30, move first tick's time from 9:25 to 9:30
           2020/12/10 9:25, -> 2020/12/10 9:30
        '''
        if trade_datetime.time() < time(9, 30):
            trade_datetime = datetime.combine(trade_time.date, time(9, 30))
            # combin就是将date和tine合起来

    def get_history_data_from_local_machine(self):
        # return data matrix
        self._open = []
        self._High = []
        self._Low = []
        self._Close = []
        self._Dt = []

    def bar_generator(self, tick):
        # Updatebars,calcaulate 5minutes ma20,not daily data
        if self._tick[0].minute % 5 == 0 and \
                self.tick[0].minute != self.last_bar_start_minute
            # creat new bar
            self._open.insert(0, self._tick[1])
            self._High.insert(0, self._tick[1])
            self._Low.insert(0, self._tick[1])
            self._Close.insert(0, self._tick[1])
            self._Dt.insert(0, self._tick[1])
            self._is_new_bar = True
        else:
            # Update current bar
            self._High[0] = max(self._High[0], self._tick[1])
            self._Low[0] = min(self._Low[0], self._tick[1])
            self.Close[0] = self._tick[0]
            self._Dt[0] = self._tick[0]
            self._is_new_bar = False

    def buy(self):
        # creat an order
        ''' need two params
            param1: price:buying price
            param2: buying volume
            return None
        '''
        self._order_number += 1
        # {key : value}
        key = "order" + str(self._order_number)
        self._current_orders[key] = {
            "Open_datatime": self._Dt[0],
            "Open_price": price,
            "volume": volume
        }

    def sell(self, key, price):
        ''' creat an long order ,It needs two params,
            param1 key : long srder's key
            param2 price : selling price
            return None
        '''
        self._current_orders[key]["close_price"] = price
        self._current_orders[key]["close_datatime"] = self._Dt[0]
        self._current_orders[key]["pnl"] = \
            (price - self._current_orders[key]["open_price"]) \
            * self._current_orders[key]["volume"] \
            - price * self._current_orders[key]["volime"] * 1 / 1000 \
            - (price + self._current_orders[key]["open_price"]) \
            * self._current_orders[key]["volume"] * 3 / 10000

        # move order from current orders to history_orders
        self._history_orders[key] = self.current_orders.pop(key)

    def strategy(self):
        # last < 0.95 * ma20, long, last > ma20 * 1.05, sell
        # ma20 = Close[:19].sum()/20
        if self._is_new_bar:
            sum = 0
            for item in self._Close[1:21]:
                sum_ = sum_ + item
            self._ma20 = sum / 20
            # vplume 股数

        if 0 == len(self._current_orders):
            if self._Close[0] < 0.98 * self._ma20:
                volume = int(100000 / self._Close[0] / 100) * 100  # shares
                self._buy(self._Close[0] + 0.01, volime)

        elif 1 == len(self._current_orders):  # have long position
            if self._Close[0] > 1.02 * self._ma20:
                key = list(self._current_orders.keys())[0]
                self.sell(key, self._Close[0] - 0.01, volume)

        else:  # len() = 2
            raise ValueError("We have more than 1 current orders!")

    # ---------------------------------------------------

    def bar_generator_for_backtesting(self, tick):
        ''' for backtesing only
            used to update _Open _High,
            It needs just one paramter
            param tick : tick info  in tuple(dataetime, price)
        '''

        if tick[0].minute % 5 == 0 \
                and tick[0].minute != self._last_bar_start_minute:
            # creat a new bar
            self._last_bar_start_minute = tick[0].minute
            self._Open.insert(0, tick[1])
            self._Low.insert(0, tick[1])
            self._Close.insert(0, tick[1])
            self._Dt.insert(0, tick[1])
            self._is_new_bar = True
        else:
            # Update current bar
            self._High[0] = max(self._High[0].tick[1])
            self._Low[0] = min(self._Low[0], tick[1])
            self._Close[0] = tick[1]
            self._Dt[0] = tick[0]
            self._is_new_bar = False

    def runStrategy(self):
        self.get_tick()
        self.get_history_data_from_local_machine()
        self.bar_generator()
        self.strategy()

    def run_backtesting(self, ticks):
        ''' ticks will be uesd to generate bars,
            when bar is long enough,call strategy()
            Parameters
            ----------
            ticks : list with(datetime,price) in the list

            Returns
            ------
            None

        '''
        for tick in ticks:
            self.bar_generator_for_backtesting(tick)
            if self._init:
                self.strategy()
            else:
                if len(self.Open) >= 100:
                    self._init = True


if __name__ == "main":
    ticks = get_ticks_for_backtesting()
    ast = AstockTrading("ma")
    ast._current_orders
    ast._history_orders

    profit_orders = 0
    loss_orders = 0
    orders = ast._history_orders
    for key in orders.keys():

astock = AstockTrading()
astock.get_tick()
while True:
    astock.runStrategy()
    sleep(3)