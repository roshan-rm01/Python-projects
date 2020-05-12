import pandas as pd
from alpha_vantage.timeseries import TimeSeries  # get closing price
import matplotlib.pyplot as plt

api_key = "Z44R1ERYHKV8HEHY"

ts = TimeSeries(key=api_key, output_format="pandas")

data, meta_data = ts.get_intraday(symbol="AAPL", interval="60min", outputsize="compact")

data["1. open"].plot()
plt.grid()
plt.show()
