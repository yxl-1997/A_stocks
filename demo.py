# -*- coding: utf-8 -*-
# @Time : 2021/2/2 20:38
# @Author : yxl
# @File : demo.py
# @Project : A_stocks


# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:04:42 2021

@author: 35119
"""
import requests
from time import sleep
from datetime import datetime, time
from dateutil import parser  # parser 是一个解析器，可以将数据解析成所需要的数据结构


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
# ---------------------------------------------------
class AstockTrading(object):  # 类
    # attributes 类的属性
    def __init__(self, strategy_name):
        self._strategy_name = strategy_name
        self._open = None
        self._High = None
        self._Low = None
        self._Close = None
        self._Dt = None
        self._tick = None
        self._last_bar_start_minute = None

    def get_tick(self):
        # Go to sina to get last tick information
        # A股的开盘时间是9:15，9：15-9：25是集合竞价->开盘价啊
        # 9：25-9：30不开盘，时间一旦大于9：30，交易开始

        page_link = "http://hq.sinajs.cn/format=text&list=sh600519"
        page = requests.get(page_link)
        stock_info = page.text
        mt_info = stock_info.split(",")  # 茅台股票信息
        last = float(mt_info[0])  # 昨日收盘价
        trade_datetime = mt_info[30] + " " + mt_info[31]  # 成交日期和时间
        self._tick = (last, trade_datetime)  # tuple支持修改，list支持修改

        if trade_datetime.time() < time(9, 30):
            trade_datetime = datetime.combine(trade_time.date, time(9, 30))  # combin就是将date和tine合起来

    def get_history_data_from_local_machine(self):
        # return data matrix
        self._open = []
        self._Hign = []
        self._Low = []
        self._Close = []
        self._Dt = []

        pass

    def bar_generator(self, tick):
        # Updatebars,calcaulate 5minutes ma20,not daily data
        if self.tick[]

        pass

    def strategy(self):
        pass

    def buy(self):
        pass

    def sell(self):
        pass

    def runStrategy(self):
        self.get_tick()
        self.get_history_data_from_local_machine()
        self.bar_generator()
        self.strategy()

    # ---------------------------------------------------


astock = AstockTrading()
astock.get_tick()
while True:
    astock.runStrategy()
    sleep(3)