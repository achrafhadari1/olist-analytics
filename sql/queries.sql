--- tables used: 
olist_order_items_dataset 
olist_orders_dataset 
product_category_name_translation
olist_products_dataset
olist_customers_dataset

# Convert date columns to datetime

alter table olist_orders_dataset ADD(

 order_purchase_timestamp_new DATE,
 order_approved_at_new DATE,
 order_delivered_carrier_date_new DATE,
 order_delivered_customer_date_new DATE,
 order_estimated_delivery_date_new DATE
 );

UPDATE olist_orders_dataset
SET 
    order_purchase_timestamp_new = TO_DATE(order_purchase_timestamp, 'YYYY-MM-DD HH24:MI:SS'),
    order_approved_at_new = TO_DATE(order_approved_at, 'YYYY-MM-DD HH24:MI:SS'),
    order_delivered_carrier_date_new = TO_DATE(order_delivered_carrier_date, 'YYYY-MM-DD HH24:MI:SS'),
    order_delivered_customer_date_new = TO_DATE(order_delivered_customer_date, 'YYYY-MM-DD HH24:MI:SS'),
    order_estimated_delivery_date_new = TO_DATE(order_estimated_delivery_date, 'YYYY-MM-DD HH24:MI:SS');

alter table olist_orders_dataset
drop column order_purchase_timestamp,
drop column order_approved_at,
drop column order_delivered_carrier_date,
drop column order_delivered_customer_date,
drop column order_estimated_delivery_date;

ALTER TABLE olist_orders_dataset
RENAME COLUMN order_purchase_timestamp_new TO order_purchase_timestamp,
RENAME COLUMN order_approved_at_new TO order_approved_at,
RENAME COLUMN order_delivered_carrier_date_new TO order_delivered_carrier_date,
RENAME COLUMN order_delivered_customer_date_new TO order_delivered_customer_date,
RENAME COLUMN order_estimated_delivery_date_new TO order_estimated_delivery_date;


alter table olist_order_items_dataset
add shipping_limit_date_new DATE;

UPDATE olist_order_items_dataset 
	SET shipping_limit_date_new=TO_DATE(shipping_limit_date, 'YYYY-MM-DD HH24:MI:SS');

alter table olist_order_items_dataset
 drop column shipping_limit_date;

 alter table olist_order_items_dataset
 rename column shipping_limit_date_new to shipping_limit_date;

 # Products + English category translation

MERGE INTO olist_products_dataset brazil
USING product_category_name_translation english 
ON (brazil.product_category_name=english.product_category_name)
WHEN MATCHED THEN 
 	UPDATE SET brazil.product_category_name=english.product_category_name_english;


# Q1 - Late delivery percentage
SELECT 
    ROUND(
        COUNT(CASE WHEN order_delivered_customer_date > order_estimated_delivery_date THEN 1 END) * 100.0 / COUNT(*), 
        2
    ) || '%' AS late_percentage
FROM olist_orders_dataset;

# Q2 — Revenue by product category (top 10)
# olist_products_dataset olist_order_items_dataset  .product_id

select * from (
	select
	 p.product_category_name, 
	 sum(i.price) as total_sales
	 from olist_order_items_dataset i 
	 join olist_products_dataset p on p.product_id=i.product_id
	 group by p.product_category_name
	 order by total_sales desc
	 ) 
where rownum <=10;

#Q3 — Average delivery time by state

select c.customer_state,round(avg(o.order_delivered_customer_date-o.order_purchase_timestamp),2) as avg_days
from olist_orders_dataset o join olist_customers_dataset c on o.customer_id=c.customer_id
where o.order_delivered_customer_date IS NOT NULL
 group by c.customer_state
 order by avg_days desc;


# Q4 — Monthly order trend

select TO_CHAR(order_purchase_timestamp,'YYYY-MM') as month, 
count(order_id) as orders 
from olist_orders_dataset
group by TO_CHAR(order_purchase_timestamp,'YYYY-MM')
order by orders desc;

# Q5 — Top 10 customers by total spend

select * from (
	select
	 o.customer_id, sum(i.price) as total_purchases
	 from olist_orders_dataset o join olist_order_items_dataset i 
	 on o.order_id=i.order_id
	 group by o.customer_id
	 order by total_purchases desc 
	 )
where rownum <=10;