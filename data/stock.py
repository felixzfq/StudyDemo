from jqdatasdk import *
import pandas as pd
import datetime


auth('15821428935', 'ZFQzfq930628')
pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 1000)


def get_stocks_list():
    """获取所有股票列表"""
    stocks = list(get_all_securities(['stock']).index)
    return stocks


def get_single_stock_price(code, start_time, end_time, time_freq):
    """存储单个股票价格数据"""
    data = get_price(code, start_time, end_time, time_freq)
    return data


def export_data(data, filename, type):
    """导出股票行情数据"""
    data.to_csv(filename)


def transfer_price_freq(data, time_freq):
    """将数据转为指定周期：开盘价、收盘价、最高价、最低价"""
    df_trans = pd.DataFrame()
    df_trans['open'] = data['open'].resample(time_freq).first()
    df_trans['close'] = data['close'].resample(time_freq).last()
    df_trans['high'] = data['high'].resample(time_freq).max()
    df_trans['low'] = data['low'].resample(time_freq).min()


def get_single_finance(code, date, stat_data):
    """获取单个股票财务指标"""
    data = get_fundamentals(query(indicator).filter(indicator.code == code), date=date, statData=stat_data)
    return data


def get_single_valuation(code, date, stat_data):
    """获取单个股票估值指标"""
    data = get_fundamentals(query(valuation).filter(valuation.code == code), date=date, statData=stat_data)
    return data


if __name__ == '__main__':
    gg = get_stocks_list()
    print(gg)