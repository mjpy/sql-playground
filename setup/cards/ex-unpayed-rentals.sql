SELECT count(*)
FROM rental
WHERE rental_id NOT IN (
    SELECT rental_id
    FROM payment
)