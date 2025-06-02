from weather_api import mock_fetch_data
from weather_api import fetch_weather_data
from dotenv import load_dotenv
import os

load_dotenv()  

import psycopg2
def connect_to_db():
    print("Connecting to PostgreSQL database...")
    try:
        conn = psycopg2.connect(
            host="your_postgres_service_name",
            database="your_database_name",
            user="your_username",
            password="your_password",
            port="5432"
        )
        return conn

    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        return None
        
def create_weather_table(conn):
    print("Creating table if not exists...")
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                CREATE SCHEMA IF NOT EXISTS dev;
                CREATE TABLE IF NOT EXISTS dev.raw_weather_data(
                    id SERIAL PRIMARY KEY,
                    city TEXT,
                    temperature FLOAT,
                    weather_description TEXT,
                    wind_speed FLOAT,
                    time TIMESTAMP,
                    inserted_at TIMESTAMP DEFAULT NOW(),
                    utc_offset TEXT

                );
                """
            
            )
            conn.commit()
            print("Table was created successfully.")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
        raise



def insert_weather_data(conn,data):
    print("Inserting weather data into the database...")
    try:
        weather = data['current']
        location = data['location']
        with conn.cursor() as cursor:
            cursor.execute(
                """
                  INSERT INTO dev.raw_weather_data(
                  city
                  ,temperature, 
                  weather_description, 
                  wind_speed, 
                  time,
                  inserted_at,
                  utc_offset)
                  VALUES(%s,%s, %s, %s, %s, NOW(), %s);
                """,
                (
                    location['name'],
                    weather['temperature'],
                    weather['weather_descriptions'][0],
                    weather['wind_speed'],
                    location['localtime'],
                    location['utc_offset']
                )
            )
            conn.commit()
            print("Weather data inserted successfully.")
    except psycopg2.Error as e:
        print(f"Error inserting weather data: {e}")
        raise


def main():
    conn = None
    try:
        data = mock_fetch_data()
        # data = fetch_weather_data()
        conn = connect_to_db()
        if conn is None:
            raise Exception("Failed to connect to the database.")
        
        
        create_weather_table(conn)
        insert_weather_data(conn, data)
    except Exception as e:
        print(f"An error occurred during execution: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")
main()