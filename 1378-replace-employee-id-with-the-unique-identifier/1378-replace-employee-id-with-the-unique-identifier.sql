# Write your MySQL query statement below

 SELECT ei.unique_id,e.name FROM Employees As e LEFT JOIN EmployeeUNI AS ei ON e.id = ei.id  ; 