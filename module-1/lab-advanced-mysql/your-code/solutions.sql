-- Lab | Advanced MySQL

-- =================
-- CHALLENGE 1 - Most Profiting Authors
-- Este challenge está hecho con derived tables. En el challenge 2 lo hago con temporary tables.
-- Step 1: Calculate the royalties of each sales for each author
SELECT titleauthor.title_id, titleauthor.au_id, titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 as ROYALTY
FROM titleauthor
INNER JOIN titles ON titles.title_id = titleauthor.title_id
INNER JOIN sales ON sales.title_id = titleauthor.title_id;

-- Step 2: Aggregate the total royalties for each title for each author
SELECT royalty_per_sale.title_id, royalty_per_sale.au_id, SUM(ROYALTY) as TOTAL_ROYALTIES
FROM
	(SELECT titleauthor.title_id, titleauthor.au_id, titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 as ROYALTY
	FROM titleauthor
	INNER JOIN titles ON titles.title_id = titleauthor.title_id
	INNER JOIN sales ON sales.title_id = titleauthor.title_id) royalty_per_sale
GROUP BY royalty_per_sale.au_id, royalty_per_sale.title_id;
    
-- Step 3: Calculate the total profits of each author
-- -- Por pasos, primero calculo el total de profits por autor que provienen de royalties
SELECT royalties_per_title.au_id, SUM(TOTAL_ROYALTIES)
FROM
	(SELECT royalty_per_sale.title_id, royalty_per_sale.au_id, SUM(ROYALTY) as TOTAL_ROYALTIES
	FROM
		(SELECT titleauthor.title_id, titleauthor.au_id, titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 as ROYALTY
		FROM titleauthor
		INNER JOIN titles ON titles.title_id = titleauthor.title_id
		INNER JOIN sales ON sales.title_id = titleauthor.title_id) royalty_per_sale
	GROUP BY royalty_per_sale.au_id, royalty_per_sale.title_id) royalties_per_title
GROUP BY royalties_per_title.au_id
ORDER BY SUM(TOTAL_ROYALTIES) DESC;

-- -- SOLUCIÓN FINAL del step 3: Ahora calculo el total de profits por autor que provienen de royalties y advance
-- -- A diferencia del anterior, le he metido el advance a sumar a los royalties, y para meter el advance he tenido que hacer un join con titles.
SELECT royalties_per_title.au_id, SUM(titles.advance + TOTAL_ROYALTIES) as TOTAL_PROFIT
FROM
	(SELECT royalty_per_sale.title_id, royalty_per_sale.au_id, SUM(ROYALTY) as TOTAL_ROYALTIES
	FROM
		(SELECT titleauthor.title_id, titleauthor.au_id, titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 as ROYALTY
		FROM titleauthor
		INNER JOIN titles ON titles.title_id = titleauthor.title_id
		INNER JOIN sales ON sales.title_id = titleauthor.title_id) royalty_per_sale
	GROUP BY royalty_per_sale.au_id, royalty_per_sale.title_id) royalties_per_title
JOIN titles ON titles.title_id = royalties_per_title.title_id
GROUP BY royalties_per_title.au_id
ORDER BY TOTAL_PROFIT DESC
LIMIT 3;

-- -- La siguiente query no funciona (porque las tablas no están creadas), pero muestra de forma más clara el concepto de la query anterior. De hecho, es el concepto siguietne de temporary tables.
SELECT royalties_per_title.au_id, SUM(titles.advance + TOTAL_ROYALTIES) as TOTAL_PROFIT
FROM royalties_per_title
JOIN titles ON titles.title_id = royalties_per_title.title_id
GROUP BY royalties_per_title.au_id
ORDER BY TOTAL_PROFIT DESC
LIMIT 3;

-- =================
-- CHALLENGE 2 - Alternative Solution
-- Hago el chalenge anterior pero con temporary tables en lugar de derived tables.
-- Step 1: Calculate the royalties of each sales for each author
SELECT titleauthor.title_id, titleauthor.au_id, titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 as ROYALTY
FROM titleauthor
INNER JOIN titles ON titles.title_id = titleauthor.title_id
INNER JOIN sales ON sales.title_id = titleauthor.title_id;

-- Step 2: Aggregate the total royalties for each title for each author
-- -- Creo la tabla temporal a partir de la query anterior
CREATE TEMPORARY TABLE royalty_per_sale
SELECT titleauthor.title_id, titleauthor.au_id, titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 as ROYALTY
FROM titleauthor
INNER JOIN titles ON titles.title_id = titleauthor.title_id
INNER JOIN sales ON sales.title_id = titleauthor.title_id;

-- -- Utilizo la tabla temporal recién creada para hacer la query del step 2.
SELECT royalty_per_sale.title_id, royalty_per_sale.au_id, SUM(ROYALTY) as TOTAL_ROYALTIES
FROM royalty_per_sale
GROUP BY royalty_per_sale.au_id, royalty_per_sale.title_id;
    
-- Step 3: Calculate the total profits of each author
-- -- Creo la tabla temporal con la query anterior.
CREATE TEMPORARY TABLE royalties_per_title
SELECT royalty_per_sale.title_id, royalty_per_sale.au_id, SUM(ROYALTY) as TOTAL_ROYALTIES
FROM royalty_per_sale
GROUP BY royalty_per_sale.au_id, royalty_per_sale.title_id;

-- -- Calculo el total de profits por autor que provienen de royalties
SELECT royalties_per_title.au_id, SUM(TOTAL_ROYALTIES)
FROM royalties_per_title
GROUP BY royalties_per_title.au_id
ORDER BY SUM(TOTAL_ROYALTIES) DESC;

-- -- SOLUCIÓN FINAL del step 3: Ahora calculo el total de profits por autor que provienen de royalties y advance
-- -- A diferencia del anterior, le he metido el advance a sumar a los royalties, y para meter el advance he tenido que hacer un join con titles.
SELECT royalties_per_title.au_id, SUM(titles.advance + TOTAL_ROYALTIES) as TOTAL_PROFIT
FROM royalties_per_title
JOIN titles ON titles.title_id = royalties_per_title.title_id
GROUP BY royalties_per_title.au_id
ORDER BY TOTAL_PROFIT DESC
LIMIT 3;

-- =================
-- CHALLENGE 3
-- Creo la tabla que pide el enunciado a partir de la última query del challenge anterior (aunque podría haberlo hecho tmabién con la del challenge 1, ya que saca los mismos resultados)
CREATE TABLE most_profiting_authors
SELECT royalties_per_title.au_id, SUM(titles.advance + TOTAL_ROYALTIES) as TOTAL_PROFIT
FROM royalties_per_title
JOIN titles ON titles.title_id = royalties_per_title.title_id
GROUP BY royalties_per_title.au_id;

-- Consulto todos los registos de la tabla recién creada.
SELECT * FROM most_profiting_authors;