WITH Rents AS (
    SELECT landlord_id
          ,SUM(rent) AS total_rent
      FROM Property
  GROUP BY landlord_id
),
Costs AS (
    SELECT p.landlord_id
          ,SUM(mt.cost) AS total_cost
      FROM Maintenance mt INNER JOIN property p ON p.id = mt.property_id
     WHERE mt.maintenance_date >= '2024-04-01'
       AND mt.maintenance_date < '2024-05-01'
  GROUP BY p.landlord_id
)
SELECT l.id AS landlord_id
      ,l.name
      ,COALESCE(r.total_rent, 0) AS total_rent
      ,COALESCE(c.total_cost, 0) AS total_cost
      ,COALESCE(r.total_rent, 0) - COALESCE(c.total_cost, 0) AS amount_payable
  FROM Landlord l LEFT JOIN rents r ON r.landlord_id = l.id
                  LEFT JOIN costs c ON c.landlord_id = l.id
ORDER BY total_rent DESC
        ,landlord_id DESC