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


def GettingNeutralChoices():
    df = pd.read_csv(
        "services/preprocessed_CAC40.csv",
        parse_dates=["Date"],
    )

    df.drop(["Unnamed: 0"], axis=1, inplace=True)

    df = df.sort_values(by=["Name", "Date"])

    # Calcular la diferencia entre los precios de años consecutivos
    df["diff_price"] = df.groupby("Name")["Closing_Price"].diff()

    # Definir un umbral de estabilidad (ajusta este valor según tus necesidades)
    umbral_estabilidad = 1.0  # Por ejemplo, 1.0 significa que la diferencia no debe ser mayor al 1% para considerarse estable

    # Filtrar las filas con diferencias de precio dentro del umbral de estabilidad
    df = df[(df["diff_price"] > 0) & (df["diff_price"] <= umbral_estabilidad)]

    # Calcular el porcentaje de cambio positivo
    df["Pct_Change"] = (
        df["diff_price"] / df.groupby("Name")["Closing_Price"].shift()
    ) * 100

    # Encontrar el top 5 de empresas con el mayor porcentaje de cambio positivo
    top_5 = df.groupby("Name")["Pct_Change"].mean().nlargest(5)

    result_df = top_5.reset_index()  # Resetear el índice para obtener 'Name' como una columna
    result_df["Pct_Change"] = result_df["Pct_Change"].round(2)  # Redondear la columna 'Pct_Change' a 2 decimales
    result_df = result_df.rename(columns={"Name": "Name", "Pct_Change": "Pct_Change"})  # Renombrar las columnas

    # Mostrar el resultado
    print("Top 5 empresas con el mayor porcentaje de cambio promedio:")
    print(result_df.to_string(index=False))  # Mostrar el DataFrame sin el índice


    # ----------------------------------
    # df = df.sort_values(by=['Name', 'Date'])

    # # Calcular el porcentaje de cambio anual
    # df['Pct_Change'] = df.groupby('Name')['Closing_Price'].pct_change(periods=720) * 100

    # # Encontrar el top 5 de empresas con el mayor porcentaje de cambio promedio
    # top_5 = df.groupby('Name')['Pct_Change'].mean().nlargest(5)

    # Mostrar el resultado
    # print("Top 5 empresas con el mayor porcentaje de cambio promedio:")
    # print(top_5)
    
    
    return result_df.to_string(index=False)

GettingNeutralChoices()

def GettingRiskyChoices():
    # Cargar el conjunto de datos desde el archivo CSV (asegúrate de cambiar el nombre del archivo)
    df = pd.read_csv(
        "services/preprocessed_CAC40.csv",
        parse_dates=["Date"],
    )

    df.drop(["Unnamed: 0"], axis=1, inplace=True)

    # Ordenar el DataFrame por empresa y año
    df = df.sort_values(by=["Name", "Date"])

    # Calcular la diferencia entre los precios de años consecutivos
    df["diff_price"] = df.groupby("Name")["Closing_Price"].diff()

    # Definir un umbral de significancia (ajusta este valor según tus necesidades)
    umbral_significancia = 5.0  # Por ejemplo, 5.0 significa que la diferencia debe ser al menos del 5% para considerarse significativa

    # Filtrar las filas con diferencias de precio dentro del umbral de significancia
    df = df[(df["diff_price"] > 0) & (df["diff_price"] >= umbral_significancia)]

    # Calcular el porcentaje de cambio positivo
    df["Pct_Change"] = (
        df["diff_price"] / df.groupby("Name")["Closing_Price"].shift()
    ) * 100

    # Encontrar el top 5 de empresas con el mayor porcentaje de cambio positivo más significativo
    top_5 = df.groupby("Name")["Pct_Change"].mean().nlargest(5)

    result_df = top_5.reset_index()  # Resetear el índice para obtener 'Name' como una columna
    result_df["Pct_Change"] = result_df["Pct_Change"].round(2)  # Redondear la columna 'Pct_Change' a 2 decimales
    result_df = result_df.rename(columns={"Name": "Name", "Pct_Change": "Pct_Change"})  # Renombrar las columnas

    # Mostrar el resultado
    print("Top 5 empresas con el mayor porcentaje de cambio positivo más significativo:")
    print(result_df.to_string(index=False))  # Mostrar el DataFrame sin el índice

    # # Mostrar el resultado
    # print(
    #     "Top 5 empresas con el mayor porcentaje de cambio positivo más significativo:"
    # )
    # print(top_5)
    # return top_5.astype(str)
    return result_df.to_string(index=False)

GettingRiskyChoices()


def GettingPopularChoices():
    # Cargar el conjunto de datos desde el archivo CSV (ajusta el nombre del archivo según tu dataset)
    df = pd.read_csv(
        "services/preprocessed_CAC40.csv",
        parse_dates=["Date"],
    )

    df.drop(["Unnamed: 0"], axis=1, inplace=True)

    # Filtrar las filas con la fecha más reciente (2020-04-03)
    fecha_mas_reciente = "2020-04-03"
    df_fecha_reciente = df[df["Date"] == fecha_mas_reciente]

    df_fecha_reciente["Volume"] = df_fecha_reciente["Volume"].str.replace(
        ",", "", regex=True
    )
    df_fecha_reciente["Volume"] = df_fecha_reciente["Volume"].fillna(0).astype("long")

    # df_fecha_reciente['Volume'] = df_fecha_reciente['Volume'].astype(int)

    # Ordenar el DataFrame por volumen de mayor a menor
    df_sorted = df_fecha_reciente.sort_values(by="Volume", ascending=False)

    # Obtener una lista de nombres de empresas y sus valores de volumen
    result = df_sorted[["Name", "Volume"]].head(5)

    # Mostrar el resultado
    print(result.to_string(index=False))
    return result.to_string(index=False)

GettingPopularChoices()
