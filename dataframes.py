from binance.client import Client
from datetime import datetime
from pandas import DataFrame as df
import keys as keys


def binance_price():
    client = Client(keys.Pkey, keys.Skey)

    # this is a good practice to not disclose your public and api keys into pub

    candles = client.get_klines(symbol='BTCUSDT',
                                interval=client.KLINE_INTERVAL_1HOUR)

    # client.get_order_book(symbol='BNBBTC')
    client.get_aggregate_trades(symbol='BNBBTC')
    candles_data_frame = df(candles)

    candles_data_frame_date = candles_data_frame.loc[:, 0]

    final_date = []

# if you do not call for unique you will have 501 date points instead of 500
    for time in candles_data_frame_date.unique():
        ms_to_s = datetime.fromtimestamp(int(time/1000))
        # we need to divide by 1000 in order to match the datetime from Binance
        final_date.append(ms_to_s)

    # here we are popping the column of time and the last one as not necessary
    candles_data_frame.pop(0)
    candles_data_frame.pop(11)

    dataframe_final_date = df(final_date)
    dataframe_final_date.columns = ['date']  # we change the name of the column
    # of time

    final_dataframe = candles_data_frame.join(dataframe_final_date)
    final_dataframe.set_index('date', inplace=True)

        final_dataframe.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume']

    return final_dataframe
    pass


binance_price()
