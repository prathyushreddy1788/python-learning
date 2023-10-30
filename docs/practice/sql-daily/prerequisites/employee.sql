CREATE TABLE departments (
  department_id INT PRIMARY KEY,
  department_name VARCHAR(50)
);

CREATE TABLE employees (
  employee_id INT PRIMARY KEY,
  employee_name VARCHAR(50),
  department_id INT,
  salary DECIMAL(10, 2),
  city VARCHAR(50),
  FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO departments (department_id, department_name)
VALUES (1, 'Finance'), (2, 'HR'), (3, 'Marketing'), (4, 'IT');

INSERT INTO employees (employee_id, employee_name, department_id, salary, city)
VALUES (1, 'John Doe', 1, 5000.00, 'New York'),
       (2, 'Jane Smith', 2, 4000.00, 'New York'),
       (3, 'Michael Johnson', 1, 4500.00, 'Chicago'),
       (4, 'Emily Brown', 3, 5500.00, 'Chicago'),
       (5, 'David Williams', 4, 6000.00, 'Los Angeles');
