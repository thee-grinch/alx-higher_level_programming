-- group the sql
SELECT score, count(*) as number
FROM second_table
GROUP BY score;
