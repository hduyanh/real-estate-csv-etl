USE real_estate;
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (customer_id VARCHAR(30), first_name VARCHAR(30), surname VARCHAR(30), gender VARCHAR(30), PRIMARY KEY (customer_id));