-- Command lists all records of the table containing a name value in my MySQL server.
-- Records sorted in descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
