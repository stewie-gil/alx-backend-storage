-- creating a function that divies two numbers
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
	IF b = 0 THEN
	   RETURN 0;
	END IF;

	RETURN a / b;
END;
//
DELIMITER ;
