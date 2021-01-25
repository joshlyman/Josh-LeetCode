# Write an SQL query to find the average selling price for each product.

# average_price should be rounded to 2 decimal places.

# The query result format is in the following example:

# Prices table:
# +------------+------------+------------+--------+
# | product_id | start_date | end_date   | price  |
# +------------+------------+------------+--------+
# | 1          | 2019-02-17 | 2019-02-28 | 5      |
# | 1          | 2019-03-01 | 2019-03-22 | 20     |
# | 2          | 2019-02-01 | 2019-02-20 | 15     |
# | 2          | 2019-02-21 | 2019-03-31 | 30     |
# +------------+------------+------------+--------+
 
# UnitsSold table:
# +------------+---------------+-------+
# | product_id | purchase_date | units |
# +------------+---------------+-------+
# | 1          | 2019-02-25    | 100   |
# | 1          | 2019-03-01    | 15    |
# | 2          | 2019-02-10    | 200   |
# | 2          | 2019-03-22    | 30    |
# +------------+---------------+-------+

# Result table:
# +------------+---------------+
# | product_id | average_price |
# +------------+---------------+
# | 1          | 6.96          |
# | 2          | 16.96         |
# +------------+---------------+
# Average selling price = Total Price of Product / Number of products sold.
# Average selling price for product 1 = ((100 * 5) + (15 * 20)) / 115 = 6.96
# Average selling price for product 2 = ((200 * 15) + (30 * 30)) / 230 = 16.96

# Write your MySQL query statement below

select Prices.product_id, round(sum(Prices.price*UnitsSold.units)/sum(UnitsSold.units),2) as average_price 
from Prices left join UnitsSold 
on Prices.product_id = UnitsSold.product_id
where UnitsSold.purchase_date between Prices.start_date and Prices.end_date
group by Prices.product_id 
