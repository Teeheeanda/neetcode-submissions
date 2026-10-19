select name
from customers
where id not in (select DISTINCT customer_id from orders);