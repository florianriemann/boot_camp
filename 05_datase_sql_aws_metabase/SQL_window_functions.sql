WITH CTE_PRODUCTS AS
	(
		SELECT 
								    prod.PRODUCT_NAME
						,             prod.PRODUCT_ID
						,             odet.QUANTITY
						, SUM( odet.QUANTITY ) OVER( PARTITION BY prod.PRODUCT_NAME )        AS SUM_ORDERS_PER_PRODUCT
						, SUM( odet.QUANTITY ) OVER()                                                                                  AS SUM_OF_ALL_ORDERS
		FROM  
							( SELECT * FROM ORDER_DETAILS ) odet
		LEFT JOIN 	( SELECT * FROM PRODUCTS            ) prod     ON odet.PRODUCT_ID = prod.PRODUCT_ID
	)

SELECT 
	  PRODUCT_ID
	, PRODUCT_NAME
	, QUANTITY
	, SUM_ORDERS_PER_PRODUCT
	, SUM_OF_ALL_ORDERS
	, ROUND(  ( cast( SUM_ORDERS_PER_PRODUCT as decimal)  / cast( SUM_OF_ALL_ORDERS as decimal )  ),  2  )   AS PERCANTAGE
FROM 
	CTE_PRODUCTS
;