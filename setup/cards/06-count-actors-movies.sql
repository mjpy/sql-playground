SELECT 
    actor_id,
    count(film_id) as played_in_how_many_films  -- In how many movies
FROM film_actor
GROUP BY 1                                      -- each actor played?
ORDER BY 2 desc