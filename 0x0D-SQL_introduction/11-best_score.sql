/* Commands list all records in the table with a score >= 10 in current database in my MySQL server.
Records sorted in descending score. */
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
