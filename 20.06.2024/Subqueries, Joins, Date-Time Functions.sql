-- Create the database
CREATE DATABASE  phone_store;
USE phone_store;

-- Create the tables
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

-- Subquery to find phones priced above the average price
SELECT model, price
FROM phones
WHERE price > (SELECT AVG(price) FROM phones);

-- Subquery to find manufacturers who have phones priced above a certain amount
SELECT manufacturer_name
FROM manufacturers
WHERE manufacturer_id IN (
    SELECT manufacturer_id
    FROM phones
    WHERE price > 1000
);

-- Using Joins
-- Inner Join to get phone details with manufacturer names
SELECT p.model, m.manufacturer_name
FROM phones p
INNER JOIN manufacturers m ON p.manufacturer_id = m.manufacturer_id;

-- Left Join to include all manufacturers, even if they have no phones listed
SELECT m.manufacturer_name, COUNT(p.phone_id) AS phone_count
FROM manufacturers m
LEFT JOIN phones p ON m.manufacturer_id = p.manufacturer_id
GROUP BY m.manufacturer_name;

-- Using Date/Time Functions
-- Selecting phones released after a specific date
SELECT model, release_date
FROM phones
WHERE release_date > '2022-01-01';

-- Calculating how long ago each phone was released
SELECT model, release_date, DATEDIFF(CURDATE(), release_date) AS days_since_release
FROM phones;
