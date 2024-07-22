import os
import pandas as pd
import time
import csv
from tradingview_ta import TA_Handler, Interval, Exchange
import sys

print('Wait until the data is received...')
print('Waiting time depends on the number of candles')
eurusd = TA_Handler(
    symbol="EURUSD",
    screener="forex",
    exchange="FX_IDC",
    interval=Interval.INTERVAL_1_MINUTE,
)

def svecha(open_price):
    close = eurusd.get_analysis().indicators["close"]
    Mom = eurusd.get_analysis().indicators["Mom"]
    RSI = eurusd.get_analysis().indicators["RSI"]
    MACD = eurusd.get_analysis().indicators["MACD.macd"]
    candle = [open_price, close, Mom, RSI, MACD]
    return candle

i = 0
d = ['open', 'close', 'Mom', 'RSI', 'MACD']  # CSV headers
file_path = 'data.csv'
header_written = False

# Checking for headers
if os.path.isfile(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        first_row = next(reader, None)
        if first_row == d + ['Direction']:
            header_written = True

previous_close = None  # previous close value storage

while i < 2:  # number of candles
    open_price = eurusd.get_analysis().indicators["open"]
    # writing candle data
    candle_data = svecha(open_price)

    with open(file_path, 'a', newline='') as csvfile:
        candlewriter = csv.writer(csvfile, delimiter=",")
        # writing headers if weren't
        if not header_written:
            candlewriter.writerow(d + ['Direction'])
            header_written = True
        # writing candle data with direction
        direction = 0  # first candle direction !NOT FINISHED!
        if previous_close is not None and candle_data[d.index('close')] > previous_close:
            direction = 1  # if bull
        candlewriter.writerow(candle_data + [direction])

        previous_close = candle_data[d.index('close')]  # rewrite previous close value

    i += 1
    time.sleep(60)  # hold 1 minute before next candle appeared
    
print('_____________________________________________')
print('Data received successfully')
