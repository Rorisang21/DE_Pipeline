I have created three tables mainly: customers, orders, and order_items. In the creation of these tables, primary keys and foreign keys were used to create a relationship between the tables. 

Please notice that in the database the email is constrained to lowercase; this is so that even when someone does bypass the Python script and load directly into the database, the email is still kept lowercase and also to prevent duplication.

Several constraints were applied to ensure data quality:

- NOT NULL constraints on critical fields such as email, order timestamp, and status, if anything gets rejected  there will be  a log letting us know if anything was rejected. 
- A CHECK constraint on order status to allow only valid values (placed, shipped, cancelled, or refunded)

- CHECK constraints on order_items to ensure quantity and unit price are positive
Data cleaning and normalization are handled during the transformation stage using Python.

The database is responsible for enforcing strict rules and maintaining data integrity. Any data that does not meet the required constraints is rejected at the database level.

Rejected records are logged and tracked to ensure visibility into data quality issues and allow for further investigation if needed.
I chose to enforce strict constraints at the database level to ensure data reliability and consistency, even if it results in rejecting some records.

This approach prioritizes data integrity over accepting potentially inconsistent or invalid data.
