select customerName, count(customers.customerNumber) as qte_produit_achete, amount as montant
from customers
inner join payments on customers.customerNumber = payments.customerNumber
group by payments.customerNumber
order by montant desc
