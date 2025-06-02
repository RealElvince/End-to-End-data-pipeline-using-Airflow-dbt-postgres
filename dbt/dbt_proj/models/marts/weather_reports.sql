{{
    config(
        materialized='table',
        unique_key='id'
    )
}}

SELECT 
    id,
    city,
    DATE(weather_time_local) AS weather_date,
    ROUND(AVG(temperature)::numeric,2) AS avg_temperature,
    ROUND(AVG(wind_speed)::numeric,2) AS avg_wind_speed
FROM {{ ref('stg_weather_data') }}
GROUP BY 
    id, 
    city, 
    DATE(weather_time_local)
ORDER BY
    id,
    city,
    DATE(weather_time_local)