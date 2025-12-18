SELECT p.id AS person_id
      ,p.birthdate
      ,COALESCE(SUM(r.speed_delta), 0) AS total_speed_delta
FROM People p LEFT JOIN Records r ON p.id = r.person_id
GROUP BY p.id
        ,p.birthdate
ORDER BY p.id ASC