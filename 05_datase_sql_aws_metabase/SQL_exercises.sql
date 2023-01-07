-- 1. Get the names and the quantities in stock for each product.
SELECT 
	  product_name
	, units_in_stock
FROM 
	products
;

-- 2. Get a list of current products (Product ID and name).
SELECT 
	  product_name
	, product_id
FROM
	products
WHERE discontinued = 0
;

-- 3. Get a list of the most and least expensive products (name and unit price).
SELECT 
	  product_name
	, unit_price
FROM 
	products
WHERE 
			unit_price = ( SELECT MAX( unit_price) FROM products )
	OR	unit_price = ( SELECT MIN( unit_price)  FROM products )
;

-- 4. Get products that cost less than $20.
SELECT 
	  product_name
	, unit_price
FROM 
	products
WHERE 
	unit_price < 20
ORDER BY unit_price ASC
;

-- 5. Get products that cost between $15 and $25.
SELECT 
	  product_name
	, unit_price
FROM 
	products
WHERE 
	unit_price BETWEEN 15 AND 25 
ORDER BY 
	unit_price ASC
;

-- 6. Get products above average price.
SELECT 
	  product_name
	, unit_price
FROM 
	products
WHERE 
	unit_price > ( SELECT AVG( unit_price ) FROM products )
ORDER BY 
	unit_price ASC
;

-- 7. Find the ten most expensive products.
SELECT 
	  product_name
	, unit_price
FROM 
	products
ORDER BY 
	unit_price DESC
LIMIT (10)
;

-- 8. Get a list of discontinued products (Product ID and name).
SELECT 
	  product_name
	, product_id
FROM 
	products
WHERE 
	discontinued = 1
;

-- 9. Count current and discontinued products.
SELECT 
	  discontinued
	, COUNT( product_id )           AS "(un)current products"
FROM 
	products
GROUP BY 
	discontinued
;

-- 10. Find products with less units in stock than the quantity on order.
SELECT 
	  product_name
	, units_in_stock
	, units_on_order
FROM 
	products
WHERE 
	units_in_stock < units_on_order
ORDER BY 
	units_in_stock 
;

-- 11. Find the customer who had the highest order amount
SELECT 
	  ordr.customer_id
	, COUNT( oddt.order_id )           AS "Amount_orders"
FROM 
				 ( SELECT * FROM order_details )     oddt
LEFT JOIN ( SELECT * FROM orders            )     ordr     on ordr.ORDER_ID = oddt.ORDER_ID
GROUP BY 
	ordr.customer_id
ORDER BY "Amount_orders" DESC
;

-- 12. 
SELECT
	  c.contact_name
	, o.order_id
	, o.employee_id
	, e.first_name
	, e.last_name
FROM customers c
INNER JOIN orders         o                           ON c.customer_id  = o.customer_id
INNER JOIN employees e                            ON o.employee_id = e.employee_id
ORDER BY c.contact_name
;

-- 13. Find the hiring age of each employee
SELECT 
	     employee_id
	, ( ROUND( ( hire_date - birth_date ) / 365,2 ) )          AS "Hire_age"
--	, AGE( hire_date, birth_date )                                        AS "Hire_age"
FROM employees
;

-- 14.Create views and/or named queries for some of these queries

CREATE OR REPLACE VIEW CUSTOMERS_MA AS 
SELECT *
FROM customers
WHERE CONTACT_NAME LIKE '%Ma%'
;

SELECT *
FROM CUSTOMERS_MA
;
