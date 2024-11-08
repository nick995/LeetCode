-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | user_id     | int     |
-- | user_name   | varchar |
-- +-------------+---------+
-- user_id is the primary key (column with unique values) for this table.
-- Each row of this table contains the name and the id of a user.
 

-- Table: Register

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | contest_id  | int     |
-- | user_id     | int     |
-- +-------------+---------+
-- (contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
-- Each row of this table contains the id of a user and the contest they registered into.
 

-- Write a solution to find the percentage of the users registered in each contest rounded to two decimals.

-- Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Users table:
-- +---------+-----------+
-- | user_id | user_name |
-- +---------+-----------+
-- | 6       | Alice     |
-- | 2       | Bob       |
-- | 7       | Alex      |
-- +---------+-----------+
-- Register table:
-- +------------+---------+
-- | contest_id | user_id |
-- +------------+---------+
-- | 215        | 6       |
-- | 209        | 2       |
-- | 208        | 2       |
-- | 210        | 6       |
-- | 208        | 6       |
-- | 209        | 7       |
-- | 209        | 6       |
-- | 215        | 7       |
-- | 208        | 7       |
-- | 210        | 2       |
-- | 207        | 2       |
-- | 210        | 7       |
-- +------------+---------+
-- Output: 
-- +------------+------------+
-- | contest_id | percentage |
-- +------------+------------+
-- | 208        | 100.0      |
-- | 209        | 100.0      |
-- | 210        | 100.0      |
-- | 215        | 66.67      |
-- | 207        | 33.33      |
-- +------------+------------+
-- Explanation: 
-- All the users registered in contests 208, 209, and 210. The percentage is 100% and we sort them in the answer table by contest_id in ascending order.
-- Alice and Alex registered in contest 215 and the percentage is ((2/3) * 100) = 66.67%
-- Bob registered in contest 207 and the percentage is ((1/3) * 100) = 33.33%

SELECT *
FROM Users as u
JOIN Register as r
ON u.user_id = r.user_id
ORDER BY user_id

| user_id | user_name | contest_id | user_id |
| ------- | --------- | ---------- | ------- |
| 2       | Bob       | 209        | 2       |
| 2       | Bob       | 208        | 2       |
| 2       | Bob       | 210        | 2       |
| 2       | Bob       | 207        | 2       |
| 6       | Alice     | 209        | 6       |
| 6       | Alice     | 210        | 6       |
| 6       | Alice     | 208        | 6       |
| 6       | Alice     | 215        | 6       |
| 7       | Alex      | 209        | 7       |
| 7       | Alex      | 215        | 7       |
| 7       | Alex      | 208        | 7       |
| 7       | Alex      | 210        | 7       |



SELECT COUNT(u.user_id)
FROM Users as u
JOIN Register as r
ON u.user_id = r.user_id
GROUP BY u.user_id

| user_id | user_name | contest_id | user_id |
| ------- | --------- | ---------- | ------- |
| 2       | Bob       | 207        | 2       |
| 7       | Alex      | 208        | 7       |
| 2       | Bob       | 208        | 2       |
| 6       | Alice     | 208        | 6       |
| 7       | Alex      | 209        | 7       |
| 6       | Alice     | 209        | 6       |
| 2       | Bob       | 209        | 2       |
| 6       | Alice     | 210        | 6       |
| 2       | Bob       | 210        | 2       |
| 7       | Alex      | 210        | 7       |
| 6       | Alice     | 215        | 6       |
| 7       | Alex      | 215        | 7       |


-- total user = SELECT COUNT(DISTINCT user_id) FROM Users

-- we also need to find a total number of user who is in the contest_id, it means 
-- we need to group by contest_id and count user_id

SELECT contest_id, ROUND(COUNT(user_id) * 100.0 / (SELECT COUNT(DISTINCT user_id) FROM Users), 2) AS percentage
FROM Register AS r
GROUP BY contest_id
ORDER BY percentage DESC,
    contest_id;

