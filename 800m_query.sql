SELECT athlete, lap_1, lap_2, lap_3, lap_4, total_time FROM race_laps
WHERE event_distance_m == 800 AND lap_2 != ""
