SELECT id
      ,info->>'name' AS user_name
      ,(
         SELECT string_agg(pet->>'name', ', ' ORDER BY ordinality)
           FROM jsonb_array_elements(info->'pets') WITH ORDINALITY AS arr(pet, ordinality)
          WHERE pet->>'name' LIKE 'M%'
       ) AS pet_names
  FROM Users
WHERE EXISTS (
              SELECT 1
                FROM jsonb_array_elements(info->'pets') AS pet
               WHERE pet->>'name' LIKE 'M%'
             )
ORDER BY id ASC