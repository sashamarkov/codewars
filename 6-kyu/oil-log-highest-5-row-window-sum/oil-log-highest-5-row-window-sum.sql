WITH intervals AS (
    SELECT depth AS start_depth
          ,LEAD(depth, 4) OVER w AS end_depth
          ,SUM(ktim) OVER w AS raw_sum
      FROM Well_log
    WINDOW w AS (
        ORDER BY depth
        ROWS BETWEEN CURRENT ROW AND 4 FOLLOWING
    )
)
SELECT start_depth
      ,end_depth
      ,ROUND(raw_sum::NUMERIC, 2)::VARCHAR AS total_ktim
  FROM Intervals
 WHERE end_depth IS NOT NULL
ORDER BY ROUND(raw_sum::NUMERIC, 2) DESC
        ,start_depth ASC