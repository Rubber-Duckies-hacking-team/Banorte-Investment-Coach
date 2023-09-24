import streamlit as st
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


# Function to get predictions and display plots
def get_predictions(company_name,ss):
    # Load your data (Replace this with your actual data loading code)
    df = pd.read_csv("services/preprocessed_CAC40.csv", parse_dates=["Date"])
    df.drop(["Unnamed: 0"], axis=1, inplace=True)

    # Define a function for specific data
    def specific_data(company, start, end):
        company_data = df[df["Name"] == company]
        date_filtered_data = company_data[
            (company_data["Date"] > start) & (company_data["Date"] < end)
        ]
        return date_filtered_data

    # Setting the start and end date
    start_date = dt.datetime(2014, 1, 1)
    end_date = dt.datetime(2020, 1, 1)

    # Calling our function
    specific_df = specific_data(company_name, start_date, end_date)

    # Convert Date column to datetime
    specific_df["Date"] = pd.to_datetime(specific_df["Date"])

    # Display the saved plot using st.image
    st.pyplot(plot_closing_prices_over_time(specific_df, company_name))

    # Create and display Candlestick Chart plot
    st.pyplot(plot_candlestick_chart(specific_df))

    # Create and display Closing Prices and Moving Average plot
    st.pyplot(plot_closing_prices_moving_average(specific_df, company_name))

    # Create and display Monthly Seasonality of Closing Prices plot
    st.pyplot(plot_monthly_seasonality(specific_df, company_name))

    # Show a loader while calculating predictions
    with st.spinner("Calculating predictions..."):
        # Generate and display predictions for the next 10 days
        predictions_next_10_days = get_next_10_days_predictions(specific_df,company_name)
        st.pyplot(plot_next_10_days_predictions(predictions_next_10_days, company_name))

# Helper function to create Closing Prices Over Time plot
def plot_closing_prices_over_time(specific_df, company_name):
    plt.figure(figsize=(15, 6))
    plt.plot(specific_df["Date"], specific_df["Closing_Price"], marker=".")
    plt.title("Closing Prices Over Time for stock " + company_name)
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.xticks(rotation=45)
    plt.grid(True)
    return plt.gcf()

# Helper function to create Candlestick Chart plot
def plot_candlestick_chart(specific_df):
    matplotlib_date = mdates.date2num(specific_df["Date"])
    ohlc = np.vstack(
        (
            matplotlib_date,
            specific_df["Open"],
            specific_df["Daily_High"],
            specific_df["Daily_Low"],
            specific_df["Closing_Price"],
        )
    ).T

    fig, ax = plt.subplots(figsize=(15, 6))
    candlestick_ohlc(ax, ohlc, width=0.6, colorup="g", colordown="r")
    ax.xaxis_date()
    plt.title("Candlestick Chart")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.grid(True)
    return plt.gcf()

