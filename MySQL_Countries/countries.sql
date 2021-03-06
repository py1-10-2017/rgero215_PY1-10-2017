 -- 1. All the countries that speak Slovene, descending by percentage.

SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages
ON countries.id = languages.country_id
WHERE languages.language = ‘Slovene’
ORDER BY languages.percentage DESC;

 -- 2. Total number of cities for each country?

SELECT countries.name, COUNT(cities.id) as num_cities
FROM countries
JOIN cities
ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY num_cities DESC;


 -- 3. Cities in Mexico with population > 500,000 in descends

SELECT cities.name, cities.population
FROM countries
JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = ‘Mexico’ AND cities.population > 500000
ORDER BY cities.population DESC;


 -- 4. Languages in each country with percentage > 89

SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages
ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

 -- 5. Countries with Surface Area < 501 and population > 100,000

SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 AND countries.population  > 100000;

 -- 6. Countries with Constitutional Monarchy with a capital > 200 and life expectancy > 75 years

SELECT countries.name, countries.government_form, countries.capital
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy' AND countries.life_expectancy  > 75 AND countries.capital > 200;

 -- 7. Argentina’s cities in Buenos Aires district and have the population > 500,000.

SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities
ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires'  AND cities.population > 500000;

 -- 8. Sum the number of countries in each region

SELECT countries.region, COUNT(countries.id) AS num_countries
FROM countries
GROUP BY countries.region
ORDER BY num_countries DESC;
