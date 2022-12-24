USE real_estate;

DROP TABLE IF EXISTS properties;

CREATE TABLE properties (
    property_id INT ,
    building INT,
    property_type VARCHAR(30),
    property_tier INT,
    area VARCHAR(30),
    property_status VARCHAR(30),
    square_meter FLOAT(10,2)
    country VARCHAR(30),
    property_state VARCHAR(30),
    customer_id INT,
    PRIMARY KEY (property_id)
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);