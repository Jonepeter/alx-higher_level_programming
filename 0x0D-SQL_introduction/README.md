SQL

SQL stands for Structured Query Language. SQL is used to create, remove, alter the database and database objects in a database management system and to store, retrieve, update the data in a database. SQL is a standard language for creating, accessing, manipulating database management system. SQL works for all modern relational database management systems, like SQL Server, Oracle, MySQL, etc.

Different types of SQL commands

SQL commands can be categorized into five categories based on their functionality.

DDL

DDL stands for data definition language. DDL commands are used for creating and altering the database and database object in the relational database management system, like CREATE DATABASE, CREATE TABLE, ALTER TABLE, etc. The most used DDL commands are CREATE, DROP, ALTER, and TRUNCATE. CREATE

CREATE command is used to create a database and database object like a table, index, view, trigger, stored procedure, etc.

Syntax

CREATE TABLE Employee (Id INT, Name VARHCAR(50), Address VARCHAR (100));

ALTER

ALTER command is used to restructure the database object and the settings in the database.

Syntax

ALTER TABLE Employee ADD Salary INT;

TRUNCATE

The TRUNCATE command is used to remove all the data from the table. TRUNCATE command empties a table.

Syntax

TRUNCATE TABLE Employee;

DROP

DROP command is used to remove the database and database object.

Syntax

DROP TABLE Employee; DML

DML stands for data manipulation language. DML commands are used for manipulating data in a relational database management system. DML commands are used for adding, removing, updating data in the database system, like INSERT INTO TableName, DELETE FROM TableName, UPDATE tableName set data, etc. The most used DML commands are INSERT INTO, DELETE FROM, UPDATE. INSERT INTO

INSERT INTO command is used to add data to the database table.

Syntax

INSERT INTO Employee (Id, Name, Address, Salary) VALUES (1, ‘Arvind Singh’, ‘Pune’, 1000);

UPDATE

UPDATE command is used to update data in the database table. A condition can be added using the WHERE clause to update a specific row.

Syntax

UPDATE Employee SET Address = ‘Pune India’, Salary = 100 WHERE Id =1;

DELETE

DELETE command is used to remove data from the database table. A condition can be added using the WHERE clause to remove a specific row which meets the condition.

Syntax

DELETE FROM Employee WHERE Id =1; DQL

DQL stands for the data query language. DQL command is used for fetching the data. DQL command is used for selecting data from the table, view, temp table, table variable, etc. There is only one command under DQL which is the SELECT command.

Syntax

SELECT * FROM Employee;

DCL

DCL stands for data control language. DCL commands are used for providing and taking back the access rights on the database and database objects. DCL command used for controlling user’s access on the data. Most used DCL commands are GRANT and REVOKE.

GRANT

GRANT is used to provide access right to the user.

Syntax GRANT INSERT, DELETE ON Employee TO user;

REVOKE

REVOKE command is used to take back access right from the user, it cancels access right of the user from the database object.

Syntax REVOKE ALL ON Employee FROM user;

TCL

TCL stands for transaction control language. TCL commands are used for handling transactions in the database. Transactions ensure data integrity in the multi-user environment. TCL commands can rollback and commit data modification in the database. The most used TCL commands are COMMIT, ROLLBACK, SAVEPOINT, and SET TRANSACTION.

COMMIT

COMMIT command is used to save or apply the modification in the database.

ROLLBACK

ROLLBACK command is used to undo the modification.

SAVEPOINT

SAVEPOINT command is used to temporarily save a transaction, the transaction can roll back to this point when it's needed.

reference https://www.c-sharpcorner.com/article/introduction-to-sql-and-sql-commands/#:~:text=SQL%20stands%20for%20Structured%20Query,accessing%2C%20manipulating%20database%20management%20system.
