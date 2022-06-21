SELECT
    actor.actor_id,
    first_name,
    last_name,
    count(film_id) as played_in_how_many_films
FROM actor
JOIN film_actor
    ON actor.actor_id = film_actor.actor_id
GROUP BY
    actor.actor_id,
    first_name,
    last_name
ORDER BY played_in_how_many_films desc
LIMIT 10;