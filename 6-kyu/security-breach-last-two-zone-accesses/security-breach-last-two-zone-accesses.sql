WITH Ranked_accesses AS (
    SELECT employee_id
          ,latest_time
          ,zone
          ,ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY latest_time DESC) AS rn
      FROM ( 
             SELECT employee_id
                   ,zone
                   ,MAX(access_time) AS latest_time
               FROM Access_logs
           GROUP BY employee_id
                   ,zone
           ) T
)
SELECT employee_id
      ,seconds_diff
FROM (
      SELECT r1.employee_id
            ,ABS(EXTRACT(EPOCH FROM (r1.latest_time - r2.latest_time))) AS seconds_diff
        FROM Ranked_accesses r1 INNER JOIN Ranked_accesses r2  ON r1.employee_id = r2.employee_id
                                                              AND r1.zone != r2.zone
                                                              AND r1.rn = 1 
                                                              AND r2.rn = 2 
     ) T
ORDER BY seconds_diff ASC
        ,employee_id ASC