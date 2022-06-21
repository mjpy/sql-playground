SELECT first_name, last_name, title             -- Let's see each actor and film they played in.
FROM actor
JOIN film_actor                                 -- We need information in which films they played
    ON actor.actor_id = film_actor.actor_id
JOIN film                                       -- and those films titles.
    ON film.film_id = film_actor.film_id;