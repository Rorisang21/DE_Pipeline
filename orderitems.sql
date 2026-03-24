CREATE TABLE order_items (
    order_id BIGINT,
    line_no INTEGER,
    sku TEXT,
    quantity INTEGER CHECK (quantity > 0),
    unit_price NUMERIC(12,2) CHECK (unit_price > 0),
    category TEXT,
    PRIMARY KEY (order_id, line_no),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);