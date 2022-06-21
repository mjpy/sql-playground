SELECT count(film_id)       -- Let's count
FROM film                   -- films
WHERE language_id = (       -- that are in English.
    SELECT language_id
    FROM language
    WHERE name = 'English'
);