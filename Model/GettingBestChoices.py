# Basic libraries
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

# For processing
import math
import random
import datetime as dt
import matplotlib.dates as mdates

# For visualization
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc

# Libraries for model training
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.metrics import mean_squared_error

df = pd.read_csv(
    "/Users/jgarcia/Library/CloudStorage/OneDrive-SoftServe,Inc/Documents/Code/HackMTY/Banorte-Investment-Coach/Model/preprocessed_CAC40.csv",
    parse_dates=["Date"],
)

df.drop(["Unnamed: 0"], axis=1, inplace=True)

# First, we need to make sure the Date column is sorted in ascending order
df = df.sort_values(by="Date")

# Then, we can calculate the percentage change in Closing_Price over the last year
df["Pct_Change"] = df["Closing_Price"].pct_change(periods=365)

# Next, we can group by the unique names in the Closing_Price column and get the mean percentage change for each name
grouped = df.groupby("Name")["Pct_Change"].mean()

# Finally, we can sort the groups by the mean percentage change in descending order and get the top 5
top_5 = grouped.sort_values(ascending=False).head(5)

# Print the top 5 unique names with the greatest growth over the last year, along with the column name
print(f"Top 5 unique names in the 'Name' column with the greatest growth over the last year:\n{df.loc[df['Name'].isin(top_5.index.tolist()), ['Name']].drop_duplicates().reset_index(drop=True)}")

