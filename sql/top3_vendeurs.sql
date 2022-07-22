select firstName, lastName, count(salesRepEmployeeNumber) as nombreDeVente
from employees 
inner join customers on employees.employeeNumber = customers.salesRepEmployeeNumber
group by employeeNumber
order by nombreDeVente desc limit 3;
