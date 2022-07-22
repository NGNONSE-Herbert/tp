USE classicmodels;
SELECT * FROM offices;
select officeCode, count(officeCode) as number_office from employees group by officeCode order by number_office desc limit 1;
