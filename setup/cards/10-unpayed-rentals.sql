SELECT count(*)                   -- Let's count all
FROM rental r                     -- rentals
LEFT JOIN payment p
    ON r.rental_id = p.rental_id
WHERE p.rental_id IS NULL         -- which are not payed for.