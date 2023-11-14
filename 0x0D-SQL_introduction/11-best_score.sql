-- script 11
-- script _that lists all reco_rds with a s_core >= 10 in the ta_ble
-- second_table of the d_atabase _hbtn_0c_0 in your _MySQL server.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
