WITH Agent_tickets AS (
    SELECT agent_id
          ,ARRAY_AGG(DISTINCT ticket_id ORDER BY ticket_id) AS tickets
      FROM Agent_ticket_assignments
  GROUP BY agent_id
)
SELECT a1.agent_id AS agent1_id
      ,a2.agent_id AS agent2_id
 FROM Agent_tickets a1 INNER JOIN Agent_tickets a2 ON a1.tickets = a2.tickets
                                                  AND a1.agent_id < a2.agent_id
ORDER BY 1 ASC
        ,2 ASC