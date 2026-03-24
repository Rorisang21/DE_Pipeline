CREATE TABLE customers (
customer_id INTEGER PRIMARY KEY,
email TEXT CHECK (email = LOWER(email)),
full_name TEXT,
sign_up DATE,
country_code CHAR(2),
is_active BOOLEAN

)