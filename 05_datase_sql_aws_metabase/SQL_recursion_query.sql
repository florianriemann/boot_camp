WITH RECURSIVE ctename AS (
      SELECT 
				  EMPLOYEE_ID
				, FIRST_NAME
				, FIRST_NAME::TEXT AS PATH_
				, 1                                      AS LEVEL
      FROM EMPLOYEES
      WHERE 
		--    EMPLOYEE_ID = 1
		    REPORTS_TO IS NULL
	UNION ALL
	SELECT 
				  emp.EMPLOYEE_ID
				, emp.FIRST_NAME
				, ctename.PATH_ || ' <- ' || emp.FIRST_NAME
				, ctename.LEVEL + 1     AS LEVEL
	FROM   EMPLOYEES emp
	JOIN     ctename     ON emp.REPORTS_TO = ctename.EMPLOYEE_ID
)

SELECT * FROM ctename;