# Helper function to create Closing Prices and Moving Average plot
def plot_closing_prices_moving_average(specific_df, company_name):
    window = 30
    plt.figure(figsize=(15, 6))
    plt.plot(
        specific_df["Date"],
        specific_df["Closing_Price"],
        label="Closing Price",
        linewidth=2,
    )
    plt.plot(
        specific_df["Date"],
        specific_df["Closing_Price"].rolling(window=window).mean(),
        label=f"{window}-Day Moving Avg",
        linestyle="--",
    )
    plt.title(f"Closing Prices and {window}-Day Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    return plt.gcf()

# Helper function to create Monthly Seasonality of Closing Prices plot
def plot_monthly_seasonality(specific_df, company_name):
    specific_df["Month"] = specific_df["Date"].dt.month
    monthly_average = specific_df.groupby("Month")["Closing_Price"].mean()

    plt.figure(figsize=(15, 6))
    plt.plot(monthly_average.index, monthly_average.values, marker="o")
    plt.title(f"Monthly Seasonality of {company_name}")
    plt.xlabel("Months")
    plt.ylabel("Average Closing Price")
    plt.xticks(
        range(1, 13),
        [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
    )
    plt.grid(True)
    return plt.gcf()

# Helper function to get predictions for the next 10 days
def get_next_10_days_predictions(specific_df,company_name):
    # Your prediction code here
    new_df = specific_df.reset_index()["Closing_Price"]
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(np.array(new_df).reshape(-1, 1))

    train_size = int(len(scaled_data) * 0.8)  # 80% for training
    train_data, test_data = scaled_data[:train_size], scaled_data[train_size:]

    n_past = 60

    # Prepare sequences for LSTM
    X_train, y_train = [], []
    for i in range(n_past, len(train_data)):
        X_train.append(train_data[i - n_past : i, 0])
        y_train.append(train_data[i, 0])
    X_train, y_train = np.array(X_train), np.array(y_train)

    # Similarly prepare sequences for the test set
    X_test, y_test = [], []
    for i in range(n_past, len(test_data)):
        X_test.append(test_data[i - n_past : i, 0])
        y_test.append(test_data[i, 0])
    X_test, y_test = np.array(X_test), np.array(y_test)

    print("Training set size:-")
    print(X_train.shape), print(y_train.shape)
    print("\n")
    print("Testing set size:-")
    print(X_test.shape), print(y_test.shape)

    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    model = Sequential()

    # First LSTM layer with 50 units, input shape, and return sequences
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(0.2))  # Adding dropout to prevent overfitting

    # Second LSTM layer with 50 units and return sequences
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))

    # Third LSTM layer with 50 units
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))

    # Add a dense output layer with one unit
    model.add(Dense(units=1))

    print(model.summary())

    model.compile(loss="mean_squared_error", optimizer="adam")


    # Defining our callbacks
    checkpoints = ModelCheckpoint(filepath="my_weights.h5", save_best_only=True)
    # Defining our early stopping
    early_stopping = EarlyStopping(
        monitor="val_loss", patience=15, restore_best_weights=True
    )

    # Training our lstm model
    model.fit(
        X_train,
        y_train,
        validation_data=(X_test, y_test),
        epochs=100,
        batch_size=32,
        verbose=1,
        callbacks=[checkpoints, early_stopping],
    )


    # Let's do the prediction and check performance metrics
    train_predict = model.predict(X_train)
    test_predict = model.predict(X_test)

    # Transform back to original form
    train_predict = scaler.inverse_transform(train_predict)
    test_predict = scaler.inverse_transform(test_predict)

    # Calculate train data RMSE
    print(math.sqrt(mean_squared_error(y_train, train_predict)))
    # Calculate test data RMSE
    print(math.sqrt(mean_squared_error(y_test, test_predict)))

    # Set the number of previous time steps to consider for plotting
    look_back = 60

    # Initialize an array for plotting the train predictions
    trainPredictPlot = np.empty_like(new_df)
    trainPredictPlot[:] = np.nan
    # Assign the predicted values to the appropriate location for train predictions
    trainPredictPlot[look_back : len(train_predict) + look_back] = train_predict.flatten()

    # Initialize an array for plotting the test predictions
    testPredictPlot = np.empty_like(new_df)
    testPredictPlot[:] = np.nan
    # Calculate the starting index for the test predictions
    test_start = len(new_df) - len(test_predict)
    # Assign the predicted values to the appropriate location for test predictions
    testPredictPlot[test_start:] = test_predict.flatten()

    # Rescale the scaled data back to its original scale using the scaler
    original_scaled_data = scaler.inverse_transform(scaled_data)

    # Plotting the baseline data, training predictions, and test predictions
    plt.figure(figsize=(15, 6))
    plt.plot(original_scaled_data, color="black", label=f"Actual {company_name} price")
    plt.plot(
        trainPredictPlot, color="red", label=f"Predicted {company_name} price(train set)"
    )
    plt.plot(
        testPredictPlot, color="blue", label=f"Predicted {company_name} price(test set)"
    )

    plt.title(f"{company_name} share price")
    plt.xlabel("time")
    plt.ylabel(f"{company_name} share price")
    plt.legend()
    plt.show()

    # To predict for the next 10 days, you'll need the last n_past days of data
    last_sequence = X_test[-1]

    # Reshape the last_sequence to match the input shape of the model
    last_sequence = last_sequence.reshape(1, n_past, 1)

    # Generate predictions for the next 10 days
    predictions_next_10_days = []
    for _ in range(10):
        next_day_prediction = model.predict(last_sequence)
        predictions_next_10_days.append(
            next_day_prediction[0, 0]
        )  # Get the predicted value
        last_sequence = np.roll(last_sequence, -1, axis=1)  # Shift the sequence by one day
        last_sequence[
            0, -1, 0
        ] = next_day_prediction  # Update the last element with the new prediction

    # Transform the predictions back to the original scale
    predictions_next_10_days = scaler.inverse_transform(
        np.array(predictions_next_10_days).reshape(-1, 1)
    )

    # Print the predictions for the next 10 days
    print("Predictions for the next 10 days:")
    for i, prediction in enumerate(predictions_next_10_days, start=1):
        print(f"Day {i}: Predicted Price = {prediction[0]}")
    
    return predictions_next_10_days

# Helper function to create plot for the next 10 days predictions
def plot_next_10_days_predictions(predictions, company_name):
    plt.figure(figsize=(15, 6))
    plt.plot(predictions, marker="*")
    plt.title(f"Predicted stock price of {company_name} for next 10 days")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.xticks(
        range(0, 10),
        ["Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7", "Day8", "Day9", "Day10"],
    )
    plt.grid(True)
    return plt.gcf()

# Main Streamlit app
def main(company_name, ss):
    st.title("Stock Price Analysis")    
    if company_name:
        get_predictions(company_name,ss)
        return "Prediccion completa"
