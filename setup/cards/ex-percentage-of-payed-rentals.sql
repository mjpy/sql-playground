SELECT (count(p.rental_id)::float / count(r.rental_id)::float) * 100
FROM rental r
LEFT JOIN payment p ON r.rental_id = p.rental_id