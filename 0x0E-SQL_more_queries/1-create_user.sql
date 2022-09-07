-- script that creates the MySQL server user user_0d_1.
-- QUERY
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- QUERY
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- QUERY
FLUSH PRIVILEGES;
