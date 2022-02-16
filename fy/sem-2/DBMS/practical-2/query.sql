-- @BLOCK
SELECT * FROM employee;

-- @BLOCK
SELECT * FROM dept;

-- @BLOCK 
/* List the description of the table */
DESC employee;

-- @BLOCK 
/* List all the databases */
SHOW DATABASES;

-- @BLOCK
/* Switch database */
USE test;

-- @BLOCK
/* List database using wildcards */
SHOW DATABASES LIKE 'demo%';

-- @BLOCK 
/* Creating database */
CREATE DATABASE demodb;

-- @BLOCK
/* Create a table */
CREATE TABLE car(
    brand VARCHAR(255),
    hp INT
);

-- @BLOCK
/* Dropping tables */
DROP TABLE students;

-- @BLOCK
/* List all the tables in the database */
SHOW TABLES;

-- @BLOCK
/* Deleting records */
TRUNCATE TABLE  ;
-- @BLOCK
/* Create employee table */
CREATE TABLE employee(
    eid INT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) UNIQUE,
    salary INT,
    age INT CHECK( age >= 18),
    city VARCHAR(20) DEFAULT 'MUMBAI',
    PRIMARY KEY(eid)
);

-- @BLOCK
/* Create department table */
CREATE TABLE dept(
    did INT PRIMARY KEY,
    dname VARCHAR(20),
    eid INT,
    FOREIGN KEY(eid) REFERENCES employee(eid)
);

-- @BLOCK
/* Create a record in table */
INSERT INTO employee(eid, first_name, last_name, salary, age) VALUES(5, "Alex", "Simons", 50500, 56); 

-- @BLOCK
/* Inserting records in the department table */
INSERT INTO dept(did, dname, eid) VALUES(3, "DevOps", 5);

-- @BLOCK
/* Updating a record */
UPDATE dept set dname='IT' WHERE did=1;
