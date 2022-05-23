/* get session count , uses lead group by function , only thing was for many records we have trip start = trip end */ 
with apply_lead as 
  ( SELECT unique_key, taxi_id , trip_start_timestamp, trip_end_timestamp , 
    lead(trip_start_timestamp) OVER(partition by  taxi_id ORDER BY trip_end_timestamp asc) lagged_timestamp ,
    date_diff (lead(trip_start_timestamp) OVER(partition by  taxi_id ORDER BY trip_end_timestamp asc),trip_end_timestamp ,hour) consicutive_diff
    FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips` 
    where 
    trip_start_timestamp <> trip_end_timestamp
    )
    /*not sure of requirement but assuming  trip length should atelast be > 0 */
    select taxi_id , count(unique_key) no_of_session   from apply_lead where consicutive_diff > 8 group by 1;
    
    
    
