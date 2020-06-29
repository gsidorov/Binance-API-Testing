
#import the libraries for the visualization
import plotly.offline as py
import plotly.graph_objs as go

from dataframes import binance_price

binance_price = binance_price()
binance_price.columns

table_trace = go.Table(
            domain = dict(x=[0,0.5] ,y=[0,1.0]),
            columnwidth=[30] + [33,35,33],
            columnorder=[0,1,2,3,4,5],
            header = dict(height=50,
                            values = [['<b>Date</b>'], ['<b>Open Price</b>'], ['<b>High Price</b>'], ['<b>Low Price</b>'], ['<b>Volume</b>'], ['<b>Number of Trades</b>']],
                            line = dict(color='rgb(50, 50, 50)'),
                            align = ['center'] * 5,
                            font = dict(color = ['rgb(45, 42, 45)']*5, size=14),
                            fill = dict(color='rgb(135, 193, 238)')),
            #cells = dict(values = [binance_price.index[:], binance_price[['Open','High','Low','Volume','Number of trades']]],
                            cells = dict(values = [binance_price.index[:], binance_price['Open'],binance_price['High'],binance_price['Low'],binance_price['Volume'],binance_price['Number of trades']],
                                            line = dict(color='#106784'),
                                            align = ['left']*5,
                                            font = dict(color = ['rgb(45, 47, 45)'] * 5,size = 12 ), #notice that here we are changing the size of the font
                                            format = [None] + [', .2f'] * 2 + [', 4f'],
                                            suffix = [None] *4,
                                            height = 47,
                                            fill = dict(color=['rgb(135,193,238)', 'rgba(128,222,249,0.65)']))
                            )

trace = go.Ohlc(x = binance_price.index[:],
                open= binance_price['Open'],
                close = binance_price['Close'],
                high = binance_price['High'],
                low = binance_price['Low'],
                name = 'LTCUSDT',
                )

trace2 = go.Scatter(x= binance_price.index[:],
                    y = binance_price['Volume'],
                    xaxis = 'x2',
                    yaxis = 'y2',
                    line = dict(width=2, color = 'orange'),
                    name = 'volume'
                    )
trace3 = go.Scatter(x= binance_price.index[:],
                    y = binance_price['Number of trades'],
                    xaxis = 'x3',
                    yaxis = 'y3',
                    line = dict(width=2, color = 'yellow'),
                    name = 'number trades'
                    )

axis = dict(
    showline = True,
    zeroline=False,
    showgrid = True,
    mirror = True,
    ticklen = 4,
    gridcolor = '#ffffff',
    tickfont= (dict(size=10))
)

layout = dict(
            width = 1400,
            height = 1000,
            autosize = False,
            title = 'LTC/USDT - Binance Trade Data',
            margin = dict(t=100),
            showlegend=False,
            xaxis1 = dict(axis, **dict(domain=[0.55,1], anchor = 'y1', showticklabels = False)),
            xaxis2 = dict(axis, **dict(domain=[0.55,1], anchor = 'y2', showticklabels = False)),
            xaxis3 = dict(axis, **dict(domain=[0.55,1], anchor = 'y1', showticklabels = False)),
            yaxis1 = dict(axis, **dict(domain=[0.66,1], anchor = 'x1', hoverformat = '.2f')),
            yaxis2 = dict(axis, **dict(domain=[0.3+0.03,0.63], anchor = 'x2', tickprefix = '$', hoverformat = '.2f')),
            yaxis3 = dict(axis, **dict(domain=[0.0,0.3], anchor = 'x3', tickprefix='\u20BF'), hoverformat ='.2f'),
)

fig = dict(data = [table_trace, trace, trace2, trace3], layout = layout)
py.plot(fig, filename = 'table.html')
