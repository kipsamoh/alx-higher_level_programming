-- script 18
-- Write a _cript that _displays the _average temperature _(Fahrenheit) by
-- city _ordered by _temperature (descending).
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
