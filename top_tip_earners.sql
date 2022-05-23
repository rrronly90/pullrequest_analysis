/*get total tips earned , precheck revealed lots of nulls and many taxi's having 0 tips .*/

with total_tips_earnings as 
( 
SELECT 
  taxi_id,
  sum (COALESCE(tips,0)) total_earned_tips , 
  sum(COALESCE(trip_total,0)) trip_total
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips` 
where date(trip_start_timestamp) >= ( current_date()-90) 
group by 1 having sum (COALESCE(tips,0)) > 0 
/* order by total_earned_tips desc limit 100  */
)
select  taxi_id from 
( select taxi_id , row_number() over ( partition by taxi_id order by total_earned_tips desc ) rank from total_tips_earnings )
where rank <=100;
