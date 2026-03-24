CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    customer_id INTEGER,
    order_ts TIMESTAMP,
    status TEXT NOT NULL CHECK (status IN ('placed', 'shipped', 'cancelled', 'refunded')),
    total_amount NUMERIC(12,2),
    currency CHAR(3),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);