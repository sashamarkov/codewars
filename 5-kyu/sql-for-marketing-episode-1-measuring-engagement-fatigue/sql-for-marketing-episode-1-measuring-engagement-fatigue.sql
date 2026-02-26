SELECT prior_touches
      ,COUNT(*) AS sends
      ,SUM(has_engagement) AS engagements
      ,ROUND(100.0 * SUM(has_engagement) / COUNT(*), 2)::varchar AS engagement_rate_pct
FROM (
      SELECT  cs.id
             ,cs.user_id
             ,cs.sent_at
             ,cs.campaign_id
             ,prior.prior_touches
             ,engagement.has_engagement::int
        FROM Campaign_sends cs LEFT JOIN LATERAL (
                                                  SELECT COUNT(*) AS prior_touches
                                                    FROM Campaign_sends cs_prior
                                                   WHERE cs_prior.user_id = cs.user_id
                                                     AND cs_prior.sent_at >= cs.sent_at - INTERVAL '7 days'
                                                     AND cs_prior.sent_at < cs.sent_at
                                                 ) prior ON true
                               LEFT JOIN LATERAL (
                                                  SELECT EXISTS (
                                                                 SELECT 1
                                                                   FROM Engagement_events ee
                                                                  WHERE ee.user_id = cs.user_id
                                                                    AND ee.campaign_id = cs.campaign_id
                                                                    AND ee.event_time >= cs.sent_at
                                                                    AND ee.event_time < cs.sent_at + INTERVAL '24 hours'
                                                                ) AS has_engagement
                                                 ) engagement ON true
) T
GROUP BY prior_touches
ORDER BY prior_touches ASC