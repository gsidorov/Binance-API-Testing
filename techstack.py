import datetime
import plotly.offline as py
import plotly.graph_objs as go
import pandas_datareader as web #this is for reading from website information

start = datetime.datetime(2019,1,1  )
end = datetime.datetime(2020,6,20)

#we use data reader to read the data from the symbols

fb = web.DataReader('FB', 'yahoo', start, end)
tw = web.DataReader('TWTR', 'yahoo', start, end)
appl = web.DataReader('AAPL', 'yahoo', start, end)

trace = go.Ohlc(x = fb.index[:], open = fb['Open'], high = fb['High'],
low = fb['Low'],
close = fb['Close'],
name = 'fb',
increasing= dict(line=dict(color='blue')),
decreasing= dict(line=dict(color='red')),
)

trace2 = go.Ohlc(x = tw.index[:],
open = tw['Open'],
high = tw['High'],
low = tw['Low'],
close = tw['Close'],
name = 'tw',
increasing= dict(line=dict(color='blue')),
decreasing= dict(line=dict(color='red')),

)

trace3 = go.Ohlc(x = fb.index[:],
open = appl['Open'],
high = appl['High'],
low = appl['Low'],
close = appl['Close'],
name = 'appl',
increasing= dict(line=dict(color='blue')),
decreasing= dict(line=dict(color='red')),
)

data = [trace,trace2, trace3]
layout = {
'title': 'Facebook vs Twitter vs Apple',
'yaxis': {'title':'Price per stock'}
}

fig = dict(data=data, layout = layout)
py.plot(fig, filename = 'techstocks.html')
