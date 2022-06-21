SELECT actor_id
FROM film_actor
GROUP BY actor_id
HAVING count(film_id) > 40