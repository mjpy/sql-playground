SELECT
    date_trunc('week', rental_date) as rental_week,
    count(rental_id) as rentals
FROM rental
GROUP BY 1
ORDER BY 1