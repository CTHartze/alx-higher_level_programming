-- Commands list all cities in California that can be found in database hbtn_0d_usa, in ascending order
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
