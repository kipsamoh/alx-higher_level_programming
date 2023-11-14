-- script 16
-- script _that lists all r_ecords of the tab_le second_table of _the
-- database hbtn_0c_0 in your _MySQL server.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
