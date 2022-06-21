WITH actors_films_count AS (
    SELECT
        actor_id,
        count(film_id) as played_in_how_many_films
    FROM film_actor
    GROUP BY actor_id
)

SELECT actor_id
FROM actors_films_count
WHERE played_in_how_many_films > 40