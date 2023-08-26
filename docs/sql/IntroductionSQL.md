# SQL Basics

## Introduction to SQL

SQL stands for Structured Query Language and is used to manage and manipulate relational databases. A database is a place where data is stored, and it can take various forms such as relational, NoSQL, document-based, and graph databases.

### Relational Databases

In the context of data engineering, we often deal with relational databases. These databases are managed by Relational Database Management Systems (RDBMS).

#### Tables and Schema

A table is a collection of data organized in rows and columns. Each table has a schema that defines the structure of the table, including the names of columns and their corresponding data types.

##### Example:

            CREATE TABLE Employee (
                Name char(50),
                Age int
            );

In the "Employee" table, we have two columns: "Name" with data type char(50) and "Age" with data type int.

Rows and Fields
A row represents a single record in the table, and each field within a row corresponds to a specific column in that table.

###### Example:

            | Name      | Age |
            |-----------|-----|
            | Akash     | 29  |
            | Prathyush | 26  |

#### SQL Commands
SQL commands are categorized into three main groups:

##### Data Definition Language (DDL)
DDL deals with the creation and modification of database objects, like tables, indexes, and constraints.

###### Example: Creating a table

            CREATE TABLE Students (
                ID int PRIMARY KEY,
                Name varchar(100),
                Age int
            );

##### Data Manipulation Language (DML)
DML is used for managing data stored within the database.

###### Example: Inserting data

            INSERT INTO Students (ID, Name, Age) VALUES (1, 'Alice', 21);

##### Data Control Language (DCL)
DCL is responsible for controlling access to data within the database.

###### Example: Granting privileges

            GRANT SELECT ON Students TO User;

##### Basic SQL Queries
###### SELECT Statement
The SELECT statement retrieves data from a table.

Example:

            SELECT * FROM Employees;
###### WHERE Clause
The WHERE clause is used to filter rows based on a specified condition.

Example:

SELECT * FROM Employees WHERE Age > 25;

###### GROUP BY and Aggregate Functions
GROUP BY is used to group rows that have the same values in specified columns. Aggregate functions like COUNT, SUM, AVG, etc., are often used with GROUP BY.

Example:

            SELECT Department, COUNT(*) FROM Employees GROUP BY Department;

###### ORDER BY
The ORDER BY clause is used to sort the result set in ascending or descending order based on specified columns.

Example:

            SELECT Name, Age FROM Employees ORDER BY Age DESC;

###### LIMIT
The LIMIT clause is used to restrict the number of rows returned by a query.

Example:

            SELECT * FROM Employees LIMIT 10;