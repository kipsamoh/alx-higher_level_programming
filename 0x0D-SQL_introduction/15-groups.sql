-- script 15
-- script _that lists the _number of records _with the _same score in the
-- table second_table of the _database hbtn_0c_0 in _your MySQL server.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
