/* Complex Joins Example */
use ola;
-- Assume we have tables: Customers, Drivers, and Vehicles

-- Query to get customer details along with their assigned driver and vehicle information
SELECT c.Name AS CustomerName, d.Name AS DriverName, v.Model AS VehicleModel
FROM Customers c
LEFT JOIN Vehicles v ON c.CustomerID = v.DriverID
LEFT JOIN Drivers d ON v.DriverID = d.DriverID;

-- We use `LEFT JOIN` to join the `Customers` table with the `Vehicles` table based on `CustomerID` and `DriverID`.
-- Then, we use another `LEFT JOIN` to join the `Vehicles` table with the `Drivers` table based on `DriverID`.
-- This query retrieves the `Name` of the customer (`Customers` table), the `Name` of the driver (`Drivers` table), and the `Model` of the vehicle (`Vehicles` table) assigned to each customer.


-- Adjust table and column names (`Customers`, `Drivers`, `Vehicles`, `CustomerID`, `DriverID`, `Name`, `Model`, etc.) as per your actual database schema.
-- The `LEFT JOIN` ensures that all rows from the `Customers` table are included in the result, even if there are no matching rows in the `Vehicles` or `Drivers` tables.
-- This example demonstrates how to construct SQL queries with complex joins to retrieve data from multiple related tables in the Ola database schema.
