# pip install yfinance
# https://pypi.org/project/yfinance/

import yfinance as yf
spy = yf.Ticker('SPY').funds_data
spy.description
print(spy.top_holdings)