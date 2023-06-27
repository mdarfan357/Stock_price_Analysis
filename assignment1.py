from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import plotly.graph_objects as go
from yahoo_fin.stock_info import get_data

# Setting the commonly used variables like current date, date one year ago, company
today = date.today()
one_yr_ago = datetime.now() - relativedelta(years=1)
one_yr_ago = one_yr_ago.date()
company = "amzn"

try:
    # Data Collection
    stock_price = get_data("amzn", start_date=one_yr_ago, end_date=today, index_as_date=True, interval="1d")
    stock_price = pd.DataFrame(stock_price)

    # Data Processing to compute average daily trading volume for one year
    avg_volume = stock_price.volume.sum() / stock_price.volume.shape[0]
    avg_volume = format(avg_volume, ".2f")
    print(f"Average daily trading volume for one year: {avg_volume}")

    print(stock_price)

    # Data Visualization
    dates = [one_yr_ago + relativedelta(months=i) for i in range(1, 13)]

    fig = go.Figure(data=[go.Candlestick(x=dates, open=stock_price.open, high=stock_price.high,
                                         low=stock_price.low, close=stock_price.close)])

    fig.update_layout(
        title={
            'text': f"Stock Price Analysis",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        })

    fig.show()

except:
    # Error handling
    stock_price = None
    print("No stock data available.")
