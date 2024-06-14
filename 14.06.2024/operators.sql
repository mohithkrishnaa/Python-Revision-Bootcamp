-- In SQL, operators are symbols or keywords used to specify conditions in SQL statements and to perform various operations on data.

-- Arithmetic Operators
-- Arithmetic operators are used to perform mathematical operations on numerical data.

-- + : Addition
-- * : Multiplication
-- / : Division
-- % : Modulus (remainder)

-- Addition
SELECT 10 + 5 AS Sum;

-- Subtraction
SELECT 10 - 5 AS Difference;

-- Multiplication
SELECT 10 * 5 AS Product;

-- Division
SELECT 10 / 5 AS Quotient;

-- Modulus
SELECT 10 % 3 AS Remainder;

-- 2. Comparison Operators
-- Comparison operators are used to compare two values and return a boolean result.

-- = : Equal to
-- <> or != : Not equal to
-- > : Greater than
-- < : Less than
-- >= : Greater than or equal to
-- <= : Less than or equal to

-- Equal to
SELECT * FROM Customers WHERE CustomerID = 1;

-- Not equal to
SELECT * FROM Customers WHERE CustomerID <> 1;

-- Greater than
SELECT * FROM Customers WHERE CustomerID > 1;

-- Less than
SELECT * FROM Customers WHERE CustomerID < 10;

-- Greater than or equal to
SELECT * FROM Customers WHERE CustomerID >= 1;

-- Less than or equal to
SELECT * FROM Customers WHERE CustomerID <= 10;

-- 3. Logical Operators
-- Logical operators are used to combine multiple conditions in SQL statements.

-- AND : True if both conditions are true
-- OR : True if at least one condition is true
-- NOT : True if the condition is not true

-- AND
SELECT * FROM Customers WHERE CustomerID > 1 AND CustomerID < 10;

-- OR
SELECT * FROM Customers WHERE CustomerID = 1 OR CustomerID = 10;

-- NOT
SELECT * FROM Customers WHERE NOT CustomerID = 1;

-- 4. Bitwise Operators
-- Bitwise operators are used to perform bit manipulation between two integer values.

-- & : Bitwise AND
-- | : Bitwise OR
-- ^ : Bitwise XOR
-- ~ : Bitwise NOT

-- Bitwise AND
SELECT 5 & 3 AS BitwiseAndResult;

-- Bitwise OR
SELECT 5 | 3 AS BitwiseOrResult;

-- Bitwise XOR
SELECT 5 ^ 3 AS BitwiseXorResult;

-- Bitwise NOT
SELECT ~5 AS BitwiseNotResult;
