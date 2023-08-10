-- updating valid_email only when email is changed
DELIMITER //
CREATE TRIGGER update_valid_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
	   SET NEW.valid_email = 0;
	END IF;
END;
//
DELIMITER;
