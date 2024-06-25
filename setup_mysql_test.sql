-- Create the database hbnb_test_db if it doesn't exist
-- Create the user hbnb_test if it doesn't exist
-- Grant all privileges on hbnb_test_db to hbnb_test
-- Grant SELECT privilege on performance_schema to hbnb_test
-- Flush privileges to ensure changes take effect

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
