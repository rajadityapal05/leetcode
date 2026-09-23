# Write your MySQL query statement below
SELECT employee_id
FROM Employees

UNION

SELECT employee_id
FROM Salaries

EXCEPT

SELECT e.employee_id
FROM Employees e
JOIN Salaries s
    ON e.employee_id = s.employee_id

ORDER BY employee_id;