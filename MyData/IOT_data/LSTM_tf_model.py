# -*- coding:utf-8 -*-
"""
make LSTM model analyze data to predict
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os

# ——————————————————导入数据——————————————————————
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y/%m/%d %H:%M:%S')
adata = pd.read_csv('../Data/dataA1_0515-19.csv', encoding='utf-8', parse_dates=['timestamp'], index_col='timestamp',
                    date_parser=dateparse)
ts = np.array(adata['temperature'])  # 获取温度序列

