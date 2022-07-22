USE classicmodels;
select  month(shippedDate), count(quantityOrdered) as quantite
from orders
INNER JOIN orderdetails on orderdetails.orderNumber = orders.orderNumber
where status = "Shipped"
group by month(shippedDate) 
order by month(shippedDate);
