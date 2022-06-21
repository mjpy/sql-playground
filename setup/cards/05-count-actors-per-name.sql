SELECT 
    first_name,
    count(actor_id) as actor_count   -- Let's count all the actors
FROM actor
GROUP BY first_name                  -- per name
ORDER BY actor_count desc            -- and order them by most popular.