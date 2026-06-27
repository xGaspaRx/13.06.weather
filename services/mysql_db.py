import mysql.connector as sql
from config import Config

def get_connection():
    return sql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_DATABASE
    )

def create_weather_table():
    query = """
    CREATE TABLE IF NOT EXISTS records (
        id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
        name VARCHAR(255) NOT NULL,
        temp FLOAT NOT NULL,
        feels_like FLOAT NOT NULL,
        wind_speed FLOAT NOT NULL,
        pressure INT NOT NULL,
        humidity INT NOT NULL,
        clouds INT NOT NULL,
        timestamp DATETIME NOT NULL
    );
    """

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabela została utworzona lub już istnieje")
    except Exception as e:
        print(e)

def save_weather_record(weather):
    query = """
    INSERT INTO records 
    (name, temp, feels_like, wind_speed, pressure, humidity, clouds, timestamp)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        weather["name"],
        weather["temp"],
        weather["feels_like"],
        weather["wind_speed"],
        weather["pressure"],
        weather["humidity"],
        weather["clouds"],
        weather["timestamp"]
    )

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()

    def get_weather_records():
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM records ORDER BY timestamp DESC"
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    # test = get_weather_records()
    # print(test)