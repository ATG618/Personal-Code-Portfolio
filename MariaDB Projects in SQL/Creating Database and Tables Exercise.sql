--Create database rookery
CREATE DATABASE rookery;

--Drop database rookery
DROP DATABASE rookery;

-- Create database rookery
CREATE DATABASE rookery
CHARACTER SET latin1
COLLATE latin1_bin;

--show all databases
SHOW DATABASES;

--Create birds table
CREATE TABLE birds (
    bird_id INT AUTO_INCREMENT PRIMARY KEY
    scientific_name VARCHAR(255) UNIQUE
    common_name VARCHAR(50)
    family_id INT
    description TEXT
);

--Insert Data into Birds Table
INSERT INTO birds (scientific_name, common_name)
VALUES ('Charadrius vociferus','Killdeer'),
    ('Gavia immer','Great Northern Loon'),
    ('Aix sponsa','Wood Duck'),
    ('Chordeiles minor','Common Nighthawk'),
    ('Sitta carolinensis','White-breasted Nuthatch'),
    ('Apteryx mantelli', 'North Island Brown Kiwi');
    
--Select data from table
SELECT * FROM birds;

--Create database birdwatchers
CREATE DATABASE birdwatchers;

--Create table in birdwatchers
CREATE TABLE birdwatchers.humans(
    human_id INT AUTO_INCREMENT PRIMARY KEY,
    formal_title VARCHAR(25),
    name_first VARCHAR(25),
    name_last VARCHAR(25),
    email_address VARCHAR(255)
);

--Add sample data to humans table
INSERT INTO birdwatchers.humans
    (formal_title, name_first, name_last, email_address)
    VALUES
    ('Mr.', 'Russell', 'Dyer', 'russell@email.com'),
    ('Mr.', 'Richard', 'Stringer', 'richard@email.com'),
    ('Ms.', 'Rusty', 'Osborne', 'rusty@email.com'),
    ('Ms.', 'Lexi', 'Hollar', 'alexandra@email.com');
    
--Create bird families table
CREATE TABLE bird_families(
    family_id INT AUTO_INCREMENT PRIMARY KEY,
    scientific_name VARCHAR(255) UNIQUE,
    brief_description VARCHAR(255)
);

--Create table for order of birds
CREATE TABLE bird_orders(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    scientific_name VARCHAR(255) UNIQUE,
    brief_description VARCHAR(255),
    order_image BLOB
) DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--Exercise 1

--Drop Table bird_orders
DROP TABLE bird_orders;

--Create table, change brief description to text
CREATE TABLE bird_orders(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    scientific_name VARCHAR(255) UNIQUE,
    brief_description TEXT,
    order_image BLOB
) DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--Exercise 2

--Create reference table for identifying birds
CREATE TABLE birds_wing_shapes(
    wing_id VARCHAR(2) UNIQUE,
    wing_shape VARCHAR(25),
    wing_example BLOB
);

--Exercise 3

--Drop bird_wing_shapes table
DROP TABLE birds_wing_shapes;

--create table bird_wing_shapes with different engine
CREATE TABLE birds_wing_shapes(
    wing_id VARCHAR(2) UNIQUE,
    wing_shape VARCHAR(25),
    wing_example BLOB
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--Exercise 4

--Create two additional tables
CREATE TABLE birds_body_shapes(
    body_id VARCHAR(3) UNIQUE,
    body_shape VARCHAR(25),
    body_example BLOB
)ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
CREATE TABLE birds_bill_shapes(
    bill_id VARCHAR(2) UNIQUE,
    bill_shape VARCHAR(25),
    bill_example BLOB
)ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;