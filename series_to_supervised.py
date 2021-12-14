# !/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd


def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    """ 
    将时间序列类型数据转为监督学习的数据
    data: 观测序列。格式是一个 list 或 2维 Numpy Array   required
    n_in: 观测数据input(X)的步长，范围[1, len(data)], 默认为1
    n_out: 观测数据output(y)的步长， 范围为[0, len(data)-1], 默认为1
    dropnan: 是否删除存在NaN的行，默认为True
    """
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = [], []
    for i in range(n_in, 0, -1):
        # i n_in,n_in-1,
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]

    for i in range(n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]

        else:
            names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    agg = pd.concat(cols, axis=1)
    agg.columns = names

    if dropnan:
        agg.dropna(inplace=True)

    return agg


# 单步单变量预测
values = [x for x in range(10)]
df = series_to_supervised(values)

print(df)
