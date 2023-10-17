/* Command lists all records of the table.
 Records sorted in descending score. */
SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
