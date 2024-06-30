-- DELIMITER
-- Delimiter - command used to change the standard delimiter (like a semicolon (;)) to a different character
-- Deterministic - It indicates that the function will always return the same result for the same input values

-- Create the database and tables
USE phone_store;

CREATE TABLE manufacturers (
    manufacturer_id INT AUTO_INCREMENT PRIMARY KEY,
    manufacturer_name VARCHAR(100) NOT NULL
);

CREATE TABLE phones (
    phone_id INT AUTO_INCREMENT PRIMARY KEY,
    model VARCHAR(100) NOT NULL,
    manufacturer_id INT,
    price DECIMAL(10, 2),
    release_date DATE,
    CONSTRAINT fk_manufacturer_id FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id)
);

-- Insert data into manufacturers table
INSERT INTO manufacturers (manufacturer_name) VALUES
('Apple'),
('Samsung'),
('Google'),
('OnePlus');

-- Insert data into phones table
INSERT INTO phones (model, manufacturer_id, price, release_date) VALUES
('iPhone 13 Pro', 1, 1099.99, '2021-09-24'),
('Galaxy S21 Ultra', 2, 1199.99, '2021-01-29'),
('Pixel 6 Pro', 3, 899.99, '2021-10-19'),
('OnePlus 9 Pro', 4, 969.00, '2021-03-23');

-- PROCEDURE
-- It is a set of SQL statements that can be saved and reused
-- Creating a procedure:
USE phone_store;
DELIMITER //
CREATE PROCEDURE select_all_phones()
BEGIN
    SELECT * FROM phones;
END //
DELIMITER ;

CALL select_all_phones();

-- Deleting a procedure:
DROP PROCEDURE select_all_phones;

-- FUNCTION
-- A function is a reusable block of code that performs a specific task and can return a value
-- Function to get manufacturer details
DELIMITER //
CREATE FUNCTION getManufacturerDetails(manufacturerId INT)
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
    DECLARE manufacturerDetails VARCHAR(255);
    SELECT CONCAT('Manufacturer: ', manufacturer_name) INTO manufacturerDetails
    FROM manufacturers
    WHERE manufacturer_id = manufacturerId;
    RETURN manufacturerDetails;
END //
DELIMITER ;

SELECT getManufacturerDetails(1);

-- IN
-- IN is a part of procedures and it allows you to pass values into the procedure
DELIMITER //
CREATE PROCEDURE get_phone_details(IN pid INT)
BEGIN
    SELECT * FROM phones WHERE phone_id = pid;
END //

CALL get_phone_details(1);

DROP PROCEDURE get_phone_details;

-- OUT 
-- OUT is a part of procedure and it allows you to return values from a procedure
DELIMITER //
CREATE PROCEDURE get_phone_count(OUT phone_count INT)
BEGIN
    SELECT COUNT(*) INTO phone_count FROM phones;
END //
DELIMITER ;

CALL get_phone_count(@phone_count);
SELECT @phone_count as phone_count;

DROP PROCEDURE get_phone_count;

-- CURSOR
-- Cursors - used to retrieve and process rows one by one from the result set of a query.
-- They are declared using the DECLARE CURSOR statement, specifying the SELECT query whose result set will be processed.
-- Two types of cursor :-
--  i) User-Defined Cursors - declared by the user to process rows retrieved from a query result set and they are useful when you need to perform custom operations on individual rows

DELIMITER //
CREATE PROCEDURE list_phone_prices()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE phone_name VARCHAR(100);
    DECLARE phone_price DECIMAL(10, 2);
    DECLARE phone_cursor CURSOR FOR SELECT model, price FROM phones;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN phone_cursor;
    read_loop: LOOP
        FETCH phone_cursor INTO phone_name, phone_price;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SELECT CONCAT('Phone: ', phone_name, ', Price: ', phone_price);
    END LOOP;

    CLOSE phone_cursor;
END //
DELIMITER ;

CALL list_phone_prices();

DROP PROCEDURE list_phone_prices;

--  ii) Pre-defined Cursors - system-defined cursors provided by the DBMS. They are often associated with built-in functions or stored procedures that return result sets

DELIMITER //
CREATE PROCEDURE total_price_by_manufacturer(IN manufacturer_name VARCHAR(100), OUT total_price DECIMAL(10, 2))
BEGIN
    SELECT SUM(p.price) INTO total_price
    FROM phones p
    JOIN manufacturers m ON p.manufacturer_id = m.manufacturer_id
    WHERE m.manufacturer_name = manufacturer_name;
END //
DELIMITER ;

CALL total_price_by_manufacturer('Apple', @total_price);
SELECT @total_price as total_price;

DROP PROCEDURE total_price_by_manufacturer;
