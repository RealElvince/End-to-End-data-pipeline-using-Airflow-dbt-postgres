{{
    config(
        materialized='table',
        unique_key='id',
        tags=['stagiging', 'dbt_proj'],
    )
}}

WITH staging_cte AS (
    SELECT * FROM {{ source('dev', 'raw_weather_data')}}
)

SELECT 
   id,
   city,
   temperature,
   weather_description,
   wind_speed,
   time AS weather_time_local,
   (inserted_at + (utc_offset || 'hours')::interval) AS inserted_at_local
FROM staging_cte