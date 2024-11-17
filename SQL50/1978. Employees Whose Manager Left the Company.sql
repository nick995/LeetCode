-- Table: Employees

-- +-------------+----------+
-- | Column Name | Type     |
-- +-------------+----------+
-- | employee_id | int      |
-- | name        | varchar  |
-- | manager_id  | int      |
-- | salary      | int      |
-- +-------------+----------+
-- In SQL, employee_id is the primary key for this table.
-- This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null). 
 

-- Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

-- Return the result table ordered by employee_id.

-- The result format is in the following example.

 

-- Example 1:

-- Input:  
-- Employees table:
-- +-------------+-----------+------------+--------+
-- | employee_id | name      | manager_id | salary |
-- +-------------+-----------+------------+--------+
-- | 3           | Mila      | 9          | 60301  |
-- | 12          | Antonella | null       | 31000  |
-- | 13          | Emery     | null       | 67084  |
-- | 1           | Kalel     | 11         | 21241  |
-- | 9           | Mikaela   | null       | 50937  |
-- | 11          | Joziah    | 6          | 28485  |
-- +-------------+-----------+------------+--------+
-- Output: 
-- +-------------+
-- | employee_id |
-- +-------------+
-- | 11          |
-- +-------------+

-- Explanation: 
-- The employees with a salary less than $30000 are 1 (Kalel) and 11 (Joziah).
-- Kalel's manager is employee 11, who is still in the company (Joziah).
-- Joziah's manager is employee 6, who left the company because there is no row for employee 6 as it was deleted.

WITH CTE AS (
    SELECT employee_id, manager_id
    FROM Employees as e 
    WHERE e.salary < 30000
)
SELECT *
FROM CTE


| employee_id | manager_id |
| ----------- | ---------- |
| 1           | 11         |
| 11          | 6          |


WITH CTE AS (
    SELECT employee_id, manager_id
    FROM Employees as e 
    WHERE e.salary < 30000
)
SELECT *
FROM CTE as cte
LEFT JOIN Employees as e
ON cte.manager_id = e.employee_id

| employee_id | manager_id | employee_id | name   | manager_id | salary |
| ----------- | ---------- | ----------- | ------ | ---------- | ------ |
| 1           | 11         | 11          | Joziah | 6          | 28485  |
| 11          | 6          | null        | null   | null       | null   |


WITH CTE AS (
    SELECT employee_id, manager_id
    FROM Employees AS e 
    WHERE e.salary < 30000
)
SELECT *
FROM CTE AS cte
LEFT JOIN Employees AS e
ON cte.manager_id = e.employee_id

| employee_id | manager_id | employee_id | name   | manager_id | salary |
| ----------- | ---------- | ----------- | ------ | ---------- | ------ |
| 1           | 11         | 11          | Joziah | 6          | 28485  |
| 11          | 6          | null        | null   | null       | null   |


WITH CTE AS (
    SELECT employee_id, manager_id
    FROM Employees AS e 
    WHERE e.salary < 30000
)
SELECT cte.employee_id
FROM CTE AS cte
WHERE NOT EXISTS(
    SELECT *
    FROM Employees as e
    WHERE (cte.manager_id = e.employee_id) 
)

--=================================================



WITH CTE AS (
    SELECT employee_id, manager_id
    FROM Employees AS e 
    WHERE e.salary < 30000
)
SELECT cte.employee_id
FROM CTE AS cte

| employee_id |
| ----------- |
| 13          |
| 17          |
| 7           |
| 2           |
| 14          |


WITH CTE AS (
    SELECT employee_id, manager_id
    FROM Employees AS e 
    WHERE e.salary < 30000
)
SELECT cte.employee_id, cte.manager_id
FROM CTE AS cte
WHERE NOT EXISTS(
    SELECT *
    FROM Employees as e
    WHERE cte.manager_id = e.employee_id
) AND cte.manager_id <> NULL

| employee_id | manager_id |
| ----------- | ---------- |
| 13          | 16         |
| 17          | 20         |
| 7           | 6          |
| 2           | null       |
| 14          | null       |

-- solution

WITH CTE AS (
    SELECT employee_id, manager_id
    FROM Employees AS e 
    WHERE e.salary < 30000
)
SELECT cte.employee_id
FROM CTE AS cte
WHERE NOT EXISTS (
    SELECT 1
    FROM Employees AS e
    WHERE cte.manager_id = e.employee_id
) 
AND cte.manager_id IS NOT NULL
ORDER BY cte.employee_id;
