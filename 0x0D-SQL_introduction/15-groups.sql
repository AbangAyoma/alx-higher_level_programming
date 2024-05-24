-- Script that list the number of records with the same score in the table second_table
-- of the database hbtn_0c_0, the result should display : the score, 
-- the number for this records will be label number, the list should be sorted in desc

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
exit  
