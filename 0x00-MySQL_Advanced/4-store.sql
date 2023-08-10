-- decreases quantity of an item in 'items' when a new order is added
DELIMITER //
CREATE TRIGGER decrease_item AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END;
//
