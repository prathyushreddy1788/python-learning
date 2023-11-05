
#Group by the average salary for each department
select department_name,avg(salary)
from departments inner join employees
on departments.department_id = employees.department_id
group by department_name;


select city, count(*) as no_of_employees from employees
group by city;


select *
from departments inner join employees
on departments.department_id = employees.department_id;

select *
from employees left join departments
on employees.department_id = departments.department_id;