-- TCL (Transaction Control Language) commands are used to manage transactions in a database. They ensure that the database remains consistent even in the event of errors or failures. The basic TCL commands are COMMIT, ROLLBACK, and SAVEPOINT.

-- examples of using these TCL commands with the provided Customers, Drivers, and Vehicles tables:

-- Using COMMIT and ROLLBACK
-- Start a transaction to insert a new customer and driver, and commit if successful:

use ola;
-- Start a new transaction
START TRANSACTION;

-- Insert a new customer with a unique CustomerID
INSERT INTO Customers (CustomerID, Name, Email, Phone, RegistrationDate)
VALUES (4, 'Amit Verma', 'amit.verma@example.com', '9876543214', '2024-01-03');

-- Insert a new driver with a unique DriverID
INSERT INTO Drivers (DriverID, Name, Phone, LicenseNumber, Rating)
VALUES (4, 'Deepak Yadav', '9876543215', 'LIC789012', 4.6);

-- Commit the transaction
COMMIT;

-- Starting a transaction, inserting data, and rolling back the transaction in case of an error:
START TRANSACTION; INSERT INTO Drivers (DriverID, Name, Phone, LicenseNumber, Rating) VALUES (4, 'Deepak Yadav', '9876543215', 'LIC789012', 4.6); ROLLBACK;

-- Using SAVEPOINT and ROLLBACK TO SAVEPOINT
START TRANSACTION; SAVEPOINT after_customer_insert; INSERT INTO Customers (CustomerID, Name, Email, Phone, RegistrationDate) VALUES (4, 'Amit Verma', 'amit.verma@example.com', '9876543214', '2024-01-03'); SAVEPOINT after_driver_insert; INSERT INTO Drivers (DriverID, Name, Phone, LicenseNumber, Rating) VALUES (4, 'Deepak Yadav', '9876543215', 'LIC789012', 4.6); ROLLBACK TO after_customer_insert; COMMIT;



