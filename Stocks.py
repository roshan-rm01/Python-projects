import pandas as pd
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

# stock = input("What stock do you want?\n")


def rsi_dataframe(stock):
    api_key = "Z44R1ERYHKV8HEHY"
    # time period
    period = 60
    ts = TimeSeries(key=api_key, output_format="pandas")
    # get stock data
    data_ts = ts.get_intraday(stock.upper(), interval="1min", outputsize="full")

    # indicator
    ti = TechIndicators(key=api_key, output_format="pandas")
    data_ti, meta_data_ti = ti.get_rsi(symbol=stock.upper(), interval="1min", time_period=period, series_type="close")
    df = data_ts[0][period::]

    df.plot("4. close")
    plt.grid()
    plt.show()


