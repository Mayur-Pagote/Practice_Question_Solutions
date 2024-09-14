SELECT eUNI.unique_id, e.name 
FROM Employees e
LEFT JOIN EmployeeUNI eUNI
ON e.id = eUNI.id;
