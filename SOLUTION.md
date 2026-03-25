# Data Engineering Assignment – Solution

## Overview

This project implements a data pipeline that extracts, transforms, and loads customer, order, and order item data into a PostgreSQL database. The goal was to ensure data quality, enforce constraints, and maintain referential integrity across related datasets.

---

## Schema Design

Three tables were created:

- **customers**
- **orders**
- **order_items**

The schema includes:

- Primary keys on all tables
- Foreign key relationships:
  - `orders.customer_id → customers.customer_id`
  - `order_items.order_id → orders.order_id`
- NOT NULL constraints on critical fields
- A UNIQUE constraint on lowercase email values
- CHECK constraints:
  - Valid order statuses (`placed`, `shipped`, `cancelled`, `refunded`)
  - Positive quantity and unit price in `order_items`

This ensures strong data integrity at the database level.

---

## Data Transformation

### Customers

- Emails were normalized to lowercase
- Duplicate emails were removed by keeping the earliest `signup_date`
- Invalid email formats were filtered out
- Column inconsistencies (e.g., `is_active`) were cleaned and standardized

### Orders

- Status values were normalized (e.g., `processing` → `placed`)
- Only valid statuses were retained
- Timestamps were converted to proper datetime format
- Orders with invalid `customer_id` values were removed to maintain referential integrity

### Order Items

- Rows with `quantity <= 0` or `unit_price <= 0` were removed
- Records referencing invalid `order_id` values were filtered out

---

## Data Integrity Approach

Data was validated at multiple stages:

- During transformation (Python)
- During loading (PostgreSQL constraints)

Foreign key violations and duplicate key errors were encountered during development and resolved by refining transformation logic to ensure all relationships were valid before insertion.

---

## Loading Strategy

Data was loaded into PostgreSQL using SQLAlchemy in the following order:

1. customers  
2. orders  
3. order_items  

This ensured that all foreign key dependencies were satisfied.

---

## Trade-offs and Decisions

- Invalid records (e.g., bad emails, missing relationships) were removed instead of corrected to prioritize data integrity
- Transformation logic was aligned closely with database constraints to prevent load-time failures
- Simplicity was prioritized in the pipeline design to ensure clarity and reproducibility

---

## Conclusion

The final pipeline ensures clean, consistent, and reliable data that adheres to the defined schema and business rules. It demonstrates a structured approach to data engineering, including validation, transformation, and constraint-driven design.
