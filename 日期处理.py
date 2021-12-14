# !/usr/bin/python
# -*- coding: utf-8 -*-


def time_period_features(df, time_col):
    """
    时间特征提取

    """
    # in hour level
    df["hour"] = df[time_col].dt.hour
    # in day level
    df["dayofweek"] = df[time_col].dt.dayofweek
    df["days_in_month"] = df[time_col].dt.days_in_month
    df["dayofyear"] = df[time_col].dt.dayofyear
    # week levels
    df["weekday"] = df[time_col].dt.weekday
    df["week"] = df[time_col].dt.week
    df["weekofyear"] = df[time_col].dt.weekofyear
    # month level
    df["month"] = df[time_col].dt.month
    df["is_month_start"] = df[time_col].dt.is_month_start
    df["is_month_end"] = df[time_col].dt.is_month_end
    # quarter level
    df["quarter"] = df[time_col].dt.quarter
    # year level
    df["year"] = df[time_col].dt.year
    return df
