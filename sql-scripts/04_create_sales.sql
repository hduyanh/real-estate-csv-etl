USE real_estate;

DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    sales_id INT ,
    year_of_sale YEAR,
    month_of_sale INT,
    price INT,
    deal_status VARCHAR(30),
    mortgage VARCHAR(30),
    meter_price FLOAT(10,2),
    property_id INT,
    customer_id INT,
    entity VARCHAR(30),
    purpose VARCHAR(30),
    age_of_buy INT,
    interval VARCHAR(30),
    y INT,
    M INT,
    D INT,
    PRIMARY KEY (sales_id)
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    FOREIGN KEY (properties_id) REFERENCES properties(properties_id)
);