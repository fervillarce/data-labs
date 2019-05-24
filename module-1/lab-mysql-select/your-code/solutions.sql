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
SELECT authors.au_id as "AUTHOR ID", authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME", COUNT(titles.title) as "TOTAL"
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
GROUP BY authors.au_id
ORDER BY COUNT(titles.title) DESC
LIMIT 3;

-- =================
-- CHALLENGE 4 - Best Selling Authors Ranking

-- Todos los autores ordenados de mayor a menos en función del número tota de títulos vendidos, incluidos los que no han vendido ninguno.
SELECT authors.au_id as "AUTHOR ID", authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME", COUNT(titles.title) as "TOTAL"
FROM authors
LEFT JOIN titleauthor ON authors.au_id = titleauthor.au_id
LEFT JOIN titles ON titles.title_id = titleauthor.title_id
GROUP BY authors.au_id
ORDER BY COUNT(titles.title) DESC;

-- =================
-- BONUS CHALLENGE - Most Profiting Authors

-- NO ES LA SOLUCIÓN FINAL: He empezado haciendo esta query sin tener en cuenta el royaltyper.
-- Sin hacer el royaltyper, Anne Ringer parece que es el que más profit tiene, pero no será así.
SELECT authors.au_id as "AUTHOR ID", authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME", SUM(titles.advance + titles.royalty) as "PROFIT"
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
GROUP BY authors.au_id
ORDER BY SUM(titles.advance + titles.royalty) DESC;

-- Esta query la he hecho para ver qué valores hay en royaltyper.
-- Además, puedo ver que, aunque Anne Ringer es la que más títulos ha vendido (como veíamos antes), tiene un royaltyper bajo.
SELECT titleauthor.au_id, authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME", titleauthor.title_id, titleauthor.royaltyper
FROM titleauthor
INNER JOIN authors ON authors.au_id = titleauthor.au_id
ORDER BY title_id, au_id;

-- SOLUCIÓN: Es por esto que cuando metemos el royaltyper, Anne Ringer ya no sale como la que más profit tiene, sino que es la octava.
SELECT authors.au_id as "AUTHOR ID", authors.au_lname as "LAST NAME", authors.au_fname as "FIRST NAME", SUM((titles.advance + titles.royalty)*(titleauthor.royaltyper/100)) as "PROFIT"
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
GROUP BY authors.au_id
ORDER BY PROFIT DESC
LIMIT 3;