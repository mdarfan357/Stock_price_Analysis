import plotly.graph_objects as go
import yfinance
import talib

company = "SPY"
# Download the data using APIs
data = yfinance.download(company, period='1y')

# Plot the candle stick figure
fig = go.Figure(data=[go.Candlestick(x=data.index,
                                     open=data.Open, 
                                     high=data.High,
                                     low=data.Low,
                                     close=data.Close)
                                     ])

# Get Morning star
morningstar = talib.CDLMORNINGSTAR(data.Open, data.High, data.Low, data.Close)
# Get Morning Star
eveningstar = talib.CDLEVENINGSTAR(data.Open, data.High, data.Low, data.Close)

data["Morning Star"] = morningstar
data["Evening Star"] = eveningstar

fig.update_layout(
    title='Stock Market Analysis',
    yaxis_title=f'{company} Stock',

)

# Plot morning star
for r in morningstar[morningstar!=0].index:
    fig.add_vline(x=r,  line_width=2, line_dash="dash", line_color="blue")
    fig.add_annotation(
    x=r, y=0.05, xref='x', yref='paper',
    showarrow=False, xanchor='center', text='Morning Star')


for r in eveningstar[eveningstar!=0].index:
    fig.add_vline(x=r,  line_width=2, line_dash="dash", line_color="gray")
    fig.add_annotation(
    x=r, y=0.05, xref='x', yref='paper',
    showarrow=False, xanchor='center', text='Evening Star')
   
print(data.head())

fig.show()