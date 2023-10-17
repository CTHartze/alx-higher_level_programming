-- Commands list number of records with the same score in the table in my MySQL server.
-- Records sorted in descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
