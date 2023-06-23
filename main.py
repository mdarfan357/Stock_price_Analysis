
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

# Setting the commonly used variables like current date, date one year ago, company
today = date.today()
one_yr_ago = datetime.now() - relativedelta(years=1)
one_yr_ago = one_yr_ago.date()
company = "amzn"


# Data Collection

from yahoo_fin.stock_info import get_data

try:
    stock_price = get_data("amzn", start_date=one_yr_ago, end_date=today, index_as_date = True, interval="1d")
    stocks = pd.DataFrame(stock_price)
except:
    # Error handling 
    print("Network Error failed to get data")

# Data Processing to compute average daily trading volume for one year 

avg_volume = stocks.volume.sum() / stocks.volume.shape[0]
avg_volume = format(avg_volume, ".2f")
print(f"average daily trading volume for one year : {avg_volume}")

print(stock_price)

# Data Visulaization

import plotly.graph_objects as go
from datetime import datetime

dates = [one_yr_ago+relativedelta(months=i) for i in range(1,13)]

fig = go.Figure(data=[go.Candlestick(x=dates,
                       open=stock_price.open, high=stock_price.high,
                       low=stock_price.low, close=stock_price.close)])

fig.update_layout(
    title={
        'text': f"Stock Price Analysis",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig.show()
