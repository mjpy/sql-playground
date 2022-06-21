WITH cities_rentals AS (
    SELECT city, rental_id
    FROM rental r
    JOIN customer c ON r.customer_id = c.customer_id
    JOIN address a on c.address_id = a.address_id
    JOIN city ct on a.city_id = ct.city_id
),

categories_rentals AS (
    SELECT c.name as category, rental_id
    FROM rental r
    JOIN inventory i on r.inventory_id = i.inventory_id
    JOIN film f on i.film_id = f.film_id
    JOIN film_category fc on f.film_id = fc.film_id
    JOIN category c on fc.category_id = c.category_id
)

SELECT city, category, count(cr.rental_id)
FROM cities_rentals cr
JOIN categories_rentals ctr ON cr.rental_id = ctr.rental_id
GROUP BY city, category