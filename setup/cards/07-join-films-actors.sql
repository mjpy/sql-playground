SELECT *                                        -- Let's see everthing
FROM actor
JOIN film_actor                                 -- from the joined "table".
    ON actor.actor_id = film_actor.actor_id;