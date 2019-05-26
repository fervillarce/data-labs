-- Lab | MySQL Select

-- =================
-- CHALLENGE 1 - Who Have Published What At Where?
SELECT authors.au_id as "AUTHOR ID", authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME", titles.title as TITLE, publishers.pub_name as PUBLISHER
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
INNER JOIN publishers ON publishers.pub_id = titles.pub_id
ORDER BY authors.au_id;

-- =================
-- CHALLENGE 2 - Who Have Published How Many At Where?

SELECT authors.au_id as "AUTHOR ID", authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME", publishers.pub_name as PUBLISHER, COUNT(titles.title) as "TITLE COUNT"
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
INNER JOIN publishers ON publishers.pub_id = titles.pub_id
GROUP BY authors.au_id, publishers.pub_name
ORDER BY authors.au_id DESC;

-- I check if the sum of the number of titles is the same as the total number of records in table titleauthor
SELECT COUNT(titles.title)
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
INNER JOIN publishers ON publishers.pub_id = titles.pub_id;
-- output: 25

SELECT COUNT(*)
FROM titleauthor;
-- output: 25

-- =================
-- CHALLENGE 3 - Best Selling Authors

-- Los 3 autores con más numero de títulos vendidos
-- He asumido que titles.ytd_sales es el número de ventas por título
SELECT authors.au_id as "AUTHOR ID", authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME", SUM(titles.ytd_sales) as "TOTAL"
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
GROUP BY authors.au_id
ORDER BY SUM(titles.ytd_sales) DESC
LIMIT 3;

-- =================
-- CHALLENGE 4 - Best Selling Authors Ranking

-- Todos los autores ordenados de mayor a menor en función del número total de títulos vendidos, incluidos los que no han vendido ninguno.
-- Utilizo la función COALESCE para mostrar 0 en lugar de null en TOTAL.
SELECT authors.au_id as "AUTHOR ID", authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME", COALESCE(SUM(titles.ytd_sales),0) as "TOTAL"
FROM authors
LEFT JOIN titleauthor ON authors.au_id = titleauthor.au_id
LEFT JOIN titles ON titles.title_id = titleauthor.title_id
LEFT JOIN sales ON sales.title_id = titles.title_id
GROUP BY authors.au_id
ORDER BY SUM(titles.ytd_sales) DESC;

-- =================
-- BONUS CHALLENGE - Most Profiting Authors
-- En PROFIT hago la suma del advance + (los royalties multiplicados por la ventas del título), y todo esto lo multiplico por el royaltyper para tener en cuenta el porcentaje que se lleva.
SELECT authors.au_id as "AUTHOR ID", authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME", SUM((titles.advance + (titles.royalty * titles.ytd_sales))*(titleauthor.royaltyper/100)) as "PROFIT"
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
GROUP BY authors.au_id
ORDER BY PROFIT DESC
LIMIT 3;