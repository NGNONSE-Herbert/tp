USE classicmodels;
select  month(shippedDate), productName, count(quantityOrdered) as quantite
from orders
INNER JOIN orderdetails on orderdetails.orderNumber = orders.orderNumber
inner join products on products.productCode = orderdetails.productCode
where status = "shipped"
group by month(shippedDate) 
order by month(shippedDate);