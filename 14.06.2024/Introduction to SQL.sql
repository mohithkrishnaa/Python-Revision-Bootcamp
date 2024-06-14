-- SQL, or Structured Query Language, is a standard programming language used to manage and manipulate relational databases.
-- SQL is used to perform various operations on the data stored in databases such as querying, updating, inserting, and deleting data.
 -- DDL (Data Definition Language) Commands: they are used to define the database schema
create database Ola;
use Ola;

-- creating cutomer's table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(15),
    RegistrationDate DATE
);

-- creating Driver's table:
CREATE TABLE Drivers (
    DriverID INT PRIMARY KEY,
    Name VARCHAR(100),
    Phone VARCHAR(15),
    LicenseNumber VARCHAR(50),
    Rating DECIMAL(3, 2)
);

-- creating vehicle table:
CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY,
    DriverID INT,
    Model VARCHAR(100),
    LicensePlate VARCHAR(20),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);

-- inserting data to customer table:
INSERT INTO Customers (CustomerID, Name, Email, Phone, RegistrationDate)
VALUES (1, 'Ravi Kumar', 'ravi.kumar@example.com', '9876543210', '2024-01-01'),
       (2, 'Priya Sharma', 'priya.sharma@example.com', '9876543211', '2024-01-02');

-- inserting data to driver's table:
INSERT INTO Drivers (DriverID, Name, Phone, LicenseNumber, Rating)
VALUES (1, 'Rajesh Singh', '9876543212', 'LIC123456', 4.5),
       (2, 'Suman Das', '9876543213', 'LIC654321', 4.7);

-- inserting data to vehicle table:
INSERT INTO Vehicles (VehicleID, DriverID, Model, LicensePlate)
VALUES (1, 1, 'Maruti Suzuki Swift', 'KA01AB1234'),
       (2, 2, 'Hyundai i20', 'KA02CD5678');

-- Querying Data

-- Select All Customers
SELECT * FROM Customers;

-- Updating Data
-- Update Customer's Email
UPDATE Customers
SET Email = 'ravi.kumar.new@example.com'
WHERE CustomerID = 1;

-- Update Driver's Rating
UPDATE Drivers
SET Rating = 4.8
WHERE DriverID = 1;

-- Deleting Data
-- Delete a Customer
DELETE FROM Customers
WHERE CustomerID = 2;
