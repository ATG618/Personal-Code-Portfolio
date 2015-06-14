-- Create two new tables in test database, display database structure
CREATE TABLE test.contacts (name CHAR(30), phone_work CHAR(12), phone_mobile CHAR(12),
email CHAR(120), relation_id INT
);
CREATE TABLE test.relation_types (relation_id INT, relationship CHAR(30)
);
DESCRIBE contacts;
DESCRIBE relation_types;

-- Insert fake data into tables, constraints for relationship are: 
-- Family, Friend, Colleague
INSERT INTO relation_types VALUES (1,'Family'), (2, 'Friend'), (3, 'Colleague');
INSERT INTO contacts VALUES ('John','123-456-6789', '123-45-6458', 'john@johnsite.com',1),
('Bob', '618-446-1254', '618-456-4587', 'bob@bobsite.com',2),
('Lisa', '314-456-1546','314-411-5894', 'lisa@lisasite.com',3),
('Tim', '618-447-4568', '618-123-4487', 'tim@timsite.com', 4),
('Jake', '816-441-4463', '816-994-6123', 'jake@jakesite.com', 1)
;

-- Update values in contact table
UPDATE contacts SET phone_work = '816-114-1236' WHERE name = 'John';
UPDATE contacts SET relation_id = 3 WHERE name = 'Tim';

-- Join contact and relation table into one based on given data, when selecting column
-- with same field you must specific table.column to distinguish between columns
SELECT name,phone_work,phone_mobile,email,relationship
FROM contacts JOIN relation_types
WHERE contacts.relation_id = relation_types.relation_id;

