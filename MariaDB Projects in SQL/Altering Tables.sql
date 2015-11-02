--Altering Tables Chapter

--Using mysql dump to back up databases and specific tables:

--Change directory to desired backup location
cd "path"

--To Back Up Complete Database
mysqldump --user='username' -p rookery > rookery.sql

--To Back Up Database Specific Table
mysqldump --user='username' -p rookery birds > birds.sql

--Make a backup of databas before changes
--To recover database
mysql --user='username' -p rookery < rookery-ch2-end.sql

--Alter table to add columns
ALTER TABLE bird_families ADD COLUMN order_id INT;

--Add columns to test database:
CREATE TABLE test.birds_new LIKE birds;

--switch database and view structure
USE Test DESCRIBE birds_new;

--insert data into a copied table with no data
INSERT INTO birds_new
SELECT * FROM rookery.birds;

--Alternative method to insert data into copied table with no data
CREATE TABLE birds_new_alternative
SELECT * FROM rookery.birds;

--Add column to table
ALTER TABLE birds_new
ADD COLUMN wing_id CHAR(2);

---Delete a column from table
ALTER TABLE birds_new
DROP COLUMN wing_id;

--Add a column to table to specific location
ALTER TABLE birds_new
ADD COLUMN wing_id CHAR(2) AFTER family_id;

--Add multiple columns to a table while specifying order in table
ALTER TABLE birds_new
ADD COLUMN body_id CHAR(2) AFTER wing_id,
ADD COLUMN bill_id CHAR(2) AFTER body_id,
ADD COLUMN endangered BIT DEFAULT b'1' AFTER bill_id,
CHANGE COLUMN common_name common_name VARCHAR(255);

--Update the values of the endangered column
UPDATE birds_new SET endangered = 0
WHERE bird_id IN(1,2,4,5);

--Select columns from birds table where endangered
SELECT bird_id, scientific_name, common_name
FROM birds_new
WHERE endangered \G

--Select columns from birds table where not endangered
SELECT * FROM birds_new
WHERE NOT endangered \G

--Modify column
ALTER TABLE birds_new
MODIFY COLUMN endangered
ENUM('Extinct',
    'Extinct in Wild',
    'Threatened - Critically Endangered',
    'Threatened - Endangered',
    'Threatened - Vulnerable',
    'Lower Risk - Convervation Dependent',
    'Lower Risk - Near Threatened',
    'Lower Risk - Least Concern')
AFTER family_id;

--Display the column settings for column
SHOW COLUMNS FROM birds_new LIKE 'endangered' \G

--Using Dynamic Columns
USE birdwatchers;

CREATE TABLE surveys
(survey_iid INT AUTO_INCREMENT KEY, survey_name VARCHAR(255));

CREATE TABLE survey_questions
(question_id INT AUTO_INCREMENT KEY, 
survey_id INT, 
question VARCHAR(255), 
choices BLOB
);

CREATE TABLE survey_answers(
answer_id INT AUTO_INCREMENT KEY,
human_id INT,
question_id INT,
date_answered DATETIME,
answer VARCHAR(255)
);

--Add fake data to the survey tables:
INSERT INTO surveys (survey_name)
VALUES ("Favorite Birding Location");

INSERT INTO survey_questions
(survey_id, question, choices)
VALUES(LAST_INSERT_ID(), 
"What's your favorite setting for bird-watching?",
COLUMN_CREATE('1','forest','2','shore','3', 'backyard')
);

INSERT INTO surveys (survey_name)
VALUES("Preferred Birds");

INSERT INTO survey_questions
(survey_id, question, choices)
VALUES(LAST_INSERT_ID(),
"which type of birds do you like best?",
COLUMN_CREATE('1','perching', '2', 'shore', '3', 'fowl', '4', 'rapture')
);
 

 --retrieving data from a dynamic column
 SELECT COLUMN_GET (choices, 3 AS CHAR)
 AS 'Location'
 FROM survey_questions
 WHERE survey_id = 1;
 
 --Enter fake survey answers
 INSERT INTO survey_answers(human_id, question_id, date_answered, answer)
 VALUES 
(29,1,NOW(),2),
(29,2,NOW(),2),
(35,1,NOW(),1),
(35,2,NOW(),1),
(26,1,NOW(),2),
(26,1,NOW(),1);


--Count the votes for the first survey question
SELECT IFNULL(COLUMN_GET(choices, answer AS CHAR), 'total')
AS 'Birding Site', COUNT(*) AS 'Votes'
FROM survey_answers
JOIN survey_questions USING(question_id)
WHERE survey_id = 1
AND question_id = 1
GROUP BY answer WITH ROLLUP;

--Create a reference table in rookery
CREATE TABLE rookery.conservation_status
(status_id INT AUTO_INCREMENT PRIMARY KEY,
convervation_category CHAR(10),
conservation_state CHAR(25)
);

--Insert all of the data into this new reference table.
INSERT INTO rookery.conservation_status
(convervation_category, conservation_state)
VALUES ('Extinct', 'Extinct'),
('Extinct','Extinct in Wild'),
('Threatened', 'Critically Endangered'),
('Threatened','Endangered'),
('Threatened', 'Vulnerable'),
('Lower Risk', 'Conservation Dependent'),
('Lower Risk', 'Near Threatened'),
('Lower Risk','Least Concern');


--Select all data in the reference table
SELECT * FROM rookery.conservation_status;

--Change a column's name and default value 
ALTER TABLE birds_new
CHANGE COLUMN endangered convervation_status_id INT DEFAULT 8;
ALTER TABLE birds_new
ALTER convervation_status_id SET DEFAULT 7;

--display changes
SHOW COLUMNS FROM birds_new LIKE 'convervation_status_id' \G


--reset default of column to initial settings
ALTER TABLE birds_new
ALTER convervation_status_id DROP DEFAULT;

--get value of next auto-increment for a given table
SELECT auto_increment
FROM information_schema.tables
WHERE table_name = 'birds';

--set the value of auto-increment for a particular table
ALTER TABLE birds AUTO_INCREMENT = 10;

--Create a table based on another table
CREATE TABLE birds_new LIKE birds;

--Show table structure to confirm auto-increment values,
--update auto-increment value
SHOW CREATE TABLE birds \G
ALTER TABLE birds_new AUTO_INCREMENT =6;

--Create a new table and copy a column settings and data to new table
CREATE TABLE birds_detail
SELECT bird_id, description
FROM birds;

--Remove column description from birds table
ALTER TABLE birds
DROP COLUMN description;



