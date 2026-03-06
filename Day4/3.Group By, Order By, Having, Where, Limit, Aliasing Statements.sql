SELECT *
FROM employee_demographics;

SELECT gender, AVG(age), MAX(age), COUNT(age)
FROM employee_demographics 
GROUP BY gender;

SELECT occupation, salary
FROM employee_salary 
GROUP BY occupation, salary;

SELECT gender, AVG(age)
FROM employee_demographics
GROUP BY gender, age
HAVING AVG(age) > 40;


SELECT *
FROM employee_demographics
ORDER  BY age DESC
LIMIT 2, 1;

SELECT gender, AVG(age) AS Average
FROM employee_demographics
GROUP BY gender
HAVING AVG(age) > 40;
