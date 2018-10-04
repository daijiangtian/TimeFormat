#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4/004 9:47
# @Author  : Woe
# @Site    : 
# @File    : format.py
# @Software: PyCharm

import time
from datetime import datetime


class TimeMat:
    def __init__(self, date):
        self.time_datetime = None
        self.time_timestamp = None
        self.time_struct_time = None
        self.time_str = None

        if isinstance(date, datetime):
            self.format_datatime(date)

        if isinstance(date, time.struct_time):
            self.format_time_struct_time(date)
        if isinstance(date, float) or isinstance(date, int):
            self.format_time_struct_time(time.localtime(date))
            self.time_timestamp = date

        if isinstance(date, str):
            self.time_str = date

    @property
    def struct_time(self):
        if self.time_struct_time:
            return self.time_struct_time
        self.time_timestamp = time.mktime(time.strptime(self.str, "%Y-%m-%d %H:%M:%S"))
        self.time_struct_time = time.localtime(self.timestamp)
        return self.time_struct_time

    @property
    def timestamp(self):
        if self.time_timestamp :
            return self.time_timestamp
        self.time_timestamp = time.mktime(time.strptime(self.time_str, "%Y-%m-%d %H:%M:%S"))
        return self.time_timestamp

    @property
    def datetime(self):
        if self.time_datetime:
            return self.time_datetime
        self.time_datetime = datetime.strptime(self.time_str, "%Y-%m-%d %H:%M:%S")
        return self.time_datetime

    @property
    def str(self):
        return self.time_str

    def __str__(self):
        return self.str

    def format_datatime(self, date: datetime):
        self.str_ymd = date.strftime('%Y-%m-%d')
        self.str_hms = date.strftime('%H:%M:%S')
        self.time_str = f"{self.str_ymd} {self.str_hms}"
        self.time_datetime = date

    def format_time_struct_time(self, date: time.struct_time):
        self.str_ymd = time.strftime('%Y-%m-%d', date)
        self.str_hms = time.strftime('%H:%M:%S', date)
        self.time_str = f"{self.str_ymd} {self.str_hms}"
        self.time_struct_time = date


if __name__ == '__main__':
    date = datetime.now()
    date = time.time()
    date = '2018-09-10 10:10:10'
    Time = TimeMat(date)
    print(Time.str)
    print(Time.datetime)
    print(Time.timestamp)
    print(Time.struct_time)
