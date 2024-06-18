-- DQL, or Data Query Language, is a subset of SQL (Structured Query Language) focused on querying and retrieving data from a database.
-- DQL primarily deals with the SELECT statement and its various clauses and functions. 

-- SELECT: This command is used to query data from a database. 
-- It retrieves data from one or more tables and allows for filtering, sorting, and combining data in various ways.
-- FROM: Specifies the table from which to retrieve the data
use ola;
SELECT * FROM customers;

-- WHERE: Filters records that meet certain criteria.
SELECT *
FROM Customers
WHERE RegistrationDate > '2024-01-01';

-- ORDER BY: Sorts the result set by one or more columns.
-- GROUP BY: Groups rows that have the same values in specified columns into summary rows.
-- HAVING: Filters groups created by the GROUP BY clause.

-- JOIN: Combines rows from two or more tables based on a related column.
-- INNER JOIN: Selects records that have matching values in both tables

-- Eg:Select vehicles driven by drivers with a rating above 4.6
SELECT v.Model AS VehicleModel, v.LicensePlate, d.Name AS DriverName, d.Rating
FROM Vehicles v
INNER JOIN Drivers d ON v.DriverID = d.DriverID
WHERE d.Rating > 4.6;

-- LEFT JOIN : Selects all records from the left table and the matched records from the right table. The result is NULL from the right side if there is no match.
-- RIGHT JOIN: Selects all records from the right table and the matched records from the left table. The result is NULL from the left side when there is no match.
-- FULL JOIN : Selects all records when there is a match in either left or right table.

SELECT d.*
FROM Drivers d
LEFT JOIN Vehicles v ON d.DriverID = v.DriverID
WHERE v.VehicleID IS NULL;