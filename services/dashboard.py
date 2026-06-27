import pandas as pd
import streamlit as st
from config import Config


def render():
    FILE = Config.WEATHER_FILE
    df = pd.read_excel(FILE)

    st.set_page_config(
        page_title="Pogoda",
        layout="wide",
    )

    st.title("Dashboard pogodowy")
    st.subheader("Dane pogodowe pochodzące z OpenWeather API")

    st.sidebar.header("Konfiguracja")

    extra_metric_key = st.sidebar.selectbox(
        "Dodatkowa metryka",
        ["humidity", "clouds"]
    )
    rows_size = st.sidebar.slider(
        "Ilość rekordów w tabeli",
        min_value=1,
        max_value=100,
    )

    st.divider()
    # Najnowszy rekord pogodowy

    last_row = df.iloc[-1] # ostatni rekord w DF
    print(last_row)
    st.subheader("Aktualna pogoda")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        temp = last_row["temp"]
        col1.metric("Temperatura", f"{temp}°C")
    with col2:
        feels_like = last_row["feels_like"]
        col2.metric("Odczuwalna", f"{feels_like}°C")
    with col3:
        wind_speed = last_row["wind_speed"]
        col3.metric("Wiatr", f"{wind_speed}m/s")
    with col4:
        extra_field = last_row[extra_metric_key]
        col4.metric(extra_metric_key, f"{extra_field}%")


    st.divider()
    # Tabela z rekordami
    st.subheader(f"Najnowsze pomiary ({rows_size})")

    st.dataframe( df.tail(rows_size) )