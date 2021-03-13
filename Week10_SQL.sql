
-- Practical
-- ------------- 
-- Create a database of your own choice. It is must be a meaningful/thought out database. 
-- Create a table with a primary key and the correct datatypes. Include a minimum of 5 fields. View the table structure to make sure it is setup correctly. 

-- creat sales database and then create customer table with 5 fields.
create database sales;
use sales;
CREATE TABLE customer(
cust_id INT PRIMARY KEY,
f_name VARCHAR(20) NOT NULL,
l_name VARCHAR(20) NOT NULL,
gender CHAR(1),
store_id INT
);
explain customer;

-- Practical 
-- • Enter 10 records and view them 

INSERT INTO customer VALUES(1, "John", "Doe", "M", NULL);
INSERT INTO customer VALUES(2, "Jane", "Doe", "F", 1);
INSERT INTO customer VALUES(3, "Elaine", "Smith", "F", 2);
INSERT INTO customer VALUES(4, "Adam", "Gelvin", "M", 3);
INSERT INTO customer VALUES(5, "Robert", "Sam", "M", 1);
INSERT INTO customer VALUES(6, "Betty", "J.", "F", 2);
INSERT INTO customer VALUES(7, "Alisha", "T.", "F", 3);
INSERT INTO customer VALUES(8, "Matt", "Price", "M", 1);
INSERT INTO customer VALUES(9, "Bob", "Byron", "M", 1);
INSERT INTO customer VALUES(10, "Katherine", "Emerson", "F", 3);
select * from customer;

-- • Update a record 

UPDATE customer SET store_id=1 WHERE cust_id=1;

-- • Delete a record 
DELETE FROM customer WHERE cust_id = 10;
select * from customer;

-- • Run a simple query (one field/column) 
SELECT f_name FROM customer;

-- • Run a complex query (more than one field/column) 
SELECT f_name, l_name FROM customer;

-- •Retrieve all your data sorted in ascending order on an appropriate field
SELECT * FROM customer ORDER BY f_name;


-- Home learning task
-- ----------------------
-- • Expand/create a relational database. (2 tables). • Enter data into your 2nd table.
CREATE TABLE store(
store_id INT PRIMARY KEY,
address VARCHAR(20) NOT NULL,
manager VARCHAR(20) NOT NULL
);
explain store;
INSERT INTO store VALUES(1, "1234 Delaware Avenue", "Ashley");
INSERT INTO store VALUES(2, "1234 West Street", "Max");
INSERT INTO store VALUES(3, "1234 Kirkwood Street", "Emily");
select * from store;

-- • Join tables.
SELECT customer.store_id , store.store_id 
FROM customer
INNER JOIN store
ON customer.store_id = store.store_id;

-- View and show both table structures and data. 
explain customer;
explain store;

-- • Run a simple query – searching one table. 

SELECT * FROM store WHERE manager = "Max";
-- • Run a complex query demonstrate the relations between the 2 tables. 

SELECT * FROM customer, store WHERE store.store_id = 1 AND customer.f_name = "Matt";

-- • Filter data using comparison operators. 

SELECT * FROM customer WHERE cust_id between 1 and 5;